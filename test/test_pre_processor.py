import unittest
from unittest.mock import patch

from app.nlp.pre_processor import PreProcessor


class TestPreProcessor(unittest.TestCase):
    def setUp(self):
        self.stopwords_patch = patch('nltk.corpus.stopwords.words', return_value=['e', 'a', 'o'])
        self.mock_stopwords = self.stopwords_patch.start()

        self.tokenize_patch = patch('nltk.tokenize.word_tokenize', side_effect=self.mock_tokenize)
        self.mock_tokenize_func = self.tokenize_patch.start()

        self.lemmatizer_patch = patch(
            'nltk.stem.WordNetLemmatizer.lemmatize',
            side_effect=lambda *args, **kwargs: args[-1] + '_lemma'
        )
        self.mock_lemmatizer = self.lemmatizer_patch.start()
        self.processor = PreProcessor(lang='portuguese')

    def tearDown(self):
        self.stopwords_patch.stop()
        self.tokenize_patch.stop()
        self.lemmatizer_patch.stop()

    def mock_tokenize(self, text, language=None):
        return text.split()

    def test_lowercase_and_regex(self):
        result = self.processor.process_text('Olá, MUNDO! 123')
        self.assertEqual(result, 'olá_lemma mundo_lemma')

    def test_stopword_removal(self):
        result = self.processor.process_text('e casa a rua o sol')
        self.assertEqual(result, 'casa_lemma rua_lemma sol_lemma')

    def test_token_length_filtering(self):
        result = self.processor.process_text('um sol no céu')
        self.assertEqual(result, 'sol_lemma céu_lemma')

    def test_lemmatization(self):
        result = self.processor.process_text('casas ruas')
        self.assertEqual(result, 'casas_lemma ruas_lemma')

    def test_empty_string(self):
        result = self.processor.process_text('')
        self.assertEqual(result, '')

    def test_only_stopwords(self):
        result = self.processor.process_text('e a o')
        self.assertEqual(result, '')

    def test_only_short_words(self):
        result = self.processor.process_text('um no')
        self.assertEqual(result, '')

if __name__ == '__main__':
    unittest.main()