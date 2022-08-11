from googletrans import Translator

translator = Translator()
print("Sinhala to English")
translation = translator.translate(
    'මේ දෙන්නා මෙහෙම විලෙන් පිටවෙලා යන්ට කතා කර ගන්න කොට එතන ලඟ හිටිය ඉබ්බෙක් මේ කතාවට කන් දීගෙන හිටියා.', dest='en')
print(translation.text)

print("English to Sinhala")
translation = translator.translate(
    'When these two got out of the lake and started talking, a turtle nearby was listening to this conversation.',
    dest='si')
print(translation.text)

# language codes - https://gist.github.com/JT5D/a2fdfefa80124a06f5a9
# Summarize using GPT-3
# Translate summary from English back to Sinhalese
# Messure data loss and level of accuracy
