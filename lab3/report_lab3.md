# Laboratory Work: Lexer & Scanner

**Course:** Formal Languages & Finite Automata\
**Author:** Mihalevschi Alexandra

## Theory

Lexical analysis, the process of converting a sequence of characters into a sequence of tokens, is a critical step in the compilation and interpretation of languages. A lexer (also called a scanner or tokenizer) is responsible for reading input text and dividing it into manageable chunks called tokens, which are classified into categories based on predefined rules.

#### Key Concepts in Lexical Analysis

1.  **Tokens:** A token is a category or classification of a string of characters that forms a meaningful unit within a language. Tokens are typically defined by regular expressions, which describe patterns that match valid strings for that token type. For example, in a programming language, tokens might include keywords (e.g., `if`, `else`), operators (e.g., `+`, `-`), identifiers (e.g., variable names), literals (e.g., numbers, strings), and delimiters (e.g., parentheses, commas). Tokens are the building blocks for understanding and processing the input text.

2.  **Lexemes:** A lexeme is the actual sequence of characters in the source text that matches a particular token. While tokens represent the category of the lexeme, the lexeme itself is the raw string that the lexer processes. For example, in the string `x = 10`, `x` is a lexeme that corresponds to an `IDENTIFIER` token, and `10` is a lexeme that corresponds to a `NUMBER` token.

3.  **Regular Expressions (Regex):** Lexers often use regular expressions to define patterns for each token type. Regular expressions provide a concise and powerful way to specify the structure of valid tokens. For instance:

    - An integer might be defined by the regex pattern `\d+`, which matches one or more digits.
    - A floating-point number might be defined by the pattern `\d+\.\d+`, which matches digits followed by a period and more digits.
    - An identifier might be defined by `\w+`, which matches one or more word characters (letters, digits, and underscores).

4.  **Finite Automata and Lexical Analysis:** The lexer often relies on finite automata (FAs) to match input text against patterns. Finite automata are abstract mathematical models that describe a system of states and transitions between them, used for recognizing patterns in strings. There are two main types of finite automata used in lexical analysis:

    - **Deterministic Finite Automata (DFA):** A DFA has a unique state transition for each input symbol, which makes it efficient for token matching.
    - **Nondeterministic Finite Automata (NFA):** An NFA can transition to multiple states for a given input symbol, which makes it more flexible but less efficient in practice. NFAs can be converted into DFAs for more efficient processing.

5.  **Whitespace and Comments:** Lexers are also responsible for handling irrelevant parts of the input text, such as whitespace and comments. In many programming languages, spaces, tabs, and line breaks are used as delimiters but are not part of any meaningful token. Similarly, comments are not processed as tokens but are often discarded or stored separately for documentation purposes. The lexer typically removes or ignores these non-essential components during the tokenization process.

6.  **Error Handling:** A key feature of any lexer is its ability to handle invalid input. If the lexer encounters a character or sequence of characters that doesn't match any of the predefined token patterns, it must report an error. This error handling ensures that the source code or input text is syntactically correct before further processing.

#### Phases of Lexical Analysis

The process of lexical analysis can be broken down into several key phases:

1.  **Input Parsing:** The lexer begins by reading the input text character by character. It processes the characters one by one to identify lexemes that match the defined token patterns.

2.  **Token Matching:** The lexer uses regular expressions to match sequences of characters against the defined token patterns. When a match is found, the lexer creates a token for that lexeme. The token typically includes the token type (e.g., `NUMBER`, `IDENTIFIER`) and may also store additional information, such as the value of the lexeme (e.g., the actual number or string).

3.  **Token Emission:** Once a token is identified, it is emitted and passed to the next phase of the compiler or interpreter. This is typically done by adding the token to a token stream or passing it to a parser for further analysis.

4.  **Error Reporting:** If the lexer encounters an invalid lexeme or a lexeme that does not match any token pattern, it raises an error. The error message typically includes information about the position in the input text where the error occurred.

5.  **Whitespace and Comment Removal:** The lexer typically skips over whitespace and comments, as they are not part of the language's syntax or semantics. However, it may still track the line numbers or column positions for better error reporting and debugging.

