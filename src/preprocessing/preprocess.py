# src/preprocessing/preprocess.py
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    """
    Preprocess text by tokenizing, lemmatizing, and removing stopwords/punctuation.
    Handles empty text and unexpected characters gracefully.
    """
    if not text:
        return ""
    try:
        doc = nlp(text)
        tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
        return " ".join(tokens)
    except Exception as e:
        print(f"Error during preprocessing: {e}")
        return ""
