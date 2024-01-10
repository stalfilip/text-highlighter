from Settings import Settings
from text_enhancer import highlightExtractor

settings = Settings()


def main():
    extractor = highlightExtractor()
    extractor.add_message(
        "system",
        "You will be provided with a block of text, and your task is to extract a list of keywords from it.",
    )
    text = read_file()
    extractor.add_message("user", text)
    sentences = extractor.extract_highlights(text)
    print(sentences)


def read_file():
    with open("api/lib/reuters.txt", "r") as file:
        text = file.read()
    return text


if __name__ == "__main__":
    main()