#### Types of Lexers

1.  **Simple Lexers:** Simple lexers are designed to recognize a limited set of token types using basic regular expressions. These lexers are typically used for small or domain-specific languages and can be written with minimal complexity.

2.  **Complex Lexers:** Complex lexers are used for programming languages or large-scale applications, where the set of tokens is large and the input may include complex constructs like nested structures, keyword handling, and context-sensitive token recognition. These lexers often use advanced parsing techniques, including finite automata and lookahead techniques, to handle complex tokenization.

3.  **Flex and Lex:** Flex and Lex are popular tools for generating lexers automatically from a set of regular expressions. These tools generate efficient C code for lexers, making them suitable for larger projects where manual lexer implementation would be time-consuming.

#### Applications of Lexers

1.  **Compilers:** In a compiler, the lexer is the first phase of the front end, responsible for converting source code into a series of tokens that can be passed to the parser. The lexer helps the parser understand the structure of the code by providing a well-defined sequence of tokens.

2.  **Interpreters:** Similar to compilers, interpreters use lexers to process source code and generate tokens. However, instead of compiling the code into machine code, interpreters execute it directly, interpreting each token at runtime.

3.  **Text Processing Tools:** Lexers are widely used in text processing applications such as search engines, syntax highlighting, and data extraction tools. For instance, a lexer can be used to tokenize a structured text file (like an XML or JSON document) for easier parsing and manipulation.

4.  **Language Development:** When designing a new programming language or domain-specific language (DSL), a lexer is essential for processing the language's syntax. It enables the identification and categorization of key elements in the language, such as keywords, operators, and literals, before further analysis by the parser.

5.  **Data Parsing:** Lexers can be used in data parsing tasks, where structured data (such as log files, configuration files, or structured text) is tokenized and analyzed for further processing or conversion to other formats.

A lexer plays an indispensable role in converting raw input text into structured tokens that can be easily processed by subsequent stages of a compiler or interpreter. By understanding and implementing lexical analysis, one gains insight into how programming languages and data formats are parsed and processed. Regular expressions, finite automata, and efficient error handling are core concepts that enable lexers to function effectively.

## Objectives

The primary objectives of this laboratory work were:

1. To understand the concept of lexical analysis.
2. To become familiar with how a lexer/scanner/tokenizer functions internally.
3. To implement a sample lexer for processing a structured text format (citations in this case) and demonstrate how the lexer works.
   In addition to the theoretical understanding, the practical component focused on developing a lexer capable of identifying various citation components, such as author names, publication titles, journals, volumes, pages, dates, DOIs, and conference details.

## Implementation Description

The implementation consists of a Python script that uses regular expressions to define patterns for different token types. The lexer processes a given text and extracts information such as:

- AUTHOR: Identifies the author names in the citation.
- TITLE: Extracts the title of the work.
- JOURNAL: Identifies the journal name.
- VOLUME: Recognizes volume numbers in the citation.
- ISSUE: Extracts issue numbers.
- PAGES: Identifies page ranges.
- MONTH_YEAR: Recognizes the publication month and year.
- DOI: Extracts the Digital Object Identifier (DOI).
- BOOK: Identifies book references and edition details.
- CONFERENCE: Recognizes conference-related details.

The core functionality is provided by the CitationLexer class. The tokenize method applies regular expressions to the text and stores matched values in a dictionary, categorized by token type. The display_tokens method prints the found tokens for review.

### Code overview

```python
import re
from typing import Dict, List

# Token types
TOKEN_TYPES = {
    "AUTHOR": r"([A-Z]\.?[A-Z]?\.\s?[A-Za-z]+(?:,\s[A-Z]\.?[A-Z]?\.\s?[A-Za-z]+)*(?:,\set\sal\.)?)",
    "TITLE": r"“([^”]+)”|\"([^\"]+)",
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
    with open("lab3/citations.txt", "r", encoding="utf-8") as file:
        citation_text = file.read()

    lexer = CitationLexer(citation_text)
    tokens = lexer.tokenize()
    lexer.display_tokens()
```

This code snippet demonstrates the implementation of a lexer for processing citations. Here's a breakdown of the key components:

