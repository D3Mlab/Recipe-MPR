'''
Inputs
	- k (number of experiment runs, i.e. folds): int, default = 1
	- train_frac: float, default = 0.1 ##train fraction of data
	- val_frac: float, default = 0.1 ##validation fraction of data
	- seed: int, default = 0
	- data_path: string, default = ../data/500QA.json

Outputs
- writes indicies for folds as 3 level list: [[[list of train indicies for fold 1],[list of val indicies for fold 1],[list of test indicies for fold 1]], [fold 2], ...]
'''

import argparse
import random
import math
import json

def make_fold_inds(K = 1, train_frac = 0.1, val_frac = 0.5, seed = 0, data_path = "../data/500QA.json", write_path = "../data/fold_inds.json"):
	random.seed(seed)

	all_fold_inds = []

	#get dataset length
	with open(data_path) as f:
		data = json.load(f)

	n = len(data)

	#make list of ordered indicies
	ordered_inds = list(range(n))
	
	for i in range(K):
		#make lists for train_inds, val_inds, test_inds and aggregate into kth_fold_inds

		shuffled_inds = random.sample(ordered_inds,n)

		#slice based on train/val/test fractions
		train_inds = shuffled_inds[0:math.ceil(n*train_frac)]
		val_inds = shuffled_inds[math.ceil(n*train_frac):(math.ceil(n*train_frac) + math.ceil(n*val_frac))]
		test_inds = shuffled_inds[(math.ceil(n*train_frac) + math.ceil(n*val_frac)):]
		
		kth_fold_inds = [train_inds,val_inds,test_inds]
		all_fold_inds.append(kth_fold_inds)

	#write
	with open(write_path, 'w') as f:
		json.dump(all_fold_inds,f)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-K', default = 1)
	parser.add_argument('-train_frac', default = 0.1)
	parser.add_argument('-val_frac', default = 0.1)
	parser.add_argument('-seed', default = 0)
	parser.add_argument('-data_path', default = "../data/500QA.json")
	parser.add_argument('-write_path', default = "../data/fold_inds.json")

	args = parser.parse_args()

	make_fold_inds(K = int(args.K), train_frac = float(args.train_frac), val_frac = float(args.val_frac), seed = float(args.seed), data_path = args.data_path, write_path = args.write_path)

