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