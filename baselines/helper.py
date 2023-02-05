import json
#from transformers import  AutoTokenizer, OPTForCausalLM, GPT2Tokenizer, GPT2LMHeadModel, OpenAIGPTLMHeadModel, OpenAIGPTTokenizer

def load_config(config_path):
	with open(config_path) as cf:
		config = json.load(cf)

	with open(config['data_path']) as df:
		all_data = json.load(df)

	with open(config['folds_path'], 'r', encoding='utf-8') as f:
		folds = json.load(f)
	
	return all_data, folds

def get_model(model_name):
	model_config = {
		"facebook/opt-1.3b": [OPTForCausalLM, AutoTokenizer], 
		"gpt2": [GPT2LMHeadModel, GPT2Tokenizer],
		"openai-gpt": [OpenAIGPTLMHeadModel, OpenAIGPTTokenizer],
		"microsoft/DialoGPT-large": [GPT2LMHeadModel, GPT2Tokenizer]
	}
	return model_config[model_name][0], model_config[model_name][1]

# aggregation function
def aggregate(scores, fcn):
  agg_scores = []

  for ind in range(len(scores[0])):
    l = [float(sublst[ind]) for sublst in scores]
    val = fcn(l)
    agg_scores.append(val)

  return agg_scores