import os
import openai

openai.api_key = os.getenv("OPEN_API_KEY")

# Fine tune the model - https://betterprogramming.pub/fine-tune-gpt3-for-quality-results-3f91f1ab44ea
response = openai.FineTune.create(training_file="file-C7KVh700iW5BZ9Ni3XzPqnzd", model='davinchi')
print(response)

# Check status
status = openai.FineTune.retrieve(id='ft-dvu6JzYaVbuglqPUXrhjoZ8z')
print(status)