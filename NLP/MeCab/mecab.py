import MeCab

# create MeCab Tagger
m = MeCab.Tagger()

# input text
text = "吾輩は猫である。名前はまだ無い。どこで生れたかとんと見当がつかぬ。何でも薄暗いじめじめした所でニヤーニヤー泣いてゐた事だけは記憶してゐる。吾輩はここで始めて人間といふものを見た。しかもあとで聞くとそれは書生といふ人間中で一番獰悪な種族であつたさうだ。この書生といふのは時々我々を捕へて煮て食ふといふ話である。しかしその当時は何といふ考へもなかつたから別段恐しいとも思はなかつた。"

# perform morphological analysis
result = m.parse(text)

# print the result
print(result)
