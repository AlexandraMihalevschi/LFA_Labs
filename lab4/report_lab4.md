# Laboratory Work: Lexer & Scanner

**Course:** Formal Languages & Finite Automata\
**Author:** Mihalevschi Alexandra

## Theory

Lexical analysis, the process of converting a sequence of characters into a sequence of tokens, is a critical step in the compilation and interpretation of languages. A lexer (also called a scanner or tokenizer) is responsible for reading input text and dividing it into manageable chunks called tokens, which are classified into categories based on predefined rules.

Lexical analysis is essential in understanding how programming languages function. It ensures that the source code adheres to a defined syntax by breaking it into recognizable components, which are later used for further compilation or interpretation. Without lexical analysis, processing raw source code would be significantly more complex, making it difficult to develop structured and efficient programming languages.

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

Lexers are used in a wide range of applications beyond just compilers and interpreters:

1.  **Compilers:** In a compiler, the lexer is the first phase of the front end, responsible for converting source code into a series of tokens that can be passed to the parser. The lexer helps the parser understand the structure of the code by providing a well-defined sequence of tokens.

2.  **Interpreters:** Similar to compilers, interpreters use lexers to process source code and generate tokens. However, instead of compiling the code into machine code, interpreters execute it directly, interpreting each token at runtime.

3.  **Text Processing Tools:** Lexers are widely used in text processing applications such as search engines, syntax highlighting, and data extraction tools. For instance, a lexer can be used to tokenize a structured text file (like an XML or JSON document) for easier parsing and manipulation.

4.  **Language Development:** When designing a new programming language or domain-specific language (DSL), a lexer is essential for processing the language's syntax. It enables the identification and categorization of key elements in the language, such as keywords, operators, and literals, before further analysis by the parser.

5.  **Data Parsing:** Lexers can be used in data parsing tasks, where structured data (such as log files, configuration files, or structured text) is tokenized and analyzed for further processing or conversion to other formats.

#### Lookahead and Backtracking in Lexers

One important feature of lexers is the ability to look ahead at the upcoming characters in the input text to make better decisions during tokenization. Lookahead allows the lexer to handle more complex tokenization tasks that require knowledge of future characters, such as distinguishing between keywords and identifiers. In many programming languages, certain sequences of characters may appear as both valid keywords and identifiers, so the lexer must decide whether a given lexeme is a keyword or an identifier based on the context in which it appears.

For example, in the expression `if(x > 10)`, the if keyword must be recognized as a keyword and not as an identifier. To handle such scenarios, the lexer may use a one-character or multi-character lookahead, allowing it to inspect characters ahead of the current position in the input text before deciding on the appropriate token.

However, lookahead is not without trade-offs. It can introduce additional complexity and processing overhead, especially when a large number of lookahead characters are required. This is one of the reasons why efficient lexers often rely on finite automata, which allow for fast transitions and reduce the need for extensive lookahead.

In some cases, backtracking might also be necessary. Backtracking allows the lexer to "undo" previous decisions and try different tokenization paths when it encounters ambiguities or incorrect assumptions. While powerful, backtracking can lead to performance inefficiencies, so it is typically reserved for complex lexing tasks that cannot be handled by simpler methods.

#### Context-Sensitive Tokenization

In many languages, tokenization is not a purely syntactic process; it may depend on the surrounding context. This type of context-sensitive tokenization allows the lexer to distinguish between different interpretations of similar-looking lexemes. For example, in many programming languages, the same sequence of characters can have different meanings based on the context in which it appears. For instance:

In a string literal, the sequence `+` may represent a concatenation operator, but in mathematical expressions, `+` represents addition.

A sequence like `//` may represent a comment when it appears at the beginning of a line, but when used within certain constructs, it may be part of an identifier or operator.

Context-sensitive tokenization requires that the lexer maintains additional state information as it processes the input, tracking whether certain constructs (such as a string literal, comment, or number) are currently active. This context-awareness adds complexity to the lexer but allows it to handle the nuances of real-world programming languages.

#### Optimizations in Lexers

One of the primary goals of lexical analysis is to tokenize input text efficiently, particularly for large programs or data files. To optimize the lexing process, several techniques can be employed:

1. Minimizing Backtracking: By designing token patterns that are as unambiguous as possible, a lexer can reduce or eliminate the need for backtracking. For instance, placing more specific patterns before less specific ones ensures that the lexer matches the longest possible token first.

2. Input Buffering: Many lexers use input buffering techniques to optimize reading and processing the input text. The input text is stored in a buffer, allowing the lexer to quickly access characters without repeatedly reading from a file or source. Techniques like double-buffering (two buffers) allow for smooth processing even when large portions of input are being read and processed concurrently.

