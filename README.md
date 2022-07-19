# Introduction

This repository is for the LGE FoodKG dataset and tools. It contains a custom recipe query dataset curated from [FoodKG](https://foodkg.github.io/), a dataset search tool, baseline methods, and evaluation tools.

# Dataset

## Data Format

The format of the dataset is in JSON, where each JSON object consists of the query, query type labels, 5 options (recipe IDs and text descriptions), as well as the recipe ID of the intended correct answer. The JSON schema used can be found under data/.

One example of the data:

```json
{
  "query": "I would like meat lasagna but I'm watching my weight",
  "query_type:": {
    "General": 0,
    "Specific": 1,
    "Objective": 1,
    "Subjective": 0,
    "Indirect": 1,
    "Direct": 0,
    "Simple": 1,
    "Compound": 0,
    "Negated": 0,
    "Analogical": 0,
    "Temporal": 0
  },
  "options": { 
      "34572cc1ee": "Vegetarian lasagna with mushrooms, mixed vegetables, textured vegetable protein, and meat replacement",
      "7042fffd85": "Forgot the Meat Lasagna with onions, mushroom and spinach",
      "0b82f37488": "Beef lasagna with whole wheat noodles, low-fat cottage cheese, and part-skim mozzarella cheese",
      "047ea4e60b": "Cheesy lasagna with Italian sausage, mushrooms, and 8 types of cheese",
      "57139f1a42": "Meat loaf containing vegetables such as potatoes, onions, corn, carrots, and cabbage"
  },
  "answer": "0b82f37488"
}
```

## Data Curation Methodology

### FoodKG Search Tool

A python-based search tool was developed to easily search through recipes in the FoodKG dataset when generating options for each query. It searched through the dataset using text matching to the recipe names and had the option to include/exclude certain ingredients. It returns a display of the recipe ID, recipe name, ingredients, and nutritional information for up to 50 recipes. See README under tools/foodkg-search-tool for more information on setup and usage.

### Query Generation

- [query categorization and examples]
- [query guidelines]

### Query Type Annotation

Each query is labeled according to the query types below, for a total of 11 binary labels where 1/0 indicates true/false.

- General vs. Specific

- Objective vs. Subjective

- Indirect vs. Direct (common sense involved)

- Simple vs. Compound (AND/OR) Logic

- Negation

- Analogical

- Temporal

Examples of queries and their corresponding labels:

### Option Generation

- [query guidelines]

### Data Validation

- [validation methodlogy]

# Baseline Methods

A number of different evaluation methods were chosen and run on the data to serve as baseline results. These results also helped standardize the difficulty of queries across different individuals. The code for these baselines can be found under baselines/.

## 1) Overlapping Word Count
- [brief description]
- [results - per person and in aggregate]

## 2) TF-IDF Ranking

## 3) Word Embedding (Glove)

## 4) Neural IR (BERT, TAS-B)

# Evaluation Metrics

- ## H@k, k < 5

- ## MRR