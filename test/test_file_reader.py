import unittest
from unittest.mock import MagicMock, mock_open, patch

from app.util.file_reader import FileReader


class TestFileReader(unittest.TestCase):
    @patch("app.util.file_reader.PdfReader")
    def test_read_pdf_file(self, mock_pdf_reader):
        reader = FileReader()
        mock_page = MagicMock()
        mock_page.extract_text.return_value = "texto da página"
        mock_pdf_reader.return_value.pages = [mock_page, mock_page]
        result = reader.read_file("documento.pdf")
        mock_pdf_reader.assert_called_once_with("documento.pdf")
        self.assertEqual(result, "texto da página" * 2)

    @patch("app.util.file_reader.PdfReader", side_effect=Exception("Falha PDF"))
    def test_pdf_read_error(self, mock_pdf_reader):
        reader = FileReader()
        with self.assertRaises(IOError) as context:
            reader.read_file("documento.pdf")
        self.assertIn("Não foi possivel extrair texto do arquivo PDF.", str(context.exception))

    @patch("app.util.file_reader.PdfReader")
    def test_pdf_with_no_text(self, mock_pdf_reader):
        reader = FileReader()
        mock_page = MagicMock()
        mock_page.extract_text.return_value = None
        mock_pdf_reader.return_value.pages = [mock_page]
        result = reader.read_file("documento.pdf")
        self.assertEqual(result, "")
        
    @patch("builtins.open", new_callable=mock_open, read_data="conteúdo do arquivo")
    def test_read_txt_file(self, mock_file):
        reader = FileReader()
        result = reader.read_file("documento.txt")
        mock_file.assert_called_once_with("documento.txt", "r", encoding="utf-8")
        self.assertEqual(result, "conteúdo do arquivo")
        
    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_read_empty_txt_file(self, mock_file):
        reader = FileReader()
        result = reader.read_file("documento.txt")
        self.assertEqual(result, "")

    def test_unsupported_file_type(self):
        reader = FileReader()
        with self.assertRaises(ValueError) as context:
            reader.read_file("documento.docx")
        self.assertIn("Tipo de arquivo não suportado", str(context.exception))

if __name__ == "__main__":
    unittest.main()