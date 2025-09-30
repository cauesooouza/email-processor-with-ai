# Analisador de E-mails com IA

Este projeto é uma aplicação web desenvolvida em Python com Flask que utiliza Inteligência Artificial (Google Gemini) para classificar e sugerir respostas automáticas para e-mails. O objetivo é otimizar o tempo dos usuários, identificando rapidamente e-mails produtivos e improdutivos, além de gerar respostas automáticas para e-mails que exigem ação.

## Funcionalidades

- **Upload de arquivos**: Suporte para arquivos `.txt` e `.pdf` contendo o corpo do e-mail.
- **Classificação automática**: O e-mail é classificado como "Produtivo" ou "Improdutivo" usando IA.
- **Sugestão de resposta**: Para e-mails produtivos, o sistema sugere uma resposta automática.
- **Interface amigável**: Interface web moderna e responsiva.
- **Processamento de texto**: Limpeza e pré-processamento do texto do e-mail antes da análise.

## Tecnologias Utilizadas

- Python 3.13+
- Flask
- Google Gemini API (`google-generativeai`)
- NLTK (Natural Language Toolkit)
- PyPDF
- Invoke (automatização de tarefas)

## Instalação

1. **Clone o repositório**

   ```sh
   git clone https://github.com/cauesooouza/email-processor-with-ai.git
   cd email-processor-with-ai
   ```

2. **Crie e ative o ambiente virtual**

   ```sh
   python -m venv env
   env\Scripts\activate  # Windows
   source env/bin/activate  # Linux/Mac
   ```

3. **Instale as dependências**

   ```sh
   pip install -r requirements.txt
   ```

4. **Configure a chave da API Gemini**
   - Remova `.example` do arquivo `.env.example` na raiz do projeto
   - Adicione sua chave de api do Gemini

## Uso

1. **Inicie o servidor**

   ```sh
   invoke run
   ```

2. **Acesse a aplicação**
   - Abra o navegador e acesse: [http://localhost:5000](http://localhost:5000)

3. **Envie um e-mail**
   - Cole o texto do e-mail ou faça upload de um arquivo `.txt` ou `.pdf`.
   - Clique em "Analisar".
   - Veja a classificação e a sugestão de resposta.

## Testes

Para executar os testes automatizados:

```sh
invoke test
```

## Autor

Desenvolvido por [Cauê Souza](https://github.com/cauesooouza).
