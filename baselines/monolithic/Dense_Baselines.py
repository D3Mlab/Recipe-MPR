from transformers import AutoTokenizer, AutoModel
from sklearn.utils import shuffle
import numpy as np
import torch

class NeuralEmbedder():
    def __init__(self, model_name, tokenizer_name):
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name) 
        self.model = AutoModel.from_pretrained(model_name)
        
    def embed(self,text):
        return self.model(**self.tokenizer(text,return_tensors="pt"))[0][:,0,:].squeeze(0).numpy()

class NeuralSearchEngine():
    def __init__(self, embedder):
        self.embedder = embedder

    def index(self, documents):
        self.documents = documents
        encoded_docs = []
        for d in documents:
            with torch.no_grad():
                d_encoded = self.embedder.embed(d)
            encoded_docs.append(d_encoded.reshape(-1,768))
        self.index = np.concatenate(encoded_docs,axis=0)
    
    def search(self, query):
        with torch.no_grad():
            q_encoded = self.embedder.embed(query).reshape(-1,768)
        scores = q_encoded.dot(self.index.T)[0]

        scores, self.documents = shuffle(scores, self.documents, random_state=0)
        args = np.argsort(scores)[::-1]

        predicted = ""
        for i in range(3):
            if i == 0:
                predicted = self.documents[args[i]]
             
        return predicted



def dense_pred(data, model_name):

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

    # create a search engine object for this query 
    engine = NeuralSearchEngine(embedder)
    # index the options into the search engine
    engine.index(docs)

    # check if model predicted the correct answer
    ## get the predicted description
    predicted_description = engine.search(sample["query"])
    ## loop through all correct options to find the predicted id
    for option in sample["options"]:
      if sample["options"][option] == predicted_description:
        predicted_id = option
    predictions.append(predicted_description)
    

  return predictions