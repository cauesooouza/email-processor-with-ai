import google.generativeai as genai

from config import GEMINI_API_KEY


class GeminiClient:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("A chave da API Gemini não foi configurada.")
        
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.5-flash-lite')

    def classify_email(self, text: str) -> str:
        prompt = f"""
Classifique o texto do email abaixo como 'Produtivo' ou 'Improdutivo':
- Produtivo: requer ação, resposta ou atenção.
- Improdutivo: não requer ação imediata.

Responda apenas com uma das palavras: Produtivo ou Improdutivo.

Email:
{text}
"""
        
        try:
            response = self.model.generate_content(prompt)
            category = response.text.strip().replace("'", "").replace('"', '')
            if category not in ['Produtivo', 'Improdutivo']:
                return "Produtivo"
            return category
        except Exception as e:
            print(f"Erro na API Gemini ao classificar: {e}")
            raise ConnectionError("Falha ao comunicar com a API Gemini para classificação.")

    def suggest_reply(self, original_text: str, category: str) -> str:
        if category == "Improdutivo":
            return "Este email não parece necessitar de uma resposta. Se desejar, um simples 'Obrigado!' pode ser suficiente."

        prompt = f"""
Com base no email abaixo, classificado como 'Produtivo', gere uma resposta curta, profissional e em português. 
A resposta deve ser objetiva e servir como ponto de partida.

Email:
{original_text}
"""
        
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"Erro na API Gemini ao sugerir resposta: {e}")
            raise ConnectionError("Falha ao comunicar com a API Gemini para sugestão de resposta.")
