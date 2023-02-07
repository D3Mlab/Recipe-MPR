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

  all_train = []
  all_val = []
  all_test = []

  for i in range(len(folds)):
    train_inds = folds[i][0]
    val_inds = folds[i][1]
    test_inds = folds[i][2]

    train_data = [all_data[j] for j in train_inds]
    val_data = [all_data[j] for j in val_inds]
    test_data = [all_data[j] for j in test_inds]
    all_train.append(train_data)
    all_val.append(val_data)
    all_test.append(test_data)

  return all_train, all_val, all_test

# aggregation function
def aggregate(scores, fcn):
  agg_scores = []

  for ind in range(len(scores[0])):
    l = [float(sublst[ind]) for sublst in scores]
    val = fcn(l)
    agg_scores.append(val)

  return agg_scores