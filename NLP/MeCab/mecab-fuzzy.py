import MeCab
import difflib
from fuzzywuzzy import fuzz

def parse_text(text):
    tagger = MeCab.Tagger("-Owakati")
    return tagger.parse(text).strip().split(" ")

def fuzzy_search(data, query):
    query_parsed = parse_text(query)
    result = []
    for item in data:
        item_parsed = parse_text(item)
        similarity = fuzz.ratio(item_parsed, query_parsed)
        print(similarity)
        if similarity >= 50: # you can adjust the threshold value
            result.append(item)
    return result


def fuzzy_search(data, query):
    query_parsed = parse_text(query)
    result = []
    # for item in data:
    #     item_parsed = parse_text(item)
    #     # print(item_parsed)
    #     # for word in item_parsed:
    #     #     print(word, query_parsed)
    #     #     Ratio = fuzz.ratio(word, query_parsed)
    #     #     print(Ratio)
    #     #     similarity = difflib.SequenceMatcher(None, word, query_parsed).ratio()
    #     #     print(similarity)
    #     similarity = fuzz.ratio(item_parsed, query_parsed)
    #     print(similarity)
    #     if similarity >= 50: # you can adjust the threshold value
    #         result.append(item)
    for item in data:
        item_parsed = parse_text(item)
        score = fuzz.token_set_ratio(query_parsed, item_parsed)
        for word in item_parsed:
            print(word, query_parsed)
            print(fuzz.token_sort_ratio(word, query_parsed))
        print(query_parsed, item_parsed)
        print(score)
        if score > 90:
            result.append(item)

    return result

data = ['焼き鳥が美味しい店', '焼肉屋', '焼鳥屋', 'ウエスト焼き肉', 'やきとり一筋']
query = 'やきとり'

print(fuzzy_search(data, query))
