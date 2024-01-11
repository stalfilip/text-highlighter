from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from Settings import initialize_settings
from text_enhancer import highlightExtractor
from utils.utils import highlight_quotes
import openai

app = Flask(__name__)
CORS(app)

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
    try:
        data = request.json
        text = data['text']
        result = run_highlighting(text)
        return jsonify({"text": result})
    except openai.AuthenticationError:
        return make_response(jsonify({"error": "Authentication error with OpenAI API"}), 401)
    except openai.RateLimitError:
        return make_response(jsonify({"error": "Rate limit error with OpenAI API"}), 429)
    except KeyError:
        return make_response(jsonify({"error": "Internal server error: missing 'text' in request data"}), 400)
    except Exception as e:
        return make_response(jsonify({"error": f"Internal server error: {str(e)}"}), 500)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return make_response(jsonify({"error": "Method not allowed"}), 405)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
