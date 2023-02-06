import nltk
nltk.download('punkt')

sentence = "I don't know about why I need to do that."
tokens = nltk.word_tokenize(sentence)
print(tokens)
