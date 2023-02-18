import json
import pandas as pd
import numpy as np
import os
import glob
import scipy
from scipy import stats

def mean_confidence_interval(data, confidence=0.90):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n - 1)
    return m,h

def gather_experiment_results(number_of_folds, experiments_path):

    list_of_experiments = os.listdir(experiments_path)
    types = ['Specific', 'Subjective', 'Commonsense', 'Compound', 'Negated', 'Analogical', 'Temporal', 'acc']
    experiments_results_aggregated = {}
    for experiment in list_of_experiments :
        if experiment != '.DS_Store':
            config_address = experiments_path+'/'+experiment+'/configs/'+ os.listdir(experiments_path+'/'+experiment+'/configs/')[0]
            config = pd.read_csv(config_address).T.values
        directory_path = experiments_path+'/'+experiment+"/evals" + "/**/*.csv"
        csv_file_pathes = [ csv_path for csv_path in glob.glob(directory_path, recursive = True)]
        cross_fold_numbers = [str(i) for i in range(number_of_folds)]
        csv_file_pathes_k_fold = [path for path in csv_file_pathes if path.split('/')[-1].split('_')[0] in cross_fold_numbers]
        results_per_config = {key:[] for key in types}
        for file_path in csv_file_pathes_k_fold: 
            for type in pd.read_csv(file_path).values.tolist():
                results_per_config[type[0]].append(type[1])
        experiments_results_aggregated[tuple(tuple(row) for row in config)] = results_per_config
    return experiments_results_aggregated

def make_df_all_results(experiments_results_aggregated,saving_path):
    final_columns = ['fold_number',
   'agg_func',
   'LM',
   'type',
   'sparse_type',
   'monolithic',
   'seed',
   'result_root'
   ]
    res = ['Specific', 'Subjective', 'Commonsense', 'Compound', 'Negated', 'Analogical', 'Temporal', 'acc']
    res_ci = [res_type+'_ci' for res_type in res]
    final_columns= final_columns+ res + res_ci
    final_result_df = {column:[] for column in final_columns}
    for key in experiments_results_aggregated:
        res = experiments_results_aggregated[key]
        for i in range(len(key[0])):
            final_result_df[key[0][i]].append(key[1][i])
        for res_metric in res:
            m , ci = mean_confidence_interval(res[res_metric])
            final_result_df[res_metric].append(m)
            final_result_df[res_metric+'_ci'].append(ci)
    final_result_df = pd.DataFrame.from_dict(final_result_df)
    final_result_df = final_result_df.drop(columns='fold_number')
    final_result_df.to_csv(saving_path)
    return final_result_df

def generate_csv_for_results(number_of_folds, experiments_path,saving_path='final_results.csv'):

    experiments_results_aggregated = gather_experiment_results(number_of_folds, experiments_path)
    df = make_df_all_results(experiments_results_aggregated,saving_path)
    return df

