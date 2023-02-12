import numpy as np
import torch
from transformers import  AutoTokenizer, OPTForCausalLM, AutoModel, GPT2Tokenizer, GPT2LMHeadModel
from helper import get_model_and_tokenizer, aggregate
from sklearn.utils import shuffle


def aspect_ZS_pred(data, model_name, agg_fcn):

  model_class, tokenizer_class = get_model_and_tokenizer(model_name)
  model = Aspect_QAModel(model_class,tokenizer_class,model_name)
  predictions = []
  for sample in data:

    options_list = [val for val in sample['options'].values()]
    aspects = sample['correctness_explanation'].keys()
    correct_answer = sample['options'][sample['answer']]
    all_scores = []

    for a in aspects:
      scores = model.get_answer(a, options_list)
      all_scores.append(scores)

    agg_scores = aggregate(all_scores, agg_fcn)
    agg_scores, options_list = shuffle(agg_scores, options_list, random_state=0)
    args = np.argsort(agg_scores)
    answer = options_list[args[-1]]
    predictions.append(answer)

  return predictions



# document conditioned on query
class Aspect_QAModel():
  
  def __init__(self, model, tokenizer, model_name, device='cuda'):
    self.model = model.from_pretrained(model_name).to(device)
    self.tokenizer = tokenizer.from_pretrained(model_name)
    self.device = device

  def get_answer(self, q, options):
    scores = []

    for o in options:
      input = self.tokenizer(q+' '+o, return_tensors="pt").input_ids.to(self.device)
      o_input = self.tokenizer(o, return_tensors="pt").to(self.device)
      o_len = o_input.input_ids.size(1)
      target_ids = input.clone()
      target_ids[:, :-o_len] = -100
      with torch.no_grad():
          outputs = self.model(input, labels=target_ids)
          neg_log_likelihood = outputs[0] 

      scores.append((-1*neg_log_likelihood.cpu()))
      
    return scores