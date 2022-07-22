.PHONY: setup

env = env/bin/activate
python = . $(env); LC_CTYPE=C.UTF-8 python

all: run

run: 
	$(python) main.py

setup: requirements.txt
	python3 -m pip install --user virtualenv
	python3 -m virtualenv -p python3 env
	$(python) -m pip install -r requirements.txt
	$(python) ../resources/json_to_dictionary.py
	$(python) load_index.py
