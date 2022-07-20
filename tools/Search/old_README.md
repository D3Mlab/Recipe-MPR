# foodkg-search-tool
A tool to search recipes in foodkg and display its data by specific search. 

# How to set up the tool:
Note: The following steps assume you already have python and pip installed.

## 1. Clone this repository

## 2. Download the required Python libraries, Whoosh and PyQt5

### Mac/Linux Users:
- (optional but suggested) Create and activate a python virtual environment by running the following in the command line <pre><code>python3 -m venv venv</code></pre> <pre><code>source venv/bin/activate</code></pre> make sure to run the second line in the same directory every time you want to run the program.
- install Whoosh by running <pre><code>pip install Whoosh</code></pre>
- install PyQt5 by running <pre><code>pip install PyQt5</code></pre>

### Windows Users:
- (optional but suggested) Create and activate a python virtual environment by running the following in the command line<pre><code>python -m venv venv</code></pre> <pre><code>venv\Scripts\Activate.ps1</code></pre> in the command line. make sure to run the second line in the same directory every time you want to run the program. 
- install Whoosh by running <pre><code>pip install Whoosh</code></pre>
- install PyQt5 by running <pre><code>pip install PyQt5</code></pre>

## 3. Load the recipe data into an index
- Run <code>load_index.py</code>. This would take a long time. 
<pre><code>python3 path_to_cloned_repository/src/load_index.py</code></pre>


# How to run the tool:
- Run <code>main.py</code>. 
<pre><code>python3 path_to_cloned_repository/src/main.py</code></pre> in the command line or run 


# How to use the tool:
- <b>Searching multiple ingredients</b>
<p>For a recipe that uses sugar, eggs and flour, search: <b>sugar eggs flour</b></p>

- <b>Searching phrases</b>
<p>For a recipe that uses vanilla extract and baking soda, search: <b>"vanilla extract" "baking soda"</b></p>