# foodkg-search-tool
A tool to search recipes in foodkg and display its data by specific search. 

# How to set up the tool:
Notes: The following steps assume you already have python installed.
If you are using Windows, you may have to download Make. [Here's a guide.](https://www.technewstoday.com/install-and-use-make-in-windows/)

1. Clone this repository
2. Download a folder called <code>Layers</code> from the Recipe1m database [here](http://im2recipe.csail.mit.edu/dataset/download/). Find </code>layer1.json</code> and move it into <code>/resources</code>.
3. In the <code>/src</code> directory, run <code>make setup</code>. This will take a long time.

# How to run the tool:
In the <code>/src</code> directory, run <code>make</code>.

# How to use the tool:
- <b>Searching multiple ingredients</b>
<p>For a recipe that uses sugar, eggs and flour, search: <b>sugar eggs flour</b></p>

- <b>Searching phrases</b>
<p>For a recipe that uses vanilla extract and baking soda, search: <b>"vanilla extract" "baking soda"</b></p>
