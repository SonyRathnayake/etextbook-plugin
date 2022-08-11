import os
import openai

#response = openai.Completion.create(model="text-davinci-002", prompt="Say this is a test", temperature=0, max_tokens=6)

def gpt3(phrase):
    openai.api_key = os.getenv("OPEN_API_KEY")
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=phrase,
        temperature=0, max_tokens=20, top_p=1, frequency_penalty=0, presence_penalty=0
    )
    content = response.choices[0].text.split('.')
    print(content)
    return response.choices[0].text

query = "What is global warming?"
response = gpt3(query)
print(response)