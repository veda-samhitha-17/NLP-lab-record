import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
sentences = [
    "I read a book.",
    "Please book a ticket.",
    "Children play football.",
    "We watched a play."
]
for sentence in sentences:
    tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
    print("\nSentence:", sentence)
    print("Tagged words:", tagged)