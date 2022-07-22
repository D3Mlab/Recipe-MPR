'''
Imports
'''
import json
import pickle

'''
Class
'''


class Recipe:
    # recipe name (from layer1)
    name = "no name"
    # string of comma separated ingredient objects (from det_igrs)
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


'''
Main function
'''
id_to_recipe = {}

''' parse through layer1 '''
x = open('../resources/layer1.json')
print("Loading recipe name and ids ...")
layer1 = json.load(x)

print("Adding recipe name and ids ...")

for i in range(0, len(layer1)):
    temp_recipe = Recipe()
    temp_recipe.name = layer1[i]["title"]
    id_to_recipe[layer1[i]["id"]] = temp_recipe

print("Done adding recipe name and ids")


''' parse through det_igrs'''
x = open('../resources/det_ingrs.json')
print("Loading ingredients data ...")
det_igrs = json.load(x)

print("Adding ingredients data ...")

for i in range(0, len(det_igrs)):

    if not det_igrs[i]["id"] in id_to_recipe:
        id_to_recipe[det_igrs[i]["id"]] = Recipe()

    ingredients_str = ""
    for j in range(0, len(det_igrs[i]["ingredients"])):
        ingredients_str += det_igrs[i]["ingredients"][j]["text"]
        ingredients_str += ","
    ingredients_str = ingredients_str[:-1]
    id_to_recipe[det_igrs[i]["id"]].ingredients = ingredients_str

print("Done adding ingredients data")

''' parse through nutritional info'''
x = open('../resources/recipes_with_nutritional_info.json')
print("Loading nutritional information ...")
nutri_info = json.load(x)

print("Adding nutritional information ...")

for i in range(0, len(nutri_info)):
    id_to_recipe[nutri_info[i]["id"]
                 ].fsa_lights_per100g = nutri_info[i]["fsa_lights_per100g"]
    id_to_recipe[nutri_info[i]["id"]
                 ].nutr_values_per100g = nutri_info[i]["nutr_values_per100g"]

print("Done adding nutritional information")


''' divide data into three text files '''
id_to_recipe2 = {}
id_to_recipe3 = {}

while len(id_to_recipe) > 680000:
    k, v = id_to_recipe.popitem()
    id_to_recipe3[k] = v

while len(id_to_recipe) > 340000:
    k, v = id_to_recipe.popitem()
    id_to_recipe2[k] = v


dbfile = open('../resources/database1.txt', 'wb')
pickle.dump(id_to_recipe, dbfile)
dbfile.close()

dbfile = open('../resources/database2.txt', 'wb')
pickle.dump(id_to_recipe2, dbfile)
dbfile.close()

dbfile = open('../resources/database3.txt', 'wb')
pickle.dump(id_to_recipe2, dbfile)
dbfile.close()

print("Generated text files")

print("calculating length of database1:")
print(len(id_to_recipe))

print("calculating length of database2:")
print(len(id_to_recipe2))

print("calculating length of database3:")
print(len(id_to_recipe3))

print("Done!")
