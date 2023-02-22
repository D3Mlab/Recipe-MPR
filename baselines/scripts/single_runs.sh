python run_exp.py --monolithic --type sparse --fold_number 0 --sparse_type OWC --result_root 1fold_runs --folds_path folds/1_fold_inds.json --folds_path folds/1_fold_inds.json
python run_exp.py --monolithic --type sparse --fold_number 0 --sparse_type BM25  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py --monolithic --type sparse --fold_number 0 --sparse_type TFIDF  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py --monolithic --type dense --fold_number 0  --LM tas-b  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py --monolithic --type dense --fold_number 0  --LM bert  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py --monolithic --type ZS --fold_number 0  --LM gpt2  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py --monolithic --type ZS --fold_number 0  --LM opt  --result_root 1fold_runs --folds_path folds/1_fold_inds.json

python run_exp.py --monolithic --type FS --fold_number 0  --LM gpt2  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py --monolithic --type FS --fold_number 0  --LM opt  --result_root 1fold_runs --folds_path folds/1_fold_inds.json

python run_exp.py  --type sparse --fold_number 0 --sparse_type OWC --agg_func min  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type sparse --fold_number 0 --sparse_type BM25 --agg_func min  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type sparse --fold_number 0 --sparse_type TFIDF --agg_func min  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type dense --fold_number 0  --LM bert --agg_func min  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type dense --fold_number 0  --LM tas-b --agg_func min  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type ZS --fold_number 0  --LM gpt2 --agg_func min  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type FS --fold_number 0  --LM gpt2 --agg_func min  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type ZS --fold_number 0  --LM opt --agg_func min  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type FS --fold_number 0  --LM opt --agg_func min  --result_root 1fold_runs --folds_path folds/1_fold_inds.json



python run_exp.py  --type sparse --fold_number 0 --sparse_type OWC --agg_func max  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type sparse --fold_number 0 --sparse_type BM25 --agg_func max  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type sparse --fold_number 0 --sparse_type TFIDF --agg_func max  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type dense --fold_number 0  --LM bert --agg_func max  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type dense --fold_number 0  --LM tas-b --agg_func max  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type ZS --fold_number 0  --LM gpt2 --agg_func max  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type FS --fold_number 0  --LM gpt2 --agg_func max  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type ZS --fold_number 0  --LM opt --agg_func max  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type FS --fold_number 0  --LM opt --agg_func max  --result_root 1fold_runs --folds_path folds/1_fold_inds.json



python run_exp.py  --type sparse --fold_number 0 --sparse_type OWC --agg_func amean  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type sparse --fold_number 0 --sparse_type BM25 --agg_func amean  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type sparse --fold_number 0 --sparse_type TFIDF --agg_func amean  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type dense --fold_number 0  --LM bert --agg_func amean  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type dense --fold_number 0  --LM tas-b --agg_func amean  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type ZS --fold_number 0  --LM gpt2 --agg_func amean  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type FS --fold_number 0  --LM gpt2 --agg_func amean  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type ZS --fold_number 0  --LM opt --agg_func amean  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type FS --fold_number 0  --LM opt --agg_func amean  --result_root 1fold_runs --folds_path folds/1_fold_inds.json



python run_exp.py  --type sparse --fold_number 0 --sparse_type OWC --agg_func gmean  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type sparse --fold_number 0 --sparse_type BM25 --agg_func gmean  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type sparse --fold_number 0 --sparse_type TFIDF --agg_func gmean  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type dense --fold_number 0  --LM bert --agg_func gmean  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type dense --fold_number 0  --LM tas-b --agg_func gmean  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type ZS --fold_number 0  --LM gpt2 --agg_func gmean  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type FS --fold_number 0  --LM gpt2 --agg_func gmean  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type ZS --fold_number 0  --LM opt --agg_func gmean  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type FS --fold_number 0  --LM opt --agg_func gmean  --result_root 1fold_runs --folds_path folds/1_fold_inds.json






python run_exp.py --monolithic --type dense --fold_number 0  --LM agribert  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py --monolithic --type dense --fold_number 0  --LM dfood  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py --monolithic --type dense --fold_number 0  --LM foodNER  --result_root 1fold_runs --folds_path folds/1_fold_inds.json


python run_exp.py  --type dense --fold_number 0  --LM agribert --agg_func min  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type dense --fold_number 0  --LM dfood --agg_func min  --result_root 1fold_runs --folds_path folds/1_fold_inds.json
python run_exp.py  --type dense --fold_number 0  --LM foodNER --agg_func min  --result_root 1fold_runs --folds_path folds/1_fold_inds.json

