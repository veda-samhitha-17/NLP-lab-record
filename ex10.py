import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
sentence = "The intelligent student reads a book in the library."
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)
print("POS-tagged words:")
print(tagged_words)
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""
chunker = nltk.RegexpParser(grammar)
chunk_tree = chunker.parse(tagged_words)
print("\nChunk tree:")
print(chunk_tree)
print("\nIdentified phrases:")
for subtree in chunk_tree.subtrees():
    if subtree.label() in ("NP", "VP", "PP"):
        phrase = " ".join(
            word for word, tag in subtree.leaves()
        )
        print(f"{subtree.label()}: {phrase}")