from transformers import AutoTokenizer, AutoModel
from sklearn.utils import shuffle
import numpy as np
import torch
import sys
sys.path.append('..')
from helper import *
import json


class NeuralEmbedder():
    def __init__(self, model_name, tokenizer_name):
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name) 
        self.model = AutoModel.from_pretrained(model_name)
        
    def embed(self,text):
        return self.model(**self.tokenizer(text,return_tensors="pt"))[0][:,0,:].squeeze(0).numpy()

class GPT3Embedder():
    def __init__(self, model_name, tokenizer_name):
        with open(model_name) as f:
            self.embeddings = json.load(f)

    def embed(self,text):
        return np.array(self.embeddings[text])



class NeuralSearchEngine():
    def __init__(self, embedder):
        self.embedder = embedder

    def index(self, documents):
        self.documents = documents
        encoded_docs = []
        for d in documents:
            with torch.no_grad():
                d_encoded = self.embedder.embed(d)
            encoded_docs.append(d_encoded.reshape(1,-1))
        self.index = np.concatenate(encoded_docs,axis=0)
  
    def search(self, aspects, agg_fcn):
        all_scores = []
        for a in aspects:
            with torch.no_grad():
                q_encoded = self.embedder.embed(a).reshape(1,-1)
            scores = q_encoded.dot(self.index.T)[0]
            all_scores.append(scores)

        agg_scores = aggregate(all_scores, agg_fcn)
        # print(agg_scores,self.documents)
        agg_scores, self.documents = shuffle(agg_scores, self.documents, random_state=0)
        args = np.argsort(agg_scores)[::-1]

        predicted = ""
        for i in range(len(args)):
            if i == 0:
                predicted = self.documents[args[i]]
            
        return predicted




def aspect_dense_pred(data, model_name, agg_fcn):

  # create an embedder object the tokenizer and model 
  if '.json'in model_name:
    embedder = GPT3Embedder(model_name, model_name)
  else:
    embedder = NeuralEmbedder(model_name, model_name)

  predictions = []
  # loop through each query
  for sample in data:
    # for key in sample['query_type']:
    #     if sample['query_type'][key] == 1:
    #       type_count[key] += 1

    docs = []
    for description in sample["options"].values():
      docs.append(description)
    engine = NeuralSearchEngine(embedder)
    engine.index(docs)
    aspects = [str(a) for a in sample["correctness_explanation"].keys()]
    predicted_description = engine.search(aspects, agg_fcn)
    predictions.append(predicted_description)

  return predictions