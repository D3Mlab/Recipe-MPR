import pandas as pd
import tiktoken

from openai.embeddings_utils import get_embedding
import openai
import json 
import time
from tqdm import tqdm


openai.api_key = 'YOUR_API_KEY'

with open('/content/500QA.json') as f:
  all_data = json.load(f)


N = len(all_data)
print(N)
for i in tqdm(range(N)):
  if (i+1)%10==0:
    time.sleep(60)
  data = all_data[i]
  # print(data['query'])
  if data['query'] not in embeddings.keys():
    embeddings[data['query']] = get_embedding(data['query'], model=embedding_model)
  for option in data['options'].values():
    # print(option)
    if option not in embeddings.keys():
      embeddings[option] = get_embedding(option, model=embedding_model)

  for aspect in data['correctness_explanation'].keys():
    # print(option)
    if aspect not in embeddings.keys():
      embeddings[aspect] = get_embedding(aspect, model=embedding_model)


with open('embeddings_with_aspects.json', 'w') as fp:
    json.dump(embeddings, fp)