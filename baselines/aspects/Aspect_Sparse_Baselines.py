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
import sys
sys.path.append('..')
from helper import *

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Base class for sparse IR methods
class Sparse_Baseline():
    def __init__(self, data):
        self.descriptions = []
        self.type_correct = {
            "Specific": 0,
            "Subjective": 0,
            "Indirect": 0,
            "Compound": 0,
            "Negated": 0,
            "Analogical": 0,
            "Temporal": 0}
        self.data = data

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
            for o in d["options"]:
                d["options"][o] = self._filter(d["options"][o])
                all_descriptions.append(d["options"][o])

        self.descriptions = all_descriptions
        return self.descriptions
    
    def get_results(self, score_fcn, agg_fcn, aspect_dict=None):
        correct = 0
        total = len(self.data)

        for d in self.data:
            try:
                options = [val for val in d['options'].values()]
                query = d['query']
                if aspect_dict == None:
                    aspects = [str(a) for a in d['correctness_explanation'].keys()]
                else:
                    aspects = aspect_dict[query]
                answer = d['options'][d['answer']]
            except Exception as e: 
                print(e)
                continue
            
            options_str = [str(i) for i in options]
            all_scores = []
            for a in aspects:
                doc_scores = score_fcn(a, options_str)
                all_scores.append(doc_scores)
            
            agg_scores = aggregate(all_scores, agg_fcn)
            agg_scores, options = shuffle(agg_scores, options, random_state=0)
            ind = np.argmax(agg_scores) 

            if (options[ind]) == answer:
                correct += 1
                for key in d['query_type']:
                    if d['query_type'][key] == 1:
                        self.type_correct[key] += 1

        print("Total correct answers: {} out of {}".format(correct, total))
        print(self.type_correct)
        return correct, total

class OWC(Sparse_Baseline):
    def __init__(self, data):
        super().__init__(data)

    def _calc_overlap(self, s1, s2):
        s1_list = s1.split(' ')
        s2_list = s2.split(' ')
        return len(list(set(s1_list)&set(s2_list)))
    
    def owc_score(self, aspect, options_str):
        overlap = []
        for option in options_str:    
            num_overlap = self._calc_overlap(aspect, option)
            overlap.append(num_overlap)
        
        return overlap

class TFIDF(Sparse_Baseline):
    def __init__(self, data):
        self.doc_freq = {}
        super().__init__(data)

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
    
    def tfidf_score(self, aspect, options_str):
        doc_scores = []
        a_words = aspect.split(' ')

        for option in options_str:
            score = 0
            # sum over individual aspect words in each doc
            for term in a_words:
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

        return doc_scores

class BM25(Sparse_Baseline):
    def __init__(self, data, b=0.75, k1=1.6):
        self.vectorizer = TfidfVectorizer(norm=None, smooth_idf=False)
        self.b = b
        self.k1 = k1
        super().__init__(data)

    def fit(self, X):
        """ Fit IDF to documents X """
        self.vectorizer.fit(X)
        y = super(TfidfVectorizer, self.vectorizer).transform(X)
        self.avdl = y.sum(1).mean()

    def bm25_score(self, q, X):
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
