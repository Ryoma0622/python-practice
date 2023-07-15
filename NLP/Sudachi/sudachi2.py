from sudachipy import tokenizer
from sudachipy import dictionary

# トークナイザの作成
config_path = "/Users/jodoi/src/ghq/github.com/Ryoma0622/python-practice/venv/lib/python3.9/site-packages/sudachipy/resources/sudachi.json"
tokenizer_obj = dictionary.Dictionary(config_path=config_path).create()

text = "すもももももももものうち、東京特許許可局、りんごジュース"

mode = tokenizer.Tokenizer.SplitMode.A
print(mode,"==>",[t.surface() for t in tokenizer_obj.tokenize(text, mode)])

mode = tokenizer.Tokenizer.SplitMode.B
print(mode,"==>",[t.surface() for t in tokenizer_obj.tokenize(text, mode)])

mode = tokenizer.Tokenizer.SplitMode.C
print(mode,"==>",[t.surface() for t in tokenizer_obj.tokenize(text, mode)])

mode = tokenizer.Tokenizer.SplitMode.C
tokens = tokenizer_obj.tokenize(text,mode)
print(tokens,"====")
outputArray = []
for t in tokens:
    outputArray = t.surface(),t.part_of_speech(),t.reading_form(),t.normalized_form()
    print(outputArray)
