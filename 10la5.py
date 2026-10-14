import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
sentence = "The scientist is developing a new application."
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)
basic_grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
"""
improved_grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD|VB.*><VB.*>*}
"""
basic_chunker = nltk.RegexpParser(basic_grammar)
improved_chunker = nltk.RegexpParser(improved_grammar)
basic_tree = basic_chunker.parse(tagged_words)
improved_tree = improved_chunker.parse(tagged_words)
print("POS-tagged words:")
print(tagged_words)
print("\nBasic Chunk Tree:")
print(basic_tree)
print("\nImproved Chunk Tree:")
print(improved_tree)