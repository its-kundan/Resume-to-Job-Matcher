import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    """
    Preprocess text by tokenizing, lemmatizing, and removing stopwords/punctuation.
    """
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)