# https://qiita.com/Hironsan/items/8f7d35f0a36e0f99752c
# https://qiita.com/omuram/items/6570973c090c6f0cb060
# https://ohke.hateblo.jp/entry/2019/06/01/120000
# https://zenn.dev/robes/articles/c251dd89a0e47f
# good: https://blog.linkode.co.jp/entry/2020/10/07/130849
# sudachi: https://github.com/WorksApplications/SudachiTra

from gensim.models import word2vec
import gensim

# Train the model
model = gensim.models.Word2Vec.load('ja.bin')

# Access the vector for a word
vector = model["dog"]

# Get the most similar words to a word
most_similar = model.wv.most_similar("dog")

print(most_similar)
