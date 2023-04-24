from helper import * 
import argparse
from eval import evaluate
from aspects.Aspect_Dense_Baselines import aspect_dense_pred 
from aspects.Aspect_Sparse_Baselines import aspect_sparse_pred,aspect_sparse_types 
from aspects.Aspect_FewShot_Baselines import aspect_FS_pred 
from aspects.Aspect_ZeroShot_Baselines import aspect_ZS_pred 
from aspects.Aspect_GPT3_Text_Baseline import aspect_gpt3_pred
from random import sample
from monolithic.Dense_Baselines import dense_pred
from monolithic.FewShot_Baselines import FS_pred
from monolithic.Sparse_Baselines import sparse_pred, sparse_types
from monolithic.ZeroShot_Baselines import ZS_pred
from monolithic.GPT3_Text_Baseline import gpt3_pred
import os
import pandas as pd
import numpy as np
import random



parser = argparse.ArgumentParser(description='Train LM')
parser.add_argument('--monolithic', action='store_true')
parser.add_argument('--eval_on_val', action='store_true')
parser.add_argument('--type', type=str, default='sparse',help='one of sparse, dense, ZS, FS')
parser.add_argument('--sparse_type', type=str, default='BM25',help='one of BM25 TF-IDF or OWC')
parser.add_argument('--LM', type=str, default='gpt2')
parser.add_argument('--agg_func', type=str, default='min')
parser.add_argument('--fold_number', type=int, default=0) # -1 for all folds
parser.add_argument('--seed', type=int, default=100)
parser.add_argument('--FS_num', type=int, default=5)
parser.add_argument('--result_root', type=str, default='results')
parser.add_argument('--folds_path', type=str)


agg_fcns = {"min":min, "max":max, "amean":np.mean, "gmean":custom_gmean}


LM_names = {'gpt2':'gpt2',
'opt':'facebook/opt-1.3b',
'bert':"bert-base-uncased",
'tas-b':'sebastian-hofstaetter/distilbert-dot-tas_b-b256-msmarco',
'agribert':'recobo/agriculture-bert-uncased',
'dfood':'chambliss/distilbert-for-food-extraction',
'foodNER':'Dizex/FoodBaseBERT-NER',
'gpt3-ada':'embeddings_ada_with_aspects.json'}


def run_experiment():
    args = parser.parse_args()
    if args.fold_number ==-1:
        folds = list(range(5))
        # folds = list(range(5,20))
    else:
        folds = [args.fold_number]
    for fold in folds:
        perform_experiment(fold,args)

def perform_experiment(fold,args):
    # config = load_config('./config.json')
    # print(config)
    
   

    exp_config = {'fold_number':fold,
                'agg_func':args.agg_func,
                'LM':args.LM,
                'type':args.type,
                'sparse_type':args.sparse_type,
                'monolithic':args.monolithic,
                'seed':args.seed,
                'result_root':args.result_root,
                'FS_num':args.FS_num,
                'eval_on_val':args.eval_on_val,
                'folds_path':args.folds_path}

    train_splits, val_splits, test_splits = load_data(exp_config['folds_path'],data_path="../data/500QA.json")


    random.seed(exp_config['seed'])
    # print(len(train_splits))
    train_data = train_splits[exp_config['fold_number']]
    if args.eval_on_val:
        test_data = val_splits[exp_config['fold_number']]
        print('Evaluation on validation set!!!!')
    else:
        test_data = test_splits[exp_config['fold_number']]

    original_test_data = test_data.copy()

    if args.eval_on_val:
        train_data = train_data[:exp_config['FS_num']]
    else:
        train_data = random.sample(train_data, exp_config['FS_num'])

    if exp_config['monolithic']:
        if exp_config['LM'] == 'DV3':
            if exp_config['type']== 'FS':
                predictions = gpt3_pred(train_data,test_data, prompt_size=exp_config['FS_num'],fewshot=True)
            else:
                predictions = gpt3_pred(train_data,test_data, prompt_size=0,fewshot=False)
        elif exp_config['type'] == 'sparse':
            st = sparse_types[exp_config['sparse_type']]
            predictions = sparse_pred(test_data,st)
        elif exp_config['type'] == 'dense':
            predictions = dense_pred(test_data,LM_names[exp_config['LM']])
        elif exp_config['type'] == 'ZS':
            predictions = ZS_pred(test_data,LM_names[exp_config['LM']])
        elif exp_config['type'] == 'FS':
            predictions = FS_pred(train_data,test_data,LM_names[exp_config['LM']], prompt_size=exp_config['FS_num'])
        

    else: # aspect
        agg  = agg_fcns[exp_config['agg_func']]
        if exp_config['LM'] == 'DV3':
            predictions = aspect_gpt3_pred(train_data,test_data,agg_fcn=agg, prompt_size=exp_config['FS_num'],fewshot=exp_config['type']=='FS')
        elif exp_config['type'] == 'sparse':
            st = aspect_sparse_types[exp_config['sparse_type']]
            predictions = aspect_sparse_pred(test_data,sparse_method=st,agg_fcn=agg)
        elif exp_config['type'] == 'dense':
            predictions = aspect_dense_pred(test_data,LM_names[exp_config['LM']],agg_fcn=agg)
        elif exp_config['type'] == 'ZS':
            predictions = aspect_ZS_pred(test_data,LM_names[exp_config['LM']],agg_fcn=agg)
        elif exp_config['type'] == 'FS':
            predictions = aspect_FS_pred(train_data,test_data,LM_names[exp_config['LM']],agg_fcn=agg, prompt_size=exp_config['FS_num'])

    EXP_NAME = "_".join([str(exp_config['monolithic']),str(exp_config['type']),str(exp_config['agg_func']),str(exp_config['LM']),str(exp_config['sparse_type']),str(exp_config['seed']),str(exp_config['FS_num'])])
    # ,
    result_root = exp_config['result_root']
    if not os.path.exists(result_root):
        os.mkdir(result_root)
    exp_dir = os.path.join(result_root,EXP_NAME)
    if not os.path.exists(exp_dir):
        os.mkdir(exp_dir)
    
    evals_folder = os.path.join(exp_dir,'evals')
    if not os.path.exists(evals_folder):
        os.mkdir(evals_folder)
    preds_folder = os.path.join(exp_dir,'preds')
    if not os.path.exists(preds_folder):
        os.mkdir(preds_folder)
    output_path = os.path.join(evals_folder, str(exp_config['fold_number']) + '_' + EXP_NAME + '.csv')
    preds_path = os.path.join(preds_folder,  'pred_'+str(exp_config['fold_number']) + '_' + EXP_NAME + '.json')


    df = evaluate(original_test_data,predictions)
    df.to_csv(output_path)
    for i,sample in enumerate(original_test_data):
        sample['pred'] = predictions[i]
    with open(preds_path, "w") as outfile:
        json.dump(original_test_data, outfile)
     
    configs_folder = os.path.join(exp_dir,'configs')
    if not os.path.exists(configs_folder):
        os.mkdir(configs_folder)


    config_pd =pd.DataFrame.from_dict(exp_config, orient="index")
    output_path = os.path.join(configs_folder, 'config_'+ str(exp_config['fold_number']) + '_' + EXP_NAME + '.csv')
    config_pd.to_csv(output_path)

run_experiment()




    
    