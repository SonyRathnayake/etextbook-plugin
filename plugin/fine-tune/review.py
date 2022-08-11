import os
import openai

openai.api_key = os.getenv("OPEN_API_KEY")

with open("../dataset/sentence.jsonl") as f:
  response = openai.File.create(file=f, purpose='fine-tune')
  print(response)