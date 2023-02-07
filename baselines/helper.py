import json

def load_config(config_path='../config.json'):
	with open(config_path) as cf:
		config = json.load(cf)
	
	return config

def load_data(config):
  with open(config['folds_path'], 'r', encoding='utf-8') as f:
    folds = json.load(f)
  
  with open(config['data_path']) as f:
    all_data = json.load(f)

  train_inds = folds[0][0]
  val_inds = folds[0][1]
  test_inds = folds[0][2]

  train_data = [all_data[i] for i in train_inds]
  val_data = [all_data[i] for i in val_inds]
  test_data = [all_data[i] for i in test_inds]

  return train_data, val_data, test_data

# aggregation function
def aggregate(scores, fcn):
  agg_scores = []

  for ind in range(len(scores[0])):
    l = [float(sublst[ind]) for sublst in scores]
    val = fcn(l)
    agg_scores.append(val)

  return agg_scores