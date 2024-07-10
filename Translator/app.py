from flask import Flask, render_template, request, jsonify
from google.cloud import translate_v2 as translate
import os

# Initialize Flask application
app = Flask(__name__)

# Set path to the service account key file
key_path = os.path.abspath("keyfile.json")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

# Initialize Google Translate client
client = translate.Client()

# Route to serve index.html from templates folder
@app.route('/')
def index():
    return render_template('index.html')

# Translation endpoint
@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    text = data['text']
    input_language = data['input_language']
    output_language = data['output_language']

    # Call Google Translate API
    result = client.translate(text, source_language=input_language, target_language=output_language)
    translated_text = result['translatedText']

    return jsonify({'translation': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
