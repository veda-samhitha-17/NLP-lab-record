import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
sentences = [
    "The student reads a book in the library.",
    "The professor teaches computer science.",
    "The students play in the playground.",
    "A researcher develops a new system.",
    "The laboratory contains modern computers."
]
grammar = r"""
    NP: {<DT|PRP\$>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""
chunker = nltk.RegexpParser(grammar)
for i, sentence in enumerate(sentences, start=1):
    tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
    tree = chunker.parse(tagged)
    print(f"\nSentence {i}: {sentence}")
    print(tree)
    for subtree in tree.subtrees():
        if subtree.label() in ("NP", "VP", "PP"):
            phrase = " ".join(
                word for word, tag in subtree.leaves()
            )
            print(f"{subtree.label()}: {phrase}")