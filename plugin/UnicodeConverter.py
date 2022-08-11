# Converter Pseudocode Credits - https://github.com/Open-SL/sinhala-unicode-converter/blob/master/src/translators/singlish_to_unicode.ts
import re
import pandas as pd

vowels = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '']
vowelsUni = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
             '', '', '', '', '', '', '', '', '', '', '', '', '', '']
vowelModifiersUni = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                     '', '', '', '', '', '']
consonantsUni = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                 '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
specialConsonantsUni = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                        '', '', '', '', '', '', '']
specialConsonants = ['', '', '', '', '', '']

consonants = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
specialCharUni = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                  '', '', '', '', '', '']
specialChar = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
               '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

vowels[0] = 'ඌ'
vowels[0] = 'oo'
vowelModifiersUni[0] = 'ූ'
vowels[1] = 'ඕ'
vowels[1] = 'o\\)'
vowelModifiersUni[1] = 'ෝ'

vowels[2] = 'ඕ'
vowels[2] = 'oe'
vowelModifiersUni[2] = 'ෝ'

vowels[3] = 'ආ'
vowels[3] = 'aa'
vowelModifiersUni[3] = 'ා'

vowels[4] = 'ආ'
vowels[4] = 'a\\)'
vowelModifiersUni[4] = 'ා'

vowels[5] = 'ඈ'
vowels[5] = 'Aa'
vowelModifiersUni[5] = 'ෑ'

vowels[6] = 'ඈ'
vowels[6] = 'A\\)'
vowelModifiersUni[6] = 'ෑ'

vowels[7] = 'ඈ'
vowels[7] = 'ae'
vowelModifiersUni[7] = 'ෑ'

vowels[8] = 'ඊ'
vowels[8] = 'ii'
vowelModifiersUni[8] = 'ී'

vowels[9] = 'ඊ'
vowels[9] = 'i\\)'
vowelModifiersUni[9] = 'ී'

vowels[10] = 'ඊ'
vowels[10] = 'ie'
vowelModifiersUni[10] = 'ී'

vowels[11] = 'ඊ'
vowels[11] = 'ee'
vowelModifiersUni[11] = 'ී'
vowels[12] = 'ඒ'
vowels[12] = 'ea'
vowelModifiersUni[12] = 'ේ'

vowels[13] = 'ඒ'
vowels[13] = 'e\\)'
vowelModifiersUni[13] = 'ේ'

vowels[14] = 'ඒ'
vowels[14] = 'ei'
vowelModifiersUni[14] = 'ේ'

vowels[15] = 'ඌ'
vowels[15] = 'uu'
vowelModifiersUni[15] = 'ූ'

vowels[16] = 'ඌ'
vowels[16] = 'u\\)'
vowelModifiersUni[16] = 'ූ'

vowels[17] = 'ඖ'
vowels[17] = 'au'
vowelModifiersUni[17] = 'ෞ'

vowels[18] = 'ඇ'
vowels[18] = '/\a'
vowelModifiersUni[18] = 'ැ'

vowelsUni[19] = 'අ'
vowels[19] = 'a'
vowelModifiersUni[19] = ''

vowelsUni[20] = 'ඇ'
vowels[20] = 'A'
vowelModifiersUni[20] = 'ැ'
vowelsUni[21] = 'ඉ'
vowels[21] = 'i'
vowelModifiersUni[21] = 'ි'
vowelsUni[22] = 'එ'
vowels[22] = 'e'
vowelModifiersUni[22] = 'ෙ'
vowelsUni[23] = 'උ'
vowels[23] = 'u'
vowelModifiersUni[23] = 'ු'
vowelsUni[24] = 'ඔ'
vowels[24] = 'o'
vowelModifiersUni[24] = 'ො'
vowelsUni[25] = 'ඓ'
vowels[25] = 'I'
vowelModifiersUni[25] = 'ෛ'
nVowels = 26

specialConsonantsUni[0] = 'ං'
specialConsonants[0] = '/\\n/g'
specialConsonantsUni[1] = 'ඃ'
specialConsonants[1] = '/\\h/g'
specialConsonantsUni[2] = 'ඞ'
specialConsonants[2] = '/\\N/g'
specialConsonantsUni[3] = 'ඍ'
specialConsonants[3] = '/\\R/g'
specialConsonantsUni[4] = 'ර්' + '\u200D'
specialConsonants[4] = '/R/g'
specialConsonantsUni[5] = 'ර්' + '\u200D'
specialConsonants[5] = '/\\r/g'

