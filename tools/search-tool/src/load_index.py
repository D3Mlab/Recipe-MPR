import pickle
import sys
import os.path
import os

from whoosh import index, query
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer

schema = Schema(
    name=TEXT(stored=True, analyzer=StemmingAnalyzer()),
    id=ID(stored=True),
    ingredients=TEXT(stored=True, analyzer=StemmingAnalyzer()),
    nutri_info=TEXT(stored=True)
)


class Recipe:
    # recipe name (from layer1)
    name = "no name"
    # list of ingredient objects (from det_igrs)
    ingredients = ""

    # dictionary for fsa lights (from recipes with nutritional info)
    fsa_lights_per100g = {
        "fat": "no data",
        "salt": "no data",
        "saturates": "no data",
        "sugars": "no data"
    }
    # dictionary for nutritional values (from recipes with nutritional info)
    nutr_values_per100g = {
        "energy": "no data",
        "fat": "no data",
        "protein": "no data",
        "salt": "no data",
        "saturates": "no data",
        "sugars": "no data"
    }


# create an index object
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = index.create_in("indexdir", schema)
writer = ix.writer()

paths = ["../resources/database1.txt",
         "../resources/database2.txt", "../resources/database3.txt"]

for i in range(0, 3):
    database_file = open(paths[i], "rb")
    print("loading database " + str(i) + " ...")
    database = pickle.load(database_file)
    database_file.close()

    print("adding to index...")
    for key in database:
        writer.add_document(name=database[key].name, id=key, ingredients=database[key].ingredients,
                            nutri_info=str(database[key].nutr_values_per100g))
        print("id:" + key)
        print("name:" + database[key].name)
        print("ingredients:" + database[key].ingredients)
        print("nutritional info:" + str(database[key].nutr_values_per100g))


print("Saving data to index ...")
writer.commit()
print("Done!")