3. Efficient State Transitions: Finite automata are an efficient way to represent tokenization patterns. By constructing a deterministic finite automaton (DFA) for each token type, the lexer can achieve constant-time state transitions for each input character. While constructing the DFA can be computationally expensive, once it is constructed, the lexer can quickly tokenize input in a linear pass.

4. Prefix Tables: Some lexers use prefix tables to optimize common prefix matching. For instance, if a lexer encounters the beginning of an identifier that matches a common pattern (such as a keyword or operator), it can quickly match the prefix and avoid unnecessary checks against all possible token patterns.

#### Conclusion

A lexer plays an indispensable role in converting raw input text into structured tokens that can be easily processed by subsequent stages of a compiler or interpreter. By understanding and implementing lexical analysis, one gains insight into how programming languages and data formats are parsed and processed. Regular expressions, finite automata, and efficient error handling are core concepts that enable lexers to function effectively.

## Objectives

The primary objectives of this laboratory work were:

1. To understand the concept of lexical analysis.
2. To become familiar with how a lexer/scanner/tokenizer functions internally.
3. To implement a sample lexer for processing a structured text format (citations in this case) and demonstrate how the lexer works.
   In addition to the theoretical understanding, the practical component focused on developing a lexer capable of identifying various citation components, such as author names, publication titles, journals, volumes, pages, dates, DOIs, and conference details.

## Implementation Description

The provided code is a Python implementation of a lexer (tokenizer) for a structured text format. The lexer is designed to recognize and tokenize various constructs from the input string, such as numbers, mathematical operations, shapes, and mathematical functions.

This code defines a lexer (or tokenizer) that breaks down an input string into a series of tokens. It handles a variety of constructs such as numbers, mathematical operations, shapes, and mathematical functions like sin(), cos(), log(), and others. The lexer recognizes these constructs from the input string and converts them into tokens that can later be used for further processing, such as evaluating expressions or performing calculations.

### Core Components:

The core components of the code include:

1.  **Token Class**: A class to represent a token with a specific type and value.
2.  **Lexer Class**: The main lexer that scans the input string and generates tokens.
3.  **Math Functions and Shapes**: The lexer is capable of recognizing specific math functions (such as sin, cos, log, etc.) and geometric shapes (such as rectangle, circle, etc.).
4.  **Main Function**: The entry point of the code, which takes an input string, processes it through the lexer, and prints the resulting tokens.

---

### Classes and Methods

#### 1\. **Token Class**

The `Token` class is a simple structure that holds information about a token. Each token consists of:

- **type**: A string that represents the type of the token (e.g., INTEGER, FLOAT, PLUS, MINUS, etc.).
- **value**: The actual value of the token, which could be a number (e.g., 10, 2.5) or a string representing the function/operation (e.g., sin, cos, area, etc.).

```python
class Token:
    def __init__(self, type, value):
        self.type = type
    self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"`
```

#### 2\. **Lexer Class**

The `Lexer` class is the core of the lexer functionality. It is responsible for scanning the input text, identifying different components, and returning corresponding tokens.

**Attributes:**

- **text**: The input string that the lexer will tokenize.
- **pos**: The current position of the lexer within the input string.
- **current_char**: The current character being processed in the string.

**Methods:**

- **advance()**: Moves the lexer to the next character in the input string.
- **skip_whitespace()**: Skips any whitespace characters in the input.
- **number()**: Recognizes numbers (integers, floats, and imaginary numbers) from the input string.
- **shape()**: Recognizes geometric shape names from the input.
- **operation()**: Recognizes operations such as area, perimeter, and scale.
- **math_function()**: Recognizes mathematical functions such as sin, cos, log, pow, sqrt, etc.
- **get_next_token()**: The main method of the lexer that processes the input and returns corresponding tokens.

```python
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def number(self):
        result = ''
        is_float = False
        is_imaginary = False

        while self.current_char is not None and (self.current_char.isdigit() or self.current_char in '.i'):
            if self.current_char == '.':
                is_float = True
            elif self.current_char == 'i':
                is_imaginary = True
                self.advance()
                break  # Stop parsing further, as 'i' should be at the end of a number

            result += self.current_char
            self.advance()

        if is_imaginary:
            return Token("IMAGINARY", complex(0, float(result)))  # Convert "2i" into complex(0,2)
        elif is_float:
            return Token("FLOAT", float(result))
        else:
            return Token("INTEGER", int(result))

    def shape(self):
        shapes = ["rectangle", "square", "circle", "triangle", "pentagon", "trapezoid"]
        for shape in shapes:
            if self.text[self.pos:self.pos + len(shape)] == shape:
                self.pos += len(shape)
                self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
                return Token(shape.upper(), shape)
        return None

    def operation(self):
        operations = ["area", "perimeter", "scale"]
        for op in operations:
            if self.text[self.pos:self.pos + len(op)] == op:
                self.pos += len(op)
                self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
                return Token(op.upper(), op)
        return None

    def math_function(self):
        functions = ["sin", "cos", "tan", "cotan", "log", "pow", "sqrt"]
        for func in functions:
            if self.text[self.pos:self.pos + len(func)] == func:
                self.pos += len(func)
                self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
                return Token(func.upper(), func)
        return None

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char == ':':  # Handle colon as a token separator
                self.advance()
                continue

            if self.current_char == '?':  # Handle the question mark
                self.advance()
                return Token("QUESTION", '?')

            if self.current_char == '=':  # Handle the equal sign as a token
                self.advance()
                return Token("EQUALS", '=')

            if self.current_char.isdigit() or self.current_char in '.i':
                return self.number()

            if self.current_char.isalpha():
                shape_token = self.shape()
                if shape_token:
                    return shape_token

                operation_token = self.operation()
                if operation_token:
                    return operation_token

                math_func_token = self.math_function()
                if math_func_token:
                    return math_func_token

            operators = {'+': "PLUS", '-': "MINUS", '*': "MULTIPLY", '/': "DIVIDE"}
            if self.current_char in operators:
                token = Token(operators[self.current_char], self.current_char)
                self.advance()
                return token

            # Handle opening parenthesis for functions like sin(), cos(), etc.
            if self.current_char == '(':
                self.advance()
                return Token("OPEN_PAREN", '(')

            # Handle closing parenthesis for functions like sin(), cos(), etc.
            if self.current_char == ')':
                self.advance()
                return Token("CLOSE_PAREN", ')')

            raise ValueError(f"Invalid character: {self.current_char}")

        return None
