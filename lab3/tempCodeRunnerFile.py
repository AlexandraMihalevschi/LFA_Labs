import re
from typing import Dict, List

# Token types
TOKEN_TYPES = {
    "AUTHOR": r"([A-Z]\.?[A-Z]?\.\s?[A-Za-z]+(?:,\s[A-Z]\.?[A-Z]?\.\s?[A-Za-z]+)*(?:,\set\sal\.)?)",
    "TITLE": r"“([^”]+)”|\"([^\"]+)\"",
    "JOURNAL": r"([A-Za-z.\s]+),",
    "VOLUME": r"vol\.?\s(\d+)",
    "ISSUE": r"no\.?\s(\d+)",
    "PAGES": r"pp\.?\s(\d+[-–]\d+)",
    "MONTH_YEAR": r"([A-Za-z]+)\.?\s(\d{4})",
    "DOI": r"doi:\s(\d{2}\.\d{4,9}/[\w.]+)",
    "BOOK": r"([A-Za-z\s]+),\s(\d+(?:rd|th|st|nd)\sed\.)",
    "CONFERENCE": r"in\s([^,]+),\s([A-Za-z\s]+),\s(\d{4})"
}

class CitationLexer:
    def __init__(self, text: str):
        self.text = text
        self.tokens: Dict[str, List[str]] = {}
    
    def tokenize(self) -> Dict[str, List[str]]:
        for token_type, pattern in TOKEN_TYPES.items():
            matches = re.findall(pattern, self.text)
            if matches:
                if isinstance(matches[0], tuple):
                    matches = [" ".join(match).strip() for match in matches if any(match)]
                self.tokens[token_type] = matches
        return self.tokens
    
    def display_tokens(self):
        for token_type, values in self.tokens.items():
            print(f"{token_type}: {', '.join(values)}")

if __name__ == "__main__":
    with open("lab3\citations.txt", "r", encoding="utf-8") as file:
        citation_text = file.read()
    
    lexer = CitationLexer(citation_text)
    tokens = lexer.tokenize()
    lexer.display_tokens()
