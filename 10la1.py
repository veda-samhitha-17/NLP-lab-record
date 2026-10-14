import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
sentence = "The young scientist is developing a new application."
tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""
tree = nltk.RegexpParser(grammar).parse(tagged)
print("Chunk tree:")
print(tree)
print("\nIdentified phrases:")
for subtree in tree.subtrees():
    if subtree.label() in ("NP", "VP", "PP"):
        print(
            subtree.label(),
            ":",
            " ".join(word for word, tag in subtree.leaves())
        )