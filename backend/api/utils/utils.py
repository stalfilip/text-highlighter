def parse_csv(content):
    return [highlight.strip() for highlight in content.split(";")]