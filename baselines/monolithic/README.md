# Monolithic Setting

In the monolithic experiment setting, the full query is given as an input, where all preference aspects are provided in the initial natural language context.

## Few-shot Prompt Format
The template used for the prompt examples given to GPT-2 and OPT was:

_input:_ \<sample query\>

_output:_ \<sample correct option description\>

Example:

```
input: I would like meat lasagna but I'm watching my weight
output: Beef lasagna with whole wheat noodles, low-fat cottage cheese, and part-skim mozzarella cheese
```

For GPT-3 text completion, the goal-setting instruction given to the model was: _"Given the recipe query and five options, choose the option that best satisfies the query_", which was prepended to the input prompt. The template used for prompt examples was:

_Query:_ \<sample query\>

_Options:_ \<sample option list\>

_Option:_ \<sample correct option description\> 

The order that the options appeared in for each of the few-shot samples was randomized.

Example:

```
Query: I would like meat lasagna but I'm watching my weight

Options:
0. Vegetarian lasagna with mushrooms, mixed vegetables, textured vegetable protein, and meat replacement",
1. Forgot the Meat Lasagna with onions, mushroom and spinach",
2. Beef lasagna with whole wheat noodles, low-fat cottage cheese, and part-skim mozzarella cheese",
3. Cheesy lasagna with Italian sausage, mushrooms, and 8 types of cheese",
4. Meat loaf containing vegetables such as potatoes, onions, corn, carrots, and cabbage

Option: Beef lasagna with whole wheat noodles, low-fat cottage cheese, and part-skim mozzarella cheese
```