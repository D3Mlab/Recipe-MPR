'''
Imports
'''
from encodings import utf_8
from pickletools import unicodestring8
import sys

import json
import pickle

from whoosh import index, query
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer
import os.path
import os
from whoosh import qparser
from whoosh.qparser import QueryParser, OrGroup
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem

'''
Globals
'''
name_query = ""
ingr_query = ""
ingr_exclude_query = ""

Hitted_ids = list()
Hitted_recipe_names = list()
Hitted_ingredients = list()
Hitted_nutri = list()


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


'''
Functions
'''


def Store_Matches(results):
    global Hitted_ids
    global Hitted_recipe_names
    global Hitted_ingredients
    global Hitted_nutri

    # Refresh
    Hitted_ids = list()
    Hitted_recipe_names = list()
    Hitted_ingredients = list()
    Hitted_nutri = list()

    print(results)
    # Store the results
    for hit in results:
        Hitted_ids.append(hit['id'])
        Hitted_recipe_names.append(hit["name"])
        Hitted_ingredients.append(hit["ingredients"])
        Hitted_nutri.append(hit["nutri_info"])


def getTableModel(Hitted_recipe_id, Hitted_recipe_names, Hitted_ingredients, Hitted_nutri):
    model = QStandardItemModel(len(Hitted_recipe_names), 5)

    id_name = list(zip(Hitted_recipe_id, Hitted_recipe_names))

    for row, id in enumerate(id_name):
        item = QStandardItem(str(id[0]) + ": " + id[1])
        model.setItem(row, 0, item)

    for row, id in enumerate(Hitted_recipe_id):
        item = QStandardItem(id)
        model.setItem(row, 1, item)

    for row, name in enumerate(Hitted_recipe_names):
        item = QStandardItem(name)
        model.setItem(row, 2, item)

    for row, ingr in enumerate(Hitted_ingredients):
        item = QStandardItem(ingr)
        model.setItem(row, 3, item)

    for row, nutri in enumerate(Hitted_nutri):
        item = QStandardItem(str(nutri))
        model.setItem(row, 4, item)

    model.setHorizontalHeaderLabels(
        ['ID+Name', 'ID', 'Recipe Name', 'Ingredients', 'Nutritional Information'])

    return model


def actOnNameType():
    global name_query
    global nameSearchField
    global recipeList

    name_query = nameSearchField.text()
    print("name search input is: " + name_query)
    actOnState()
    model = getTableModel(Hitted_ids, Hitted_recipe_names,
                          Hitted_ingredients, Hitted_nutri)
    recipeList.setModel(model)
    recipeList.resizeColumnsToContents()


def actOnIngrType():
    global ingrSearchField
    global ingr_query
    global recipeList

    ingr_query = ingrSearchField.text()
    print("ingr include input is: " + ingr_query)
    actOnState()
    model = getTableModel(Hitted_ids, Hitted_recipe_names,
                          Hitted_ingredients, Hitted_nutri)
    recipeList.setModel(model)
    recipeList.resizeColumnsToContents()


def actOnExcludeIngrType():
    global ingrExcludeSearchField
    global ingr_exclude_query
    global recipeList

    ingr_exclude_query = ingrExcludeSearchField.text()
    print("ingr exclude input is: " + ingr_exclude_query)
    actOnState()
    model = getTableModel(Hitted_ids, Hitted_recipe_names,
                          Hitted_ingredients, Hitted_nutri)
    recipeList.setModel(model)
    recipeList.resizeColumnsToContents()


def actOnState():
    global name_query
    global ingr_query
    global ingr_exclude_query

    qp = QueryParser("name", schema=ix.schema)
    q = qp.parse(name_query)

    qp_ingr = QueryParser("ingredients", schema=ix.schema)
    q_ingr = qp_ingr.parse(ingr_query)

    qp_excl = qparser.QueryParser(
        "ingredients", schema=ix.schema, group=qparser.OrGroup)
    np = qparser.OperatorsPlugin(Not='NOT')
    qp_excl.replace_plugin(np)
    q_excl = qp_excl.parse("NOT("+ingr_exclude_query+")")

    with ix.searcher() as searcher:
        results = searcher.search((q & q_ingr & q_excl), limit=50)
        Store_Matches(results)


def createNameSearchBar():
    global nameSearchField
    layout.addWidget(QLabel("name search: "), 0, 0)
    nameSearchField.editingFinished.connect(actOnNameType)
    layout.addWidget(nameSearchField, 0, 1, 1, 3)


def createIngredientSearchBar():
    global ingrSearchField
    layout.addWidget(QLabel("include ingredients: "), 1, 0)
    ingrSearchField.editingFinished.connect(actOnIngrType)
    layout.addWidget(ingrSearchField, 1, 1, 1, 3)


def createIngredientExcludeSearchBar():
    global ingrExcludeSearchField
    layout.addWidget(QLabel("exclude ingredients: "), 2, 0)
    ingrExcludeSearchField.editingFinished.connect(actOnExcludeIngrType)
    layout.addWidget(ingrExcludeSearchField, 2, 1, 1, 3)


def createCheckBoxes():
    fatCheckBox = QCheckBox('Low fat')
    layout.addWidget(fatCheckBox, 2, 0, 1, 1)
    saltCheckBox = QCheckBox('Low salt')
    layout.addWidget(saltCheckBox, 2, 1, 1, 1)
    saturatesCheckBox = QCheckBox('Low saturates')
    layout.addWidget(saturatesCheckBox, 2, 2, 1, 1)
    sugarCheckBox = QCheckBox('Low sugar')
    layout.addWidget(sugarCheckBox, 2, 3, 1, 1)


def createTable():
    # recipeList.verticalHeader().setVisible(False)
    model = getTableModel(Hitted_ids, Hitted_recipe_names,
                          Hitted_ingredients, Hitted_nutri)
    recipeList.setModel(model)
    recipeList.resizeColumnsToContents()
    layout.addWidget(recipeList, 3, 0, 1, 4)


'''
Main program
'''

''' set up search '''
schema = Schema(
    name=TEXT(stored=True, analyzer=StemmingAnalyzer()),
    id=ID(stored=True),
    ingredients=TEXT(stored=True, analyzer=StemmingAnalyzer()),
    nutri_info=TEXT(stored=True)
)

# # create an index object
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
ix = index.open_dir("indexdir")

''' set up GUI '''
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Foodkg Search Tool')
window.setGeometry(400, 250, 800, 300)
layout = QGridLayout()

nameSearchField = QLineEdit()
ingrSearchField = QLineEdit()
ingrExcludeSearchField = QLineEdit()
recipeList = QTableView()

createNameSearchBar()
createIngredientSearchBar()
createIngredientExcludeSearchBar()
# createCheckBoxes()
createTable()

# send to GUI and exit
window.setLayout(layout)
window.show()

numdocs = ix.searcher().doc_count_all()
print("numdocs:" + str(numdocs))

sys.exit(app.exec_())
