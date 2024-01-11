from ..api.utils.utils import parse_csv, highlight_quotes, count_words


def test_parse_content():
    # Test with normal input
    content = "highlight1; highlight2; highlight3"
    expected_output = ['highlight1', 'highlight2', 'highlight3']
    result = parse_csv(content)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test with leading and trailing spaces
    content = " highlight1 ; highlight2 ; highlight3 "
    expected_output = ['highlight1', 'highlight2', 'highlight3']
    result = parse_csv(content)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test with empty string
    content = ""
    expected_output = ['']
    result = parse_csv(content)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

    # Test with string containing only spaces
    content = "   "
    expected_output = ['']
    result = parse_csv(content)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"


def test_highlight_quotes():
    # Normal case
    text = "This is a test string."
    quotes = ["test"]
    expected = "This is a <mark>test</mark> string."
    assert highlight_quotes(text, quotes) == expected

    # Multiple occurrences
    text = "test test test."
    quotes = ["test"]
    res = highlight_quotes(text, quotes)
    expected = "<mark>test</mark> <mark>test</mark> <mark>test</mark>."
    assert res == expected

    # Multiple quotes
    text = "This is a test string."
    quotes = ["This", "test"]
    expected = "<mark>This</mark> is a <mark>test</mark> string."
    assert highlight_quotes(text, quotes) == expected

    # No quotes in text
    text = "This is a test string."
    quotes = ["not in text"]
    expected = "This is a test string."
    assert highlight_quotes(text, quotes) == expected

    # Empty quotes
    text = "This is a test string."
    quotes = [""]
    expected = "This is a test string."
    assert highlight_quotes(text, quotes) == expected

    # Empty text
    text = ""
    quotes = ["test"]
    expected = ""
    assert highlight_quotes(text, quotes) == expected

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


    