import json

from ..api.utils.utils import count_words, highlight_quotes


def test_highlight_quotes():
    # Normal case
    text = "This is a quote1 string."
    json_obj = json.loads('{"test": "quote1"}')
    expected = "This is a <mark>quote1</mark> string."
    assert highlight_quotes(text, json_obj) == expected

    # Multiple occurrences
    text = "quote1 quote1 quote1."
    json_obj = json.loads('{"test": "quote1"}')
    res = highlight_quotes(text, json_obj)
    expected = "<mark>quote1</mark> <mark>quote1</mark> <mark>quote1</mark>."
    assert res == expected

    # Value not in text
    text = "This is a test string."
    json_obj = json.loads('{"test": "not in text"}')
    expected = "This is a test string."
    assert highlight_quotes(text, json_obj) == expected

    # Empty text
    text = ""
    json_obj = json.loads('{"test": "quote1"}')
    expected = ""
    assert highlight_quotes(text, json_obj) == expected

    # Empty JSON object
    text = "This is a test string."
    json_obj = json.loads('{}')
    expected = "This is a test string."
    assert highlight_quotes(text, json_obj) == expected

    # JSON object with empty value
    text = "This is a test string."
    json_obj = json.loads('{"test": ""}')
    expected = "This is a test string."
    assert highlight_quotes(text, json_obj) == expected

def test_count_words():
    # Normal case
    text = "This is a test string."
    expected = 5
    assert count_words(text) == expected

    # Empty string
    text = ""
    expected = 0
    assert count_words(text) == expected

    # String with only spaces
    text = "   "
    expected = 0
    assert count_words(text) == expected

    # String with only one word
    text = "test"
    expected = 1
    assert count_words(text) == expected


    