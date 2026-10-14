import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
sentence = "The young researcher develops an AI model."
tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""
chunker = nltk.RegexpParser(grammar)
tree = chunker.parse(tagged)
print("POS-tagged sequence:")
print(tagged)
print("\nChunk tree:")
print(tree)
print("\nNoun phrases:")
for subtree in tree.subtrees(
    filter=lambda t: t.label() == "NP"
):
    print(" ".join(word for word, tag in subtree.leaves()))