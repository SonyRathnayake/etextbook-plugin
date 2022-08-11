import os
import openai
from googletrans import Translator


# Translator
def google_translator(phrase, destination):
    translator = Translator()
    translation = translator.translate(phrase, dest=destination)
    return translation.text


def gpt3(phrase):
    openai.api_key = os.getenv("OPEN_API_KEY")
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=phrase,
        temperature=0, max_tokens=10, top_p=1, frequency_penalty=0, presence_penalty=0
    )
    content = response.choices[0].text.split('.')
    print(content)
    return response.choices[0].text


query = input("Input text to Summarize >")
query = google_translator(query, 'en')
print(query)
response = gpt3("Summarize " + query)
response = google_translator(response, 'si')
print(response)

# Sample input - තෝරාගත් මාතෘකාවට අදාළව රචනය ලිවීමට පෙර එකී මාතෘකාව පිළිබඳ ස්ථිර  සැලැස්මක් ගොඩ නගා ගත යුතුය.
