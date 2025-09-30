import re

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')

class PreProcessor:
    def __init__(self, lang: str = 'portuguese'):
        self.stop_words = set(stopwords.words(lang))
        self.lemmatizer = WordNetLemmatizer()
        
    def process_text(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r'[^a-zA-ZáéíóúãõâêôçÁÉÍÓÚÃÕÂÊÔÇ\s]', '', text)
        tokens = word_tokenize(text, language='portuguese')
        processed_tokens = [
            self.lemmatizer.lemmatize(word) for word in tokens
            if word not in self.stop_words and len(word) > 2
        ]
        return " ".join(processed_tokens)