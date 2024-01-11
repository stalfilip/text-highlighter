from openai import OpenAI
from Settings import initialize_settings
from utils.utils import parse_csv, count_words
import openai

settings = initialize_settings()

class openAi:
    def __init__(self, model="gpt-3.5-turbo", temperature=0.5, top_p=1):
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
            messages=self.messages,
            temperature=self.temperature,
            max_tokens=64,
            top_p=self.top_p,
        )


class highlightExtractor(openAi):
    def __init__(self, model="gpt-3.5-turbo", temperature=0.0, top_p=1):
        super().__init__(model, temperature, top_p)

    def fetch_instructions(self):
        instructions = """
        You will be provided with a block of text, and your task is to extract key sentences 
        that highlight the most important parts. It's crucial that you cite the text exactly.
        Please return the key sentences in CSV format, with each sentence separated by a semi-colon.
        """
        return instructions

    def extract_highlights(self, text):
        num_sentences = max(count_words(text) // 50, 1)
        self.add_message("user", text)
        self.add_message("system", self.fetch_instructions())
        self.add_message("system", f"Look for 4 key sentences accross the whole text, from the start to the end.")
        self.add_message("system", "It's crucial that you cite the text exactly.")
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
        return parse_csv(content)
