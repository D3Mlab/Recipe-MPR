from helper import * 
import argparse
from eval import evaluate
from aspects.Aspect_Dense_Baselines import aspect_dense_pred 
from aspects.Aspect_Sparse_Baselines import aspect_sparse_pred,aspect_sparse_types 
from aspects.Aspect_FewShot_Baselines import aspect_FS_pred 
from aspects.Aspect_ZeroShot_Baselines import aspect_ZS_pred 

from monolithic.Dense_Baselines import dense_pred
from monolithic.FewShot_Baselines import FS_pred
from monolithic.Sparse_Baselines import sparse_pred, sparse_types
from monolithic.ZeroShot_Baselines import ZS_pred
import os
import pandas as pd
import numpy as np




parser = argparse.ArgumentParser(description='Train LM')
parser.add_argument('--monolithic', action='store_true')
parser.add_argument('--type', type=str, default='sparse',help='one of sparse, dense, ZS, FS')
parser.add_argument('--sparse_type', type=str, default='BM25',help='one of BM25 TF-IDF or OWC')
parser.add_argument('--LM', type=str, default='gpt2')
parser.add_argument('--agg_func', type=str, default='min')
parser.add_argument('--fold_number', type=int, default=0) # -1 for all folds




agg_fcns = {"min":min, "max":max, "amean":np.mean, "gmean":custom_gmean}


LM_names = {'gpt2':'gpt2',
'opt':'facebook/opt-1.3b',
'bert':"bert-base-uncased",
'tas-b':'sebastian-hofstaetter/distilbert-dot-tas_b-b256-msmarco'}


def run_experiment():
    config = load_config('./config.json')
    train_splits, val_splits, test_splits = load_data(config)
    args = parser.parse_args()

    exp_config = {'fold_number':args.fold_number,
                'agg_func':args.agg_func,
                'LM':args.LM,
                'type':args.type,
                'sparse_type':args.sparse_type,
                'monolithic':args.monolithic,}

    train_data = train_splits[exp_config['fold_number']]
    val_data = val_splits[exp_config['fold_number']]
    test_data = test_splits[exp_config['fold_number']]


    if exp_config['monolithic']:
        if exp_config['type'] == 'sparse':
            st = sparse_types[exp_config['sparse_type']]
            predictions = sparse_pred(test_data,st)
        elif exp_config['type'] == 'dense':
            predictions = dense_pred(test_data,LM_names[exp_config['LM']])
        elif exp_config['type'] == 'ZS':
            predictions = ZS_pred(test_data,LM_names[exp_config['LM']])
        elif exp_config['type'] == 'FS':
            predictions = FS_pred(train_data,test_data,LM_names[exp_config['LM']])

    else: # aspect
        agg  =agg_fcns[exp_config['agg_func']]
        if exp_config['type'] == 'sparse':
            st = aspect_sparse_types[exp_config['sparse_type']]
            predictions = aspect_sparse_pred(test_data,sparse_method=st,agg_fcn=agg)
        elif exp_config['type'] == 'dense':
            predictions = aspect_dense_pred(test_data,LM_names[exp_config['LM']],agg_fcn=agg)
        elif exp_config['type'] == 'ZS':
            predictions = aspect_ZS_pred(test_data,LM_names[exp_config['LM']],agg_fcn=agg)
        elif exp_config['type'] == 'FS':
            predictions = aspect_FS_pred(train_data,test_data,LM_names[exp_config['LM']],agg_fcn=agg)

    EXP_NAME = "_".join([str(exp_config['monolithic']),str(exp_config['type']),str(exp_config['agg_func']),str(exp_config['LM']),str(exp_config['sparse_type'])])
    # ,
    result_root = './results'
    if not os.path.exists(result_root):
        os.mkdir(result_root)
    exp_dir = os.path.join(result_root,EXP_NAME)
    if not os.path.exists(exp_dir):
        os.mkdir(exp_dir)
    
    evals_folder = os.path.join(exp_dir,'evals')
    if not os.path.exists(evals_folder):
        os.mkdir(evals_folder)
    output_path = os.path.join(evals_folder, str(exp_config['fold_number']) + '_' + EXP_NAME + '.csv')
    evaluate(test_data,predictions, output_filename=output_path)


    configs_folder = os.path.join(exp_dir,'configs')
    if not os.path.exists(configs_folder):
        os.mkdir(configs_folder)


    config_pd =pd.DataFrame.from_dict(exp_config, orient="index")
    output_path = os.path.join(configs_folder, 'config_'+ str(exp_config['fold_number']) + '_' + EXP_NAME + '.csv')
    config_pd.to_csv(output_path)

run_experiment()




    
    