python run_exp.py --monolithic --type dense --fold_number -1  --LM gpt3-ada --result_root gpt3_run --FS_num 5 --folds_path folds/5_fold_inds.json


python run_exp.py  --type dense --fold_number -1  --LM gpt3-ada --result_root gpt3_run --agg_func min --FS_num 5 --folds_path folds/5_fold_inds.json
python run_exp.py  --type dense --fold_number -1  --LM gpt3-ada --result_root gpt3_run --agg_func max --FS_num 5 --folds_path folds/5_fold_inds.json
python run_exp.py  --type dense --fold_number -1  --LM gpt3-ada --result_root gpt3_run --agg_func amean --FS_num 5 --folds_path folds/5_fold_inds.json
python run_exp.py  --type dense --fold_number -1  --LM gpt3-ada --result_root gpt3_run --agg_func gmean --FS_num 5 --folds_path folds/5_fold_inds.json



python run_exp.py --monolithic --type dense --fold_number 0  --LM gpt3-ada --result_root gpt3_run_single --agg_func min --FS_num 5 --folds_path folds/1_fold_inds.json

python run_exp.py  --type dense --fold_number 0  --LM gpt3-ada --result_root gpt3_run_single --agg_func min --FS_num 5 --folds_path folds/1_fold_inds.json
python run_exp.py  --type dense --fold_number 0  --LM gpt3-ada --result_root gpt3_run_single --agg_func max --FS_num 5 --folds_path folds/1_fold_inds.json
python run_exp.py  --type dense --fold_number 0  --LM gpt3-ada --result_root gpt3_run_single --agg_func amean --FS_num 5 --folds_path folds/1_fold_inds.json
python run_exp.py  --type dense --fold_number 0  --LM gpt3-ada --result_root gpt3_run_single --agg_func gmean --FS_num 5 --folds_path folds/1_fold_inds.json
