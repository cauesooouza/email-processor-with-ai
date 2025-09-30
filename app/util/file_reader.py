import logging
import os

from pypdf import PdfReader


class FileReader:
    def read_file(self, file_path: str) -> str:
        _, extension = os.path.splitext(file_path)
        
        if extension.lower() == '.txt':
            return self._read_txt(file_path)
        elif extension.lower() == '.pdf':
            return self._read_pdf(file_path)
        else:
            raise ValueError(f"Tipo de arquivo não suportado: {extension}")

    
    def _read_txt(self, file_path: str) -> str:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
        
    def _read_pdf(self, file_path: str) -> str:
        text = ""
        try:
            reader = PdfReader(file_path)
            for page in reader.pages:
                text += page.extract_text() or ""
        except Exception as error:
            logging.error(f"Erro ao ler PDF: {error}")
            raise IOError("Não foi possivel extrair texto do arquivo PDF.")
        return text