consonantsUni[0] = 'ඬ'
consonants[0] = 'nnd'
consonantsUni[1] = 'ඳ'
consonants[1] = 'nndh'
consonantsUni[2] = 'ඟ'
consonants[2] = 'nng'
consonantsUni[3] = 'ථ'
consonants[3] = 'Th'
consonantsUni[4] = 'ධ'
consonants[4] = 'Dh'
consonantsUni[5] = 'ඝ'
consonants[5] = 'gh'
consonantsUni[6] = 'ඡ'
consonants[6] = 'Ch'
consonantsUni[7] = 'ඵ'
consonants[7] = 'ph'
consonantsUni[8] = 'භ'
consonants[8] = 'bh'
consonantsUni[9] = 'ශ'
consonants[9] = 'sh'
consonantsUni[10] = 'ෂ'
consonants[10] = 'Sh'
consonantsUni[11] = 'ඥ'
consonants[11] = 'GN'
consonantsUni[12] = 'ඤ'
consonants[12] = 'KN'
consonantsUni[13] = 'ළු'
consonants[13] = 'Lu'
consonantsUni[14] = 'ද'
consonants[14] = 'dh'
consonantsUni[15] = 'ච'
consonants[15] = 'ch'
consonantsUni[16] = 'ඛ'
consonants[16] = 'kh'
consonantsUni[17] = 'ත'
consonants[17] = 'th'

consonantsUni[18] = 'ට'
consonants[18] = 't'
consonantsUni[19] = 'ක'
consonants[19] = 'k'
consonantsUni[20] = 'ඩ'
consonants[20] = 'd'
consonantsUni[21] = 'න'
consonants[21] = 'n'
consonantsUni[22] = 'ප'
consonants[22] = 'p'
consonantsUni[23] = 'බ'
consonants[23] = 'b'
consonantsUni[24] = 'ම'
consonants[24] = 'm'
consonantsUni[25] = '‍ය'
consonants[25] = '\\u005C' + 'y'
consonantsUni[26] = '‍ය'
consonants[26] = 'Y'
consonantsUni[27] = 'ය'
consonants[27] = 'y'
consonantsUni[28] = 'ජ'
consonants[28] = 'j'
consonantsUni[29] = 'ල'
consonants[29] = 'l'
consonantsUni[30] = 'ව'
consonants[30] = 'v'
consonantsUni[31] = 'ව'
consonants[31] = 'w'
consonantsUni[32] = 'ස'
consonants[32] = 's'
consonantsUni[33] = 'හ'
consonants[33] = 'h'
consonantsUni[34] = 'ණ'
consonants[34] = 'N'
consonantsUni[35] = 'ළ'
consonants[35] = 'L'
consonantsUni[36] = 'ඛ'
consonants[36] = 'K'
consonantsUni[37] = 'ඝ'
consonants[37] = 'G'
consonantsUni[38] = 'ඨ'
consonants[38] = 'T'
consonantsUni[39] = 'ඪ'
consonants[39] = 'D'
consonantsUni[40] = 'ඵ'
consonants[40] = 'P'
consonantsUni[41] = 'ඹ'
consonants[41] = 'B'
consonantsUni[42] = 'ෆ'
consonants[42] = 'f'
consonantsUni[43] = 'ඣ'
consonants[43] = 'q'
consonantsUni[44] = 'ග'
consonants[44] = 'g'
consonantsUni[45] = 'ර'
consonants[45] = 'r'

specialCharUni[0] = 'ෲ'
specialChar[0] = 'ruu'
specialCharUni[1] = 'ෘ'
specialChar[1] = 'ru'
specialCharUni[2] = '්‍ර'
specialChar[2] = 'ra'


def converter(text):
    s = ""
    v = ""
    r = ""

    for i in range(len(specialConsonants)):
        text = text.replace(specialConsonants[i], specialConsonantsUni[i])

    for i in range(len(specialCharUni)):
        for j in range(len(consonants)):
            s = consonants[j] + specialChar[i]
            v = consonantsUni[j] + specialCharUni[i]
            r = re.search(s, "g")
            print(r, v, s)
            text = text.replace(r, v)

    for j in range(len(consonants)):
        for i in range(len(vowels)):
            s = consonants[j] + "r" + vowels[i]
            v = consonantsUni[j] + "්‍ර" + vowelModifiersUni[i]
            r = re.search(s, "g")
            text = text.replace(r, v)
        s = consonants[j] + "r"
        v = consonantsUni[j] + "්‍ර"
        r = re.search(s, "g")
        text = text.replace(r, v)

    for i in range(len(consonants)):
        for j in range(nVowels):
            s = consonants[i] + vowels[j]
            v = consonantsUni[i] + vowelModifiersUni[j]
            r = re.search(s, "g")
            text = text.replace(r, v)

    for i in range(len(consonants)):
        r = re.search(consonants[i], "g")
        text = text.replace(r, consonantsUni[i] + "්")

    for i in range(len(vowels)):
        r = re.search(vowels[i], "g")
        text = text.replace(r, vowelsUni[i])

    return text


# reading dataset

df = pd.read_excel(r'dataset/dataset.xlsx', sheet_name='dataset2')
cd = pd.DataFrame(df, columns=['Phrase', 'Summary'])
print("==== Original Dataset ====")
print(cd)

print("==== JSONL Format ====")
# printing the GPT-3 format
for index, row in df.iterrows():
    print('{"prompt":"' + row['Phrase'] + ' -->","completion":"', row['Summary'] + '"}')
