import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
sentence = "The intelligent student reads a book."
tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)
print("Part-of-Speech Tagging")
print("-" * 35)
print(f"{'Word':<18}{'POS Tag'}")
print("-" * 35)
for word, tag in tagged_words:
    print(f"{word:<18}{tag}")