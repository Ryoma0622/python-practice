from gensim.models import word2vec

# Define a list of sentences
sentences = [["cat", "say", "meow"], ["dog", "say", "woof"]]

# Train the model
model = word2vec.Word2Vec(sentences, size=100, window=5, min_count=1, workers=4)

# Save the model
model.save("word2vec.model")

# Load the model
model = word2vec.load("word2vec.model")

# Access the vector for a word
vector = model["dog"]

# Get the most similar words to a word
most_similar = model.wv.most_similar("dog")

print(most_similar)
