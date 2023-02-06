import MeCab
import difflib

def get_base_form(word):
    tagger = MeCab.Tagger("-Owakati")
    parsed = tagger.parse(word)
    return parsed.split()[0]

def fuzzy_search(data, query):
    query_base_form = get_base_form(query)
    match_data = []
    for d in data:
        d_base_form = get_base_form(d)
        ratio = difflib.SequenceMatcher(None, query_base_form, d_base_form).ratio()
        if ratio >= 0.8:
            match_data.append(d)
    return match_data

data = ['焼き鳥が美味しい店', '焼肉屋', '焼鳥屋', 'ウエスト焼き肉', 'やきとり一筋']
query = 'やきとり'

print(fuzzy_search(data, query))
