from app.infra.gemini_client import GeminiClient
from app.nlp.pre_processor import PreProcessor
from app.util.file_reader import FileReader


class EmailService:
    def __init__(self):
        self.file_reader = FileReader()
        self.preprocessor = PreProcessor()
        self.gemini_client = GeminiClient()
    
    def process_email_file(self, file_path: str) -> dict:
        original_text = self.file_reader.read_file(file_path)
        
        if not original_text.strip():
            return {
                'original_text': '',
                'category': '',
                'suggested_reply': ''
            }
        
        processed_text = self.preprocessor.process_text(original_text)
        category = self.gemini_client.classify_email(processed_text)
        suggested_reply = self.gemini_client.suggest_reply(original_text, category)
        
        return {
            'original_text': original_text,
            'category': category,
            'suggested_reply': suggested_reply
        }

    def process_email_text(self, email_text: str) -> dict:
        if not email_text.strip():
            return {
                'original_text': '',
                'category': '',
                'suggested_reply': ''
            }
        
        processed_text = self.preprocessor.process_text(email_text)
        category = self.gemini_client.classify_email(processed_text)
        suggested_reply = self.gemini_client.suggest_reply(email_text, category)
        
        return {
            'original_text': email_text,
            'category': category,
            'suggested_reply': suggested_reply
        }