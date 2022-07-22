# foodkg-search-tool
A tool to search recipes in foodkg and display its data by specific search. 

# How to set up the tool:
Notes: The following steps assume you already have python installed.
If you are using Windows, you may have to download Make. [Here's a guide.](https://www.technewstoday.com/install-and-use-make-in-windows/)

1. Clone this repository
2. Download the raw data
The recipe data we used in the research is gathered from the [Im2recipe project](http://im2recipe.csail.mit.edu/). 
It requires a simple registration to download the recipe data.
Please follow [this link](http://im2recipe.csail.mit.edu/dataset/register/) to register.

After the registration, download <code>Layers</code>, and <code>det_ingrs.json</code> and <code>recipes_with_nutritional_info.json</code> from the Recipe1m database [here](http://im2recipe.csail.mit.edu/dataset/download/). 

[Layer1.json](http://data.csail.mit.edu/im2recipe/recipe1M_layers.tar.gz) (Inside Layers): The basic descriptions of the recipes (Titles, url, id, etc.).

[det_ingrs.json](http://data.csail.mit.edu/im2recipe/det_ingrs.json): The ingredient information of each recipe in layer1.

[recipes_with_nutritional_info.json](http://data.csail.mit.edu/im2recipe/recipes_with_nutritional_info.json): The nutritional information of the recipes.

After downloading the data, find <code>layer1.json</code>, <code>det_ingrs.json</code> and <code>recipes_with_nutritional_info.json</code> and move it into <code>/resources</code>.

3. In the <code>/src</code> directory, run <code>make setup</code>. This will take a long time.
