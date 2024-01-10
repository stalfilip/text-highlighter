from flask import Flask, jsonify, request
from Settings import initialize_settings
from text_enhancer import highlightExtractor
from utils.utils import highlight_quotes

app = Flask(__name__)
settings = initialize_settings()

def run_highlighting(text):
    extractor = highlightExtractor()
    extractor.add_message(
        "system",
        "You will be provided with a block of text, and your task is to extract a list of keywords from it.",
    )
    extractor.add_message("user", text)
    sentences = extractor.extract_highlights(text)
    print(f"nr of sentences: {len(sentences)}")
    highlighted_text = highlight_quotes(text, sentences)
    return highlighted_text

@app.route('/ingest', methods=['POST'])
def ingest():
    data = request.json
    text = data['text']
    result = run_highlighting(text)
    return jsonify({"text": result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
