import json

def load_config(config_path='../config.json'):
	with open(config_path) as cf:
		config = json.load(cf)
	
	return config

# aggregation function
def aggregate(scores, fcn):
  agg_scores = []

  for ind in range(len(scores[0])):
    l = [float(sublst[ind]) for sublst in scores]
    val = fcn(l)
    agg_scores.append(val)

  return agg_scores