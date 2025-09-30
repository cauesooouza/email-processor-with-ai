import unittest
from unittest.mock import patch

from app.infra.gemini_client import GeminiClient


class TestGeminiClient(unittest.TestCase):
    @patch("app.infra.gemini_client.GEMINI_API_KEY", "fake-key")
    @patch("app.infra.gemini_client.genai")
    def test_init_with_api_key(self, mock_genai):
        client = GeminiClient()
        mock_genai.configure.assert_called_once_with(api_key="fake-key")
        self.assertIsNotNone(client.model)

    @patch("app.infra.gemini_client.GEMINI_API_KEY", None)
    def test_init_without_api_key(self):
        with self.assertRaises(ValueError) as context:
            GeminiClient()
        self.assertIn("A chave da API Gemini não foi configurada.", str(context.exception))


class TestGeminiClientIntegration(unittest.TestCase):
    def setUp(self):
        self.client = GeminiClient()

    def test_classify_email_produtivo(self):
        result = self.client.classify_email("Preciso de suporte técnico para meu produto.")
        self.assertIn(result, ["Produtivo", "Improdutivo"])

    def test_classify_email_improdutivo(self):
        result = self.client.classify_email("Parabéns pelo seu aniversário!")
        self.assertIn(result, ["Produtivo", "Improdutivo"])

    def test_suggest_reply_produtivo(self):
        reply = self.client.suggest_reply("Preciso de suporte técnico para meu produto.", "Produtivo")
        self.assertIsInstance(reply, str)
        self.assertTrue(len(reply) > 0)

    def test_suggest_reply_improdutivo(self):
        reply = self.client.suggest_reply("Parabéns pelo seu aniversário!", "Improdutivo")
        self.assertIn("não parece necessitar de uma resposta", reply)


if __name__ == "__main__":
    unittest.main()