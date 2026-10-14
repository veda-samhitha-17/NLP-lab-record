import nltk

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)

sentences = [
    "The children are playing outside.",
    "She writes beautiful poems.",
    "They visited the library yesterday."
]

def classify(tag):
    if tag.startswith("NN"):
        return "Noun"
    elif tag.startswith("VB"):
        return "Verb"
    elif tag.startswith("JJ"):
        return "Adjective"
    elif tag.startswith("RB"):
        return "Adverb"
    elif tag.startswith("PRP"):
        return "Pronoun"
    elif tag == "DT":
        return "Determiner"
    return "Other"

for sentence in sentences:
    print("\nSentence:", sentence)
    print("Word\tTag\tCategory")

    for word, tag in nltk.pos_tag(nltk.word_tokenize(sentence)):
        print(f"{word}\t{tag}\t{classify(tag)}")