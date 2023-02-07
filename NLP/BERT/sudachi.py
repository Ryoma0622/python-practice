# https://www.koi.mashykom.com/bert.html
# https://tt-tsukumochi.com/archives/4908
# https://huggingface.co/docs/transformers/main_classes/output

from sudachitra.tokenization_bert_sudachipy import BertSudachipyTokenizer
from transformers import BertModel, BertJapaneseTokenizer, AutoModelForMaskedLM
import torch
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

tokenizer = BertSudachipyTokenizer.from_pretrained('chiTra-1.0')
# print(tokenizer.tokenize("選挙管理委員会とすだち"))
# print(tokenizer.tokenize("しょう油を１本買いました"))

model = BertModel.from_pretrained('chiTra-1.0')
# outputs = model(**tokenizer("まさにオールマイティーな商品だ。", return_tensors="pt"))
# print(outputs.last_hidden_state.shape)
# print(outputs.keys())
# print(model)
# print(model.embeddings)

# input_word = "犬"
# input_ids = tokenizer.encode(input_word, return_tensors="pt")
# print(input_ids)

# with torch.no_grad():
#     outputs = model(input_ids)
# word_embeddings = outputs[0][0][0].numpy()

# print(word_embeddings)

# def extract_synonyms(word, model, tokenizer):
#     input_ids = tokenizer.encode(word, return_tensors="pt")
#     with torch.no_grad():
#         last_hidden_states = model(input_ids).last_hidden_state
#     # word_embeddings = last_hidden_states[0][0].detach().numpy()
#     # word_embeddings = last_hidden_states[0][0][0].numpy()
#     # print(word_embeddings)
#     # word_cosine_similarities = cosine_similarity(word_embeddings, word_embeddings)
#     # word_cosine_similarities = word_cosine_similarities[0]
#     # most_similar_indices = np.argsort(-word_cosine_similarities)
#     # synonyms = [tokenizer.decode([i]) for i in most_similar_indices if i != 0]
#     # return synonyms

# word = "犬"
# synonyms = extract_synonyms(word, model, tokenizer)
# print("Synonyms for the word '%s':" % word)
# print(synonyms)

text = "これはテストです。私はトムです。"

encoded_text = tokenizer(text)
print(encoded_text)

tokens = tokenizer.convert_ids_to_tokens(encoded_text.input_ids)
print(tokens)

# サンプルデータ
raw_inputs = [
    "私は毎週水曜日にカフェで勉強します。",
    "その後、ジムに寄ってから帰ります。",
]

# サンプルデータを入力してTokenizerによる変換を行う
tokenized_inputs = tokenizer(raw_inputs, padding=True, truncation=True, return_tensors='pt')

print(tokenized_inputs)

converted_tokenized_inputs = [*map(lambda x: tokenizer.convert_ids_to_tokens(x), tokenized_inputs.input_ids)]
for inputs in converted_tokenized_inputs:
    print(''.join(inputs))

for input_ids in tokenized_inputs.input_ids:
    print(tokenizer.decode(input_ids).replace(' ', ''))
