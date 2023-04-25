# Aspect-based Setting

In the aspect-based experiment setting, we sequentially provide one preference aspect (span of query text) at a time as an input to a model, after which we aggregate the output scores.

## Few-shot Prompt Format
The template used for the prompt examples given to GPT-2 and OPT was:

_input:_ \<sample aspect\>

_output:_ \<sample correct option description\>

Example:

```
input: meat lasagna
output: Beef lasagna with whole wheat noodles, low-fat cottage cheese, and part-skim mozzarella cheese
```

For GPT-3 text completion, a goal-setting instruction was prepended to the prompt given to the model: _"Given the preference aspect and five options, generate a list of scores for how well each option satisfies the query_". The prompt was then appended with a formatting instruction after the few-shot examples: 

*"Please answer in a format that looks like this:*

*Option 0 Score: _*  
*Option 1 Score: _*  
*Option 2 Score: _*  
*Option 3 Score: _*  
*Option 4 Score: _ "* 

The template used for the prompt examples was:

_Query:_ \<sample query\>

_Options:_ \<sample option list\>

_Option:_ \<sample correct option description\> 

The order that the options appeared in for each of the few-shot samples was randomized. All incorrect options were given a score of 0 and the correct option was given a score of 1.

Example:

```
Aspect: meat lasagna

Options:
0. Vegetarian lasagna with mushrooms, mixed vegetables, textured vegetable protein, and meat replacement",
1. Forgot the Meat Lasagna with onions, mushroom and spinach",
2. Beef lasagna with whole wheat noodles, low-fat cottage cheese, and part-skim mozzarella cheese",
3. Cheesy lasagna with Italian sausage, mushrooms, and 8 types of cheese",
4. Meat loaf containing vegetables such as potatoes, onions, corn, carrots, and cabbage

Option 0 Score: 0
Option 1 Score: 0
Option 2 Score: 1
Option 3 Score: 0
Option 4 Score: 0
```