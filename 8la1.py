import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)
sentence = "Ravi plays cricket every evening."
tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
print("Word\tPOS Tag\tCategory")
for word, tag in tagged:
    if tag.startswith("NN"):
        category = "Noun"
    elif tag.startswith("VB"):
        category = "Verb"
    elif tag.startswith("RB"):
        category = "Adverb"
    else:
        category = "Other"
    print(f"{word}\t{tag}\t{category}")