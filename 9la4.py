import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
sentences = [
    "a student",
    "the very intelligent student"
]
grammar = r"""
    NP: {<DT>?<RB.*>*<JJ.*>*<NN.*>+}
"""
chunker = nltk.RegexpParser(grammar)
for sentence in sentences:
    tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
    tree = chunker.parse(tagged)
    print("\nSentence:", sentence)
    print("POS tags:", tagged)
    print("Chunk tree:", tree)