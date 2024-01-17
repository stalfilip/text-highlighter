import logging

import openai
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from Settings import initialize_settings
from text_enhancer import highlightExtractor
from utils.utils import highlight_quotes

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
CORS(app)

settings = initialize_settings()

def run_highlighting(text: str) -> str:
    extractor = highlightExtractor()
    res = extractor.extract_highlights(text)
    res = highlight_quotes(text, res)
    return res

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
