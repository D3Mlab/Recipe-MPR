
import pandas as pd

def evaluate(data_split, predictions):
    type_correct = {
            "Specific": 0,
            # "Subjective": 0,
            "Commonsense": 0,
            # "Compound": 0,
            "Negated": 0,
            "Analogical": 0,
            "Temporal": 0}
    type_count = {
            "Specific": 0,
            # "Subjective": 0,
            "Commonsense": 0,
            # "Compound": 0,
            "Negated": 0,
            "Analogical": 0,
            "Temporal": 0}
    total = 0
    correct = 0
    for i,data in enumerate(data_split):
        total+=1
        answer = data['options'][data['answer']]
        value_to_add_to_correct = 0
        if answer == predictions[i]:
            correct+=1
            value_to_add_to_correct = 1
        # print(data)
        for t in type_count.keys():
            if data['query_type'][t]==1:
                type_correct[t]+=value_to_add_to_correct
                type_count[t]+=1
    results = {}
    for t in type_count.keys():
        results[t] = type_correct[t]*100/type_count[t]
    results['acc'] = correct*100/total
    df = pd.DataFrame.from_dict(results, orient="index")
    print(df)
    # df.to_csv(output_filename)
    return df