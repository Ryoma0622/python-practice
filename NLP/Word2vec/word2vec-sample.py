import MeCab
import pandas as pd

tagger = MeCab.Tagger()


def mecab_tokenizer(text):
    # テキストを分かち書きする関数を準備する
    parsed_lines = tagger.parse(text).split("\n")[:-2]
    surfaces = [l.split('\t')[0] for l in parsed_lines]
    features = [l.split('\t')[1] for l in parsed_lines]
    # 原型を取得
    bases = [f.split(',')[6] for f in features]
    # 配列で結果を返す
    token_list = [b if b != '*' else s for s, b in zip(surfaces, bases)]
    # アルファベットを小文字に統一
    token_list = [t.lower() for t in token_list]
    return token_list


# コーパスの見込み (df["text"]にニュース記事本文が入る。)
df = pd.read_csv("./livedoor_news_corpus.csv")


# 不要な文字を消す
stop_chars = "\n,.、。()（）「」　『 』[]【】“”!！ ?？—:・■●★▲▼"
for stop_char in stop_chars:
    df["text"] = df["text"].str.replace(stop_char, " ")

# ユニコード正規化
df["text"] = df["text"].str.normalize("NFKC")
# アルファベットを小文字に統一
df["text"] = df["text"].str.lower()

# 分かち書きしたデータを作成
sentences = df["text"].apply(mecab_tokenizer)

# 作成されたデータのサンプル
print(sentences[:5])
