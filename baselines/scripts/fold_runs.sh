python run_exp.py --monolithic --type sparse --fold_number -1 --sparse_type OWC --result_root option2_runs --folds_path folds/20_fold_inds.json --folds_path folds/20_fold_inds.json
python run_exp.py --monolithic --type sparse --fold_number -1 --sparse_type BM25  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py --monolithic --type sparse --fold_number -1 --sparse_type TFIDF  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py --monolithic --type dense --fold_number -1  --LM tas-b  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py --monolithic --type dense --fold_number -1  --LM bert  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py --monolithic --type ZS --fold_number -1  --LM gpt2  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py --monolithic --type ZS --fold_number -1  --LM opt  --result_root option2_runs --folds_path folds/20_fold_inds.json

python run_exp.py --monolithic --type FS --fold_number -1  --LM gpt2  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py --monolithic --type FS --fold_number -1  --LM opt  --result_root option2_runs --folds_path folds/20_fold_inds.json

python run_exp.py  --type sparse --fold_number -1 --sparse_type OWC --agg_func min  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type sparse --fold_number -1 --sparse_type BM25 --agg_func min  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type sparse --fold_number -1 --sparse_type TFIDF --agg_func min  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type dense --fold_number -1  --LM bert --agg_func min  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type dense --fold_number -1  --LM tas-b --agg_func min  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type ZS --fold_number -1  --LM gpt2 --agg_func min  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type FS --fold_number -1  --LM gpt2 --agg_func min  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type ZS --fold_number -1  --LM opt --agg_func min  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type FS --fold_number -1  --LM opt --agg_func min  --result_root option2_runs --folds_path folds/20_fold_inds.json



python run_exp.py  --type sparse --fold_number -1 --sparse_type OWC --agg_func max  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type sparse --fold_number -1 --sparse_type BM25 --agg_func max  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type sparse --fold_number -1 --sparse_type TFIDF --agg_func max  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type dense --fold_number -1  --LM bert --agg_func max  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type dense --fold_number -1  --LM tas-b --agg_func max  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type ZS --fold_number -1  --LM gpt2 --agg_func max  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type FS --fold_number -1  --LM gpt2 --agg_func max  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type ZS --fold_number -1  --LM opt --agg_func max  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type FS --fold_number -1  --LM opt --agg_func max  --result_root option2_runs --folds_path folds/20_fold_inds.json



python run_exp.py  --type sparse --fold_number -1 --sparse_type OWC --agg_func amean  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type sparse --fold_number -1 --sparse_type BM25 --agg_func amean  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type sparse --fold_number -1 --sparse_type TFIDF --agg_func amean  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type dense --fold_number -1  --LM bert --agg_func amean  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type dense --fold_number -1  --LM tas-b --agg_func amean  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type ZS --fold_number -1  --LM gpt2 --agg_func amean  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type FS --fold_number -1  --LM gpt2 --agg_func amean  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type ZS --fold_number -1  --LM opt --agg_func amean  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type FS --fold_number -1  --LM opt --agg_func amean  --result_root option2_runs --folds_path folds/20_fold_inds.json



python run_exp.py  --type sparse --fold_number -1 --sparse_type OWC --agg_func gmean  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type sparse --fold_number -1 --sparse_type BM25 --agg_func gmean  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type sparse --fold_number -1 --sparse_type TFIDF --agg_func gmean  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type dense --fold_number -1  --LM bert --agg_func gmean  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type dense --fold_number -1  --LM tas-b --agg_func gmean  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type ZS --fold_number -1  --LM gpt2 --agg_func gmean  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type FS --fold_number -1  --LM gpt2 --agg_func gmean  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type ZS --fold_number -1  --LM opt --agg_func gmean  --result_root option2_runs --folds_path folds/20_fold_inds.json
python run_exp.py  --type FS --fold_number -1  --LM opt --agg_func gmean  --result_root option2_runs --folds_path folds/20_fold_inds.json