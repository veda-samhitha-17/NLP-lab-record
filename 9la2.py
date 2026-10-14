import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
sentence = "The teacher explains the lesson in the classroom."
tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<VB.*>+}
    PP: {<IN><NP>}
"""
chunker = nltk.RegexpParser(grammar)
tree = chunker.parse(tagged)
print("Chunk tree:")
print(tree)
print("\nDetected phrases:")
for subtree in tree.subtrees():
    if subtree.label() in ("NP", "VP", "PP"):
        phrase = " ".join(
            word for word, tag in subtree.leaves()
        )
        print(subtree.label(), ":", phrase)