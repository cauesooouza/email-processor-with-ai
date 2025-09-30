import logging
import os

import nltk
from flask import Flask, render_template, request

from app.service.email_service import EmailService

logging.basicConfig(level=logging.INFO)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

for resource in ['stopwords', 'punkt', 'wordnet']:
    try:
        nltk.data.find(f'corpora/{resource}' if resource in ['stopwords', 'wordnet'] else f'tokenizers/{resource}')
    except LookupError:
        nltk.download(resource)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        result = None
        file = request.files.get('file')
        email_text = request.form.get('email_text', '').strip()

        if file and file.filename != '':
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)  
            file.save(filepath)
            try:
                service = EmailService()
                result = service.process_email_file(filepath)
            except Exception as error:
                logging.error(f"Ocorreu um erro: {error}")
                result = {'error': str(error)}
            finally:
                if os.path.exists(filepath):
                    os.remove(filepath)
        elif email_text:
            try:
                service = EmailService()
                result = service.process_email_text(email_text)
            except Exception as error:
                print(f"Ocorreu um erro: {error}")
                result = {'error': str(error)}
        else:
            result = {'error': 'Nenhum conteúdo fornecido.'}

        return render_template('index.html', result=result)

    return render_template('index.html', result=None)

if __name__ == '__main__':
    env = os.getenv('FLASK_ENV', 'production')
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=(env == 'development'))