import os
import openai

openai.api_key = os.getenv("OPEN_API_KEY")

# Fine tune the model - https://betterprogramming.pub/fine-tune-gpt3-for-quality-results-3f91f1ab44ea
response = openai.FineTune.create(training_file="file-ug8bQn6RqtPTWPc3ZRCF2Oyt", model='ada')
print(response)

# Check status
status = openai.FineTune.retrieve(id='ft-dvu6JzYaVbuglqPUXrhjoZ8z')
print(status)