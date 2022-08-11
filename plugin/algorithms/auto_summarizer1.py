from googletrans import Translator
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


# nltk.download('stopwords')
# nltk.download('punkt')


# Translator
def google_translator(phrase, destination):
    translator = Translator()
    translation = translator.translate(phrase, dest=destination)
    return translation.text


# phrase = input("Input text to Summarize >")
# print(phrase)

sample_text =  """එය සරලව තබා ගැනීම සඳහා නිස්සාරණ සාරාංශයක් ජනනය කිරීමට බොහෝ ශිල්පීය ක්‍රම තිබේ,
වාක්‍ය සමානකම් සොයා ගැනීමට සහ ඒවා ශ්‍රේණිගත කිරීමට මම අධීක්ෂණය නොකළ ඉගෙනුම් ප්‍රවේශයක් භාවිතා කරමි.
සාරාංශ කිරීම යතුර සංරක්ෂණය කරමින් සංක්ෂිප්ත හා චතුර ලෙස සාරාංශයක් නිෂ්පාදනය කිරීමේ කාර්යයක් ලෙස අර්ථ දැක්විය හැක.
තොරතුරු සහ සමස්ත අර්ථය. මෙයින් එක් ප්‍රයෝජනයක් වනුයේ, ඔබට ආදර්ශයක් පුහුණු කිරීමට සහ ගොඩනැගීමට අවශ්‍ය නොවේ
ඔබගේ ව්යාපෘතිය සඳහා එය භාවිතා කිරීමට පෙර. හොඳම ප්‍රයෝජනය සඳහා කොසයින් සමානතාවය තේරුම් ගැනීම හොඳය
ඔබ බැලීමට යන කේතය. කොසයින් සමානතාව යනු ශුන්‍ය නොවන දෛශික දෙකක් අතර සමානකම් මැනීමකි
ඒවා අතර කෝණයේ කෝසයිනය මනින අභ්‍යන්තර නිෂ්පාදන අවකාශයක. එහි මිනුම් කොසයින් හි
දෛශික අතර කෝණය. වාක්‍ය සමාන නම් කෝණය e වනු ඇත"""

print("==== Original text in Sinhalese ====")
print(sample_text + '\n')
text = google_translator(sample_text, 'en')
print("==== Original text in English ====")
print(text + '\n')
# Tokenizing the text
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

# Creating a frequency table to keep the score of each word
freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

# Creating a dictionary to keep the score of each sentence
sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

# Average value of a sentence from the original text
average = int(sumValues / len(sentenceValue))

# Storing sentences into our summary.
summary = ''

for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += "" + sentence

print("==== Summary in English ====")
print(summary + '\n')
print("====  Summary in Sinhalese ====")
print(google_translator(summary, 'si'))
