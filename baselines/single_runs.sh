# python run_exp.py --monolithic --type sparse --fold_number 0 --sparse_type OWC
# python run_exp.py --monolithic --type sparse --fold_number 0 --sparse_type BM25
# python run_exp.py --monolithic --type sparse --fold_number 0 --sparse_type TFIDF
# python run_exp.py --monolithic --type dense --fold_number 0  --LM tas-b
# python run_exp.py --monolithic --type ZS --fold_number 0  --LM gpt2


python run_exp.py --monolithic --type FS --fold_number 0  --LM gpt2


# python run_exp.py  --type sparse --fold_number 0 --sparse_type OWC --agg_func min
# python run_exp.py  --type sparse --fold_number 0 --sparse_type BM25 --agg_func min
# python run_exp.py  --type sparse --fold_number 0 --sparse_type TFIDF --agg_func max
# python run_exp.py  --type dense --fold_number 0  --LM bert --agg_func amean
# python run_exp.py  --type ZS --fold_number 0  --LM gpt2 --agg_func gmean

# python run_exp.py  --type FS --fold_number 0  --LM gpt2 --agg_func amean