import numpy as np
import torch

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