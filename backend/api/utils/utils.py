
def highlight_quotes(text, json_obj):
    for key, value in json_obj.items():
        if value:  # Check if the value is not an empty string
            text = text.replace(value, f"<mark>{value}</mark>")

    return text

def count_words(text):
    return len(text.split())