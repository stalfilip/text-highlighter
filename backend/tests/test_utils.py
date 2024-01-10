from ..api.utils.utils import parse_csv

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