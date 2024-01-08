from Settings import settings
from text_enhancer import openAi, KeywordExtractor


def main():
    keyword_extractor = KeywordExtractor()
    keyword_extractor.add_message("system", "You will be provided with a block of text, and your task is to extract a list of keywords from it.")
    text = read_file()
    keyword_extractor.add_message("user", text)
    keywords = keyword_extractor.extract_keywords(text)
    print(keywords)

def read_file():
    with open("api/lib/reuters.txt", "r") as file:
        text = file.read()
    return text

if __name__ == "__main__":
    main()