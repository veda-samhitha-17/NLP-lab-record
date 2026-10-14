import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
sentence = "The boy plays in the garden."
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)
print("POS-tagged words:")
print(tagged_words)
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""
chunker = nltk.RegexpParser(grammar)
chunk_tree = chunker.parse(tagged_words)
print("\nChunk tree:")
print(chunk_tree)
print("\nIdentified noun phrases:")
for subtree in chunk_tree.subtrees(
    filter=lambda t: t.label() == "NP"
):
    print(" ".join(word for word, tag in subtree.leaves()))