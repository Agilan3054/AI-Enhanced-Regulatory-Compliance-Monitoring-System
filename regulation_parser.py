import re
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

nltk.download('punkt')
nltk.download('stopwords')

def parse_regulation_text(regulation_text):
    sentences = sent_tokenize(regulation_text)
    cleaned_sentences = [re.sub(r'\W', ' ', sentence).lower() for sentence in sentences]
    stop_words = set(stopwords.words('english'))
    vectorizer = CountVectorizer(stop_words=stop_words)
    X = vectorizer.fit_transform(cleaned_sentences)
    return vectorizer.get_feature_names_out()

# Example usage
if __name__ == "__main__":
    with open('regulation_document.txt', 'r') as file:
        regulation_text = file.read()
    features = parse_regulation_text(regulation_text)
    print("Extracted features:", features)
