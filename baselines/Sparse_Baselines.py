import math
import pandas as pd
from sklearn.utils import shuffle
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import nltk, nltk.stem, nltk.corpus, nltk.tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
import json
import torch
from nltk.tokenize import word_tokenize
from scipy import sparse

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Base class for sparse IR methods
class Sparse_Baseline():
    def __init__(self, path):
        self.path = path
        self.descriptions = []
        self.type_correct = {
            "Specific": 0,
            "Subjective": 0,
            "Indirect": 0,
            "Compound": 0,
            "Negated": 0,
            "Analogical": 0,
            "Temporal": 0}
        with open(self.path) as f:
            self.data = json.load(f)

    def _filter(self, text):
        lemmatizer = WordNetLemmatizer()
        stop = set(stopwords.words('english') + list(string.punctuation))

        lst_tokens = [i for i in word_tokenize(text.lower()) if i not in stop]
        lemmatized_lst = []
        for token in lst_tokens:
            lemmatized_token = lemmatizer.lemmatize(token)
            lemmatized_lst.append(lemmatized_token)
        lemmatized_sentence = " ".join(lemmatized_lst)
        return lemmatized_sentence
    
    def clean_data(self):
        all_descriptions = []
        for d in self.data:
            d["query"] = self._filter(d["query"])
            for o in d["options"]:
                d["options"][o] = self._filter(d["options"][o])
                all_descriptions.append(d["options"][o])

        self.descriptions = all_descriptions
        return self.descriptions

class OWC(Sparse_Baseline):
    def __init__(self, path):
        super().__init__(path)

    def _calc_overlap(self, s1, s2):
        s1_list = s1.split(' ')
        s2_list = s2.split(' ')
        return len(list(set(s1_list)&set(s2_list)))

    # General function to determine correct answer based on word overlap after pre-processing
    def get_results(self):
        results = []
        correct = 0
        total = len(self.data)
            
        for d in self.data:
            try:
                options = [val for val in d['options'].values()]
                query = d['query']
                answer = d['options'][d['answer']]
            except:
                continue
            
            options_str = [str(i) for i in options]
            cleaned_query = str(query)
            
            overlap = []
            for option in options_str:
                cleaned_option = option
                num_overlap = self._calc_overlap(cleaned_query, cleaned_option)
                overlap.append(num_overlap)
                
            overlap, options = shuffle(overlap, options, random_state=0)
            ind = np.argmax(overlap) 
            result = 0
            if (options[ind]) == answer:
                correct += 1
                result = 1
                for key in d['query_type']:
                    if d['query_type'][key] == 1:
                        self.type_correct[key] += 1
            #results.append([result, "Query: " + query, "Recommended: " + str(options[ind])])
        print("Total correct answers: {} out of {}".format(correct, total))
        #print(results)
        print(self.type_correct)

class TFIDF(Sparse_Baseline):
    def __init__(self, path):
        self.doc_freq = {}
        super().__init__(path)

    # calculate document frequency for terms based on corpus of descriptions
    def calc_df(self, docs):
        for doc in docs:
            words = doc.split(' ')
            words = list(set(words))
            for w in words:
                if w in self.doc_freq.keys():
                    self.doc_freq[w] += 1
                else:
                    self.doc_freq.update({w:1})

    # General function to compute tfidf score for each query using corpus of descriptions
    def get_results(self):
        results = []
        correct = 0
        total = len(self.data)
            
        for d in self.data:
            try:
                options = [val for val in d['options'].values()]
                query = d['query']
                answer = d['options'][d['answer']]
            except:
                continue
            
            options_str = [str(i) for i in options]
            query_str = query.split(' ')
            
            doc_scores = []
            for option in options_str:
                score = 0
                # sum over query terms in each document
                for term in query_str:
                    freq = option.count(term)
                    if freq != 0:
                        tf = 1 + math.log10(freq)
                    else:
                        tf = 0
                    if term in self.doc_freq.keys():
                        idf = math.log10(len(self.descriptions)/(self.doc_freq[term] + 1))
                    else:
                        idf = math.log10(len(self.descriptions))
                    score += tf*idf
                doc_scores.append(score)

            # choose option that has highest similarity as correct answer
            doc_scores, options = shuffle(doc_scores, options, random_state=0)
            ind = np.argmax(doc_scores) 
            result = 0
            if (options[ind]) == answer:
                correct += 1
                result = 1
                for key in d['query_type']:
                    if d['query_type'][key] == 1:
                        self.type_correct[key] += 1
            #results.append([result, "Query: " + query, "Recommended: " + str(options[ind])])

        print("Total correct answers: {} out of {}".format(correct, total))
        #print(results)
        print(self.type_correct)
        return correct, total

class BM25(Sparse_Baseline):
    def __init__(self, path, b=0.75, k1=1.6):
        self.vectorizer = TfidfVectorizer(norm=None, smooth_idf=False)
        self.b = b
        self.k1 = k1
        super().__init__(path)

    def _fit(self, X):
        """ Fit IDF to documents X """
        self.vectorizer.fit(X)
        y = super(TfidfVectorizer, self.vectorizer).transform(X)
        self.avdl = y.sum(1).mean()

    def _transform(self, q, X):
        """ Calculate BM25 between query q and documents X """
        b, k1, avdl = self.b, self.k1, self.avdl

        # apply CountVectorizer
        X = super(TfidfVectorizer, self.vectorizer).transform(X)
        len_X = X.sum(1).A1
        q, = super(TfidfVectorizer, self.vectorizer).transform([q])
        assert sparse.isspmatrix_csr(q)

        # convert to csc for better column slicing
        X = X.tocsc()[:, q.indices]
        denom = X + (k1 * (1 - b + b * len_X / avdl))[:, None]
        idf = self.vectorizer._tfidf.idf_[None, q.indices] - 1.
        numer = X.multiply(np.broadcast_to(idf, X.shape)) * (k1 + 1)
        return (numer / denom).sum(1).A1
    
    def get_results(self):
        results = []
        correct = 0
        total = len(self.data)
        self._fit(self.descriptions)

        for d in self.data:
            try:
                options = [val for val in d['options'].values()]
                query = d['query']
                answer = d['options'][d['answer']]
            except:
                continue
            
            options_str = [str(i) for i in options]
            doc_scores = self._transform(query, options_str)
            
            # choose option that has highest similarity as correct answer
            doc_scores, options = shuffle(doc_scores, options, random_state=0)
            ind = np.argmax(doc_scores) 
            result = 0
            if (options[ind]) == answer:
                correct += 1
            result = 1
            for key in d['query_type']:
                if d['query_type'][key] == 1:
                    self.type_correct[key] += 1
            #results.append([result, "Query: " + query, "Recommended: " + str(options[ind])])

        print("Total correct answers: {} out of {}".format(correct, total))
        #print(results)
        print(self.type_correct)

        return correct, total