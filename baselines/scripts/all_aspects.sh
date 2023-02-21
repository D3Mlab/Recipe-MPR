python run_exp.py --monolithic --type sparse --fold_number -1 --sparse_type OWC --result_root all_aspects_concate --folds_path folds/5_fold_inds.json
python run_exp.py --monolithic --type sparse --fold_number -1 --sparse_type BM25  --result_root all_aspects_concate --folds_path folds/5_fold_inds.json
python run_exp.py --monolithic --type sparse --fold_number -1 --sparse_type TFIDF  --result_root all_aspects_concate --folds_path folds/5_fold_inds.json
python run_exp.py --monolithic --type dense --fold_number -1  --LM tas-b  --result_root all_aspects_concate --folds_path folds/5_fold_inds.json
python run_exp.py --monolithic --type dense --fold_number -1  --LM bert  --result_root all_aspects_concate --folds_path folds/5_fold_inds.json
python run_exp.py --monolithic --type ZS --fold_number -1  --LM gpt2  --result_root all_aspects_concate --folds_path folds/5_fold_inds.json
python run_exp.py --monolithic --type ZS --fold_number -1  --LM opt  --result_root all_aspects_concate --folds_path folds/5_fold_inds.json

python run_exp.py --monolithic --type FS --fold_number -1  --LM gpt2  --result_root all_aspects_concate --folds_path folds/5_fold_inds.json
python run_exp.py --monolithic --type FS --fold_number -1  --LM opt  --result_root all_aspects_concate --folds_path folds/5_fold_inds.json