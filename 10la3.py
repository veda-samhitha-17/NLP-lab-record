import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
sentence = "The student reads a book in the library."
tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
np_grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""
full_grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""
np_tree = nltk.RegexpParser(np_grammar).parse(tagged)
full_tree = nltk.RegexpParser(full_grammar).parse(tagged)
print("NP-only chunk tree:")
print(np_tree)
print("\nNP + VP + PP chunk tree:")
print(full_tree)