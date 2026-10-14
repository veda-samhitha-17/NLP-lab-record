import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
sentences = [
    "The tall boy runs fast.",
    "A beautiful flower blooms.",
    "The computer science student studies NLP."
]
chunker = nltk.RegexpParser(
    r"NP: {<DT>?<JJ.*>*<NN.*>+}"
)
for sentence in sentences:
    tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
    tree = chunker.parse(tagged)
    phrases = [
        " ".join(word for word, tag in subtree.leaves())
        for subtree in tree.subtrees(
            filter=lambda t: t.label() == "NP"
        )
    ]
    print("\nSentence:", sentence)
    print("Noun phrases:", phrases)