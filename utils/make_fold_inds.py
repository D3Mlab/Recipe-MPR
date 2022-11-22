'''
Inputs
	- k (number of experiment runs, i.e. folds): int, default = 1
	- train_frac: float, default = 0.1 ##train fraction of data
	- val_frac: float, default = 0.1 ##validation fraction of data
	- seed: int, default = 0
	- data_path: string, default = ../data/500QA.json

Outputs
- return indicies for folds as 3 level list: [[[list of train indicies for fold 1],[list of val indicies for fold 1],[list of test indicies for fold 1]], [fold 2], ...]
'''

import argparse
import random
import math
import json

def make_fold_inds(k = 1, train_frac = 0.1, val_frac = 0.5, seed = 0, data_path = "../data/500QA.json", write_path = "../data/fold_inds"):
	random.seed(seed)

	all_fold_inds = []

	#get dataset length
	with open(data_path) as f:
		data = json.load(f)

	n = len(data)

	#make list of indicies
	ordered_inds = list(range(n))
	
	for i in range(k):
		#make lists for train_inds, val_inds, test_inds and aggregate into kth_fold_inds

		shuffled_inds = random.sample(ordered_inds,n)

		train_inds = shuffled_inds[0:math.ceil(n*train_frac)]
		val_inds = shuffled_inds[math.ceil(n*train_frac):(math.ceil(n*train_frac) + math.ceil(n*val_frac))]
		test_inds = shuffled_inds[(math.ceil(n*train_frac) + math.ceil(n*val_frac)):]
		
		kth_fold_inds = [train_inds,val_inds,test_inds]
		all_fold_inds.append(kth_fold_inds)

	with open(write_path,w) as f:
		for i in range(k):
			f.writeline(all_fold_inds[i])

	return all_fold_inds

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-k', default = 1)
	parser.add_argument('-train_frac', default = 0.1)
	parser.add_argument('-val_frac', default = 0.1)
	parser.add_argument('-seed', default = 0)
	parser.add_argument('-data_path', default = "../data/500QA.json")
	parser.add_argument('-write_path', default = "../data/fold_inds")

	args = parser.parse_args()

	make_fold_inds(k = int(args.k), train_frac = float(args.train_frac), val_frac = float(args.val_frac), seed = float(args.seed), data_path = args.data_path, write_path = args.write_path)