```

#### 3\. **Main**

The `main()` function serves as the entry point of the program. It interacts with the user to get an input string and then processes it through the lexer. The process includes:

- Prompting the user to enter a string (e.g., `rectangle: 2.5 5.8 area=? sin(45) log(2)`).
- Passing the input string to the `Lexer` class.
- Iterating through the tokens generated by the lexer and printing them out.

---

### Detailed Functionality

#### Handling Numbers:

- The lexer handles both integer and floating-point numbers by reading the digits and checking for a decimal point (`.`). If it encounters an imaginary unit (`i`), it recognizes the number as a complex number (e.g., `3i` is treated as `complex(0, 3)`).

#### Recognizing Mathematical Functions:

- The lexer recognizes standard mathematical functions like `sin`, `cos`, `log`, `pow`, `sqrt` from the input string. It checks for the presence of these function names and, upon recognizing them, returns the corresponding token.

#### Recognizing Shapes:

- Geometric shapes like `rectangle`, `circle`, `square`, `triangle`, etc., are identified by the lexer. The lexer compares substrings from the input with a predefined list of shapes. If a match is found, it returns a token with the corresponding shape type.

#### Recognizing Operations:

- The lexer recognizes operations like `area`, `perimeter`, and `scale`, which are commonly associated with shapes in geometry or calculations.

#### Handling Operators:

- The lexer handles basic mathematical operators such as `+`, `-`, `*`, and `/` by checking if the current character in the input matches any of these symbols.

#### Parentheses:

- The lexer handles parentheses, which are commonly used in mathematical functions like `sin(45)` or `log(2)`. It returns tokens for opening parentheses (`OPEN_PAREN`) and closing parentheses (`CLOSE_PAREN`) to mark the start and end of function arguments.

#### Error Handling:

- The lexer raises a `ValueError` if it encounters an invalid character in the input string, ensuring that any unexpected characters are flagged during the tokenization

#### Using `re`, `cmath`, and `math` in the Lexer

Using `re`, `cmath`, and `math` provided me several advantages:

1. **`re` (Regular Expressions):**

   - Regular expressions allow efficient pattern matching to identify different token types (e.g., keywords, operators, numbers, identifiers).
   - Using regex simplifies the lexer, as a single regex pattern can match multiple tokens instead of manually checking each character.
   - Example: `re.findall(r'\d+|\w+|[+\-*/]', source_code)` can extract numbers, words, and operators efficiently.

2. **`cmath` (Complex Math):**

   - If your lexer or language needs to handle complex numbers, `cmath` is essential.
   - Unlike `math`, `cmath` supports operations on complex numbers, which are useful to find the complex numbers if the users add them.

3. **`math` (Mathematical Functions):**
   - The `math` module provides functions like `log`, `sqrt`, and `sin`, which are useful if your lexer needs to process mathematical expressions.
   - If your language has built-in functions (like `sin(30)`), using `math` allows direct evaluation of expressions without reinventing trigonometric calculations.

### Why Is This a Better Approach?

- **Efficiency:** Regex (`re`) speeds up token recognition instead of manually iterating through characters.
- **Readability:** Using standard modules like `re`, `math`, and `cmath` keeps the lexer clean and understandable.
- **Built-in Support:** Python’s built-in libraries are optimized, reducing the need to manually implement math functions or complex number handling.

## Expected Results

When running this lexer code, the expected result is that the input string will be tokenized into a sequence of meaningful tokens, each representing a distinct element of the input. The lexer processes numbers, operations, functions, shapes, parentheses, and special characters, converting them into tokens that can be further analyzed or evaluated.

For numbers, the lexer will correctly identify integers, floating-point numbers, and complex numbers. For example, the input `2`, `2.5`, and `3i` will be tokenized as `Token(INTEGER, 2)`, `Token(FLOAT, 2.5)`, and `Token(IMAGINARY, complex(0, 3))` respectively. If the input contains mathematical functions like `sin()`, `cos()`, `log()`, or others, these will be recognized as well. For instance, `sin(45)` will produce the tokens `Token(SIN, 'sin')`, `Token(OPEN_PAREN, '(')`, `Token(INTEGER, 45)`, and `Token(CLOSE_PAREN, ')')`.

Geometric shapes such as `rectangle`, `circle`, and `triangle` are also recognized and tokenized, with inputs like `rectangle` generating the token `Token(RECTANGLE, 'rectangle')`. Similarly, if the input includes operations such as `area`, `perimeter`, or `scale`, these will be tokenized as well, like `Token(AREA, 'area')`.

The lexer also handles basic operators like `+`, `-`, `*`, and `/`, recognizing them as `Token(PLUS, '+')`, `Token(MINUS, '-')`, and so on. Parentheses are treated as individual tokens, with `(` and `)` being tokenized as `Token(OPEN_PAREN, '(')` and `Token(CLOSE_PAREN, ')')`.

Special characters like colons (`:`), equal signs (`=`), and question marks (`?`) are also tokenized, so `:` becomes `Token(COLON, ':')`, `=` is tokenized as `Token(EQUALS, '=')`, and `?` as `Token(QUESTION, '?')`.

If the lexer encounters any invalid characters that don't match known token types, it will raise a `ValueError` to signal an error. For example, an invalid character like `@` would trigger a `ValueError: Invalid character: @`.

## Output

Input:

    Enter your input (e.g., 'rectangle: 2.5 5.8 area=? sin(45) log(2)'): rectangle: 5i 10.23 area=? sin(30) cos(60*2) log(10/23)

Output:

    Tokens: [Token(RECTANGLE, 'rectangle'), Token(IMAGINARY, 5j), Token(FLOAT, 10.23), Token(AREA, 'area'), Token(EQUALS, '='), Token(QUESTION, '?'), Token(SIN, 'sin'), Token(OPEN_PAREN, '('), Token(INTEGER, 30), Token(CLOSE_PAREN, ')'), Token(COS, 'cos'), Token(OPEN_PAREN, '('), Token(INTEGER, 60), Token(MULTIPLY, '*'), Token(INTEGER, 2), Token(CLOSE_PAREN, ')'), Token(LOG, 'log'), Token(OPEN_PAREN, '('), Token(INTEGER, 10), Token(DIVIDE, '/'), Token(INTEGER, 23), Token(CLOSE_PAREN, ')')]

## Conclusions

This lab provided me with a hands-on understanding of lexical analysis and how lexers work in real-world applications. By working with different token types and regular expressions, I learned how to break down a sequence of characters into meaningful units, or tokens, that can be further processed. I was able to define token patterns, such as keywords, operators, and literals, and implement a lexer that can identify and categorize these tokens from a given input text.

Testing various inputs and observing how the lexer processes and tokenizes the text helped me understand the importance of regular expressions in pattern matching and token classification. The process of handling whitespace, comments, and error cases reinforced the role of lexers in preprocessing source code and ensuring the text is structured correctly for further analysis. Additionally, visualizing the tokens generated by the lexer helped me appreciate how different components of a program or language are parsed and processed.

Overall, the lab not only solidified my theoretical knowledge of lexical analysis but also provided practical experience in applying these concepts to real-world tasks like text processing, language development, and even compiler design. This experience showed me how crucial lexers are in the initial stages of interpreting and compiling programming languages.

## References

- Laboratory work guide - https://github.com/filpatterson/DSL_laboratory_works
- Python documentation - https://docs.python.org/3/
- Tutorial on lexer in Python - https://medium.com/@pythonmembers.club/building-a-lexer-in-python-a-tutorial-3b6de161fe84
