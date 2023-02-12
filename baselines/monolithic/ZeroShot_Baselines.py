from sklearn.utils import shuffle
import numpy as np
import torch
from helper import get_model_and_tokenizer

# document conditioned on query
class QAModel():

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

    scores, options = shuffle(scores, options, random_state=0)
    args = np.argsort(scores)
    return options[args[-1]]




def ZS_pred(data,model_name):
  # model_config = {
  #   "facebook/opt-1.3b": [OPTForCausalLM, AutoTokenizer], 
  #   "gpt2": [GPT2LMHeadModel, GPT2Tokenizer]
  # }
  
  lm_model, tokenizer = get_model_and_tokenizer(model_name)
  model = QAModel(lm_model, tokenizer, model_name, device='cuda')

  prediction = []
  for sample in data:
    # for key in sample['query_type']:
    #   if sample['query_type'][key] == 1:
    #     type_count[key] += 1
    options_list = [val for val in sample['options'].values()]
    query = sample['query']
    correct_answer = sample['options'][sample['answer']]
    answer = model.get_answer(query, options_list)
    prediction.append(answer)

  return prediction