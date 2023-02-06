# https://ohke.hateblo.jp/entry/2019/03/09/101500

import json
from sudachipy import dictionary

with open('/Users/jg20022/src/ghq/github.com/Ryoma0622/python-practice/venv/lib/python3.9/site-packages/sudachipy/resources/sudachi.json', 'r', encoding='utf-8') as f:
    settings = json.load(f)

print(settings)

from sudachipy import tokenizer

tokenizer_obj = dictionary.Dictionary(settings).create()
print(type(tokenizer_obj))
# <class 'sudachipy.tokenizer.Tokenizer'>

text = '友人・我孫子とスカイツリーでスパゲティを食った。'

tokens = tokenizer_obj.tokenize(tokenizer.Tokenizer.SplitMode.C, text)
print(type(tokens))

for t in tokens:
    print(t.surface(), t.part_of_speech(), t.reading_form(), t.normalized_form())
