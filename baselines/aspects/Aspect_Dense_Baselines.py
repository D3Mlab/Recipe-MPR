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
  
  # aggregation function
	def _aggregate(self, scores, fcn):
		agg_scores = []

		for ind in range(len(scores[0])):
			l = [float(sublst[ind]) for sublst in scores]
			val = fcn(l)
			agg_scores.append(val)

		return agg_scores
  
	def search(self, aspects, agg_fcn):
		all_scores = []
		for a in aspects:
			with torch.no_grad():
				q_encoded = self.embedder.embed(a).reshape(-1,768)
			scores = q_encoded.dot(self.index.T)[0]
			all_scores.append(scores)

		agg_scores = self._aggregate(all_scores, agg_fcn)

		agg_scores, self.documents = shuffle(agg_scores, self.documents, random_state=0)
		args = np.argsort(agg_scores)[::-1]

		predicted = ""
		for i in range(3):
			if i == 0:
				predicted = self.documents[args[i]]
			
		return predicted