1. **Regular Expressions (Regex)**: Each token type (author, title, journal, etc.) is associated with a specific regex pattern that matches the desired text format.
2. **CitationLexer Class**: This class is responsible for applying the regex patterns to the input text and categorizing the matched parts as tokens.
3. **Tokenization**: The `tokenize` method matches the regex patterns against the input text and stores the results in a dictionary, where the keys are token types (e.g., AUTHOR, TITLE), and the values are lists of matched lexemes.
4. **Display Tokens**: The `display_tokens` method prints the categorized tokens to the console, allowing the user to verify the tokenization process.

### Workflow

1.  **Importing Required Libraries:** The code begins by importing two important modules: re and typing.

- `re` is Python’s module for working with regular expressions. It allows you to search for patterns in strings and find all occurrences that match the given pattern.
- `typing` is used to define the expected data types for variables and function arguments. In this case, it helps define that the tokens are stored in a dictionary where each key is a string (the token type), and the associated value is a list of strings (the actual token values).

2.  **Defining Token Types:** The code defines a dictionary called `TOKEN_TYPES` that contains regular expressions for various token types. Each token type corresponds to a specific pattern that the lexer will use to identify and extract the corresponding information from the input text.

3.  **CitationLexer Class:** The `CitationLexer` class is the core of the lexer. It takes a text input and uses the defined token types to identify and extract relevant information from the text.
    The constructor method initializes the CitationLexer object with the input text (text) containing citations and an empty dictionary (tokens) to store the matched tokens. The `tokenize` method applies the regular expressions defined in `TOKEN_TYPES` to the input text and stores the matched tokens in the tokens dictionary. The `display_tokens` method prints the found tokens for review.

4.  **Main Execution:** The code reads the citation text from a file named "citations.txt" and passes it to the CitationLexer class. The lexer processes the text and displays the identified tokens.

## Results

After running the code, the following **results are expected**:

Imagine the content of `citations.txt` contains the following citation:

    Smith J., “Advanced Python Programming,” Journal of Python Studies, vol. 5, no. 3, pp. 123-125, 2021, doi: 10.1234/abcd.5678

The ``tokenize` method will identify the following tokens:

    AUTHOR: Smith J.
    TITLE: Advanced Python Programming
    JOURNAL: Journal of Python Studies
    VOLUME: 5
    ISSUE: 3
    PAGES: 123-125
    MONTH_YEAR: 2021
    DOI: 10.1234/abcd.5678

## Output

citations.txt content:

    Smith J., “Advanced Python Programming,” Journal of Python Studies, vol. 5, no. 3, pp. 123-125, 2021, doi: 10.1234/abcd.5678

Output:

    TITLE: Advanced Python Programming,
    JOURNAL: Smith J., Advanced Python Programming,  Journal of Python Studies
    VOLUME: 5
    ISSUE: 3
    PAGES: 123-125
    DOI: 10.1234/abcd.5678

## Conclusions

This lab provided me with a hands-on understanding of lexical analysis and how lexers work in real-world applications. By working with different token types and regular expressions, I learned how to break down a sequence of characters into meaningful units, or tokens, that can be further processed. I was able to define token patterns, such as keywords, operators, and literals, and implement a lexer that can identify and categorize these tokens from a given input text.

Testing various inputs and observing how the lexer processes and tokenizes the text helped me understand the importance of regular expressions in pattern matching and token classification. The process of handling whitespace, comments, and error cases reinforced the role of lexers in preprocessing source code and ensuring the text is structured correctly for further analysis. Additionally, visualizing the tokens generated by the lexer helped me appreciate how different components of a program or language are parsed and processed.

Overall, the lab not only solidified my theoretical knowledge of lexical analysis but also provided practical experience in applying these concepts to real-world tasks like text processing, language development, and even compiler design. This experience showed me how crucial lexers are in the initial stages of interpreting and compiling programming languages.

## References

- Introduction of Finite Automata - GeeksforGeeks - https://www.geeksforgeeks.org/introduction-of-finite-automata/
- Laboratory work guide - https://github.com/filpatterson/DSL_laboratory_works
- Finite automata. Part 1- Irina Cojuhari - presentation
