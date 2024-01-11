def parse_csv(content):
    return [highlight.replace('"', '').strip() for highlight in content.split(";")]

def highlight_quotes(text, quotes):
    for quote in quotes:
        if quote and quote in text:
            text = text.replace(quote, f"<mark>{quote}</mark>")
    return text

def count_words(text):
    return len(text.split())