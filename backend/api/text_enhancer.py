import json
import logging

import openai
from openai import OpenAI
from Settings import initialize_settings

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

settings = initialize_settings()

class openAi:
    def __init__(self, model="", temperature=0.5, top_p=1):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = model
        self.messages = []
        self.response = None
        self.temperature = temperature
        self.top_p = top_p

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def create_response(self):
        self.response = self.client.chat.completions.create(
            model=self.model,
            response_format={ "type": "json_object" },
            messages=self.messages,
            temperature=self.temperature,
            top_p=self.top_p,
        )


class highlightExtractor(openAi):
    def __init__(self, model="gpt-4-1106-preview", temperature=0.3, top_p=1):
        super().__init__(model, temperature, top_p)

    def fetch_instructions(self):
        instructions = """
        You will be provided with a block of text, and your task is to find on key sentence. It is important that you consider the whole text, from the start to the end, when looking for the key sentence.
        Not just the beginning or the end of the text.
        
        Make sure to return the sentence as a the value of a key 'sentence' in a JSON object.
        
        It is crucial that the sentence are citated exactly as they are written in the text.
        """
        return instructions

    def extract_highlights(self, text):
        self.add_message("system", self.fetch_instructions())
        self.add_message("user", text)
        try:
            self.create_response()
        except openai.AuthenticationError as e:
            raise openai.AuthenticationError(f"Authentication error: {e}")
        except openai.RateLimitError as e:
            raise openai.RateLimitError(f"Rate limit error: {e}")
        except Exception as e:
            raise Exception(f"Unexpected error: {e}")

        if self.response is None:
            raise Exception("No response available. Please try again.")

        content = self.response.choices[0].message.content

        # Check if content is a string
        if isinstance(content, str):
            try:
                # Try to parse it as JSON
                content = json.loads(content)
            except json.JSONDecodeError:
                # If it's not valid JSON, leave it as is
                pass
        
        return content
