from enum import Enum, auto
import re
import cmath
import math

class TokenType(Enum):
    INTEGER = auto()
    FLOAT = auto()
    IMAGINARY = auto()
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    EQUALS = auto()
    QUESTION = auto()
    OPEN_PAREN = auto()
    CLOSE_PAREN = auto()

    # Shapes
    RECTANGLE = auto()
    SQUARE = auto()
    CIRCLE = auto()
    TRIANGLE = auto()
    PENTAGON = auto()
    TRAPEZOID = auto()

    # Operations
    AREA = auto()
    PERIMETER = auto()
    SCALE = auto()

    # Math functions
    SIN = auto()
    COS = auto()
    TAN = auto()
    COTAN = auto()
    LOG = auto()
    POW = auto()
    SQRT = auto()


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None
        
        # Define regex patterns for token types
        self.patterns = [
            (TokenType.FLOAT, r'\d+\.\d+'),
            (TokenType.IMAGINARY, r'\d+(\.\d+)?i'),
            (TokenType.INTEGER, r'\d+'),
            (TokenType.PLUS, r'\+'),
            (TokenType.MINUS, r'-'),
            (TokenType.MULTIPLY, r'\*'),
            (TokenType.DIVIDE, r'/'),
            (TokenType.EQUALS, r'='),
            (TokenType.QUESTION, r'\?'),
            (TokenType.OPEN_PAREN, r'\('),
            (TokenType.CLOSE_PAREN, r'\)'),
            # Shapes
            (TokenType.RECTANGLE, r'rectangle'),
            (TokenType.SQUARE, r'square'),
            (TokenType.CIRCLE, r'circle'),
            (TokenType.TRIANGLE, r'triangle'),
            (TokenType.PENTAGON, r'pentagon'),
            (TokenType.TRAPEZOID, r'trapezoid'),
            # Operations
            (TokenType.AREA, r'area'),
            (TokenType.PERIMETER, r'perimeter'),
            (TokenType.SCALE, r'scale'),
            # Math functions
            (TokenType.SIN, r'sin'),
            (TokenType.COS, r'cos'),
            (TokenType.TAN, r'tan'),
            (TokenType.COTAN, r'cotan'),
            (TokenType.LOG, r'log'),
            (TokenType.POW, r'pow'),
            (TokenType.SQRT, r'sqrt'),
        ]

    def tokenize(self):
        tokens = []
        pos = 0
        
        while pos < len(self.text):
            # Skip whitespace and colons
            match = re.match(r'[ \t\n:]+', self.text[pos:])
            if match:
                pos += match.end()
                continue
                
            # Try to match a token
            matched = False
            for token_type, pattern in self.patterns:
                regex = re.compile(pattern)
                match = regex.match(self.text[pos:])
                
                if match:
                    value = match.group(0)
                    
                    # Convert value based on token type
                    if token_type == TokenType.INTEGER:
                        value = int(value)
                    elif token_type == TokenType.FLOAT:
                        value = float(value)
                    elif token_type == TokenType.IMAGINARY:
                        # Remove 'i' and convert to complex
                        num = value[:-1]  # Remove 'i'
                        value = complex(0, float(num))
                    
                    tokens.append(Token(token_type, value))
                    pos += match.end()
                    matched = True
                    break
            
            if not matched:
                raise ValueError(f"Invalid token at position {pos}: '{self.text[pos:]}'")
        
        return tokens

    # Keep the old methods for backward compatibility
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
            return Token(TokenType.IMAGINARY, complex(0, float(result)))  # Convert "2i" into complex(0,2)
        elif is_float:
            return Token(TokenType.FLOAT, float(result))
        else:
            return Token(TokenType.INTEGER, int(result))

    def shape(self):
        shapes = {
            "rectangle": TokenType.RECTANGLE,
            "square": TokenType.SQUARE,
            "circle": TokenType.CIRCLE,
            "triangle": TokenType.TRIANGLE,
            "pentagon": TokenType.PENTAGON,
            "trapezoid": TokenType.TRAPEZOID
        }
        
        for shape, token_type in shapes.items():
            if self.text[self.pos:self.pos + len(shape)] == shape:
                self.pos += len(shape)
                self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
                return Token(token_type, shape)
        return None

    def operation(self):
        operations = {
            "area": TokenType.AREA,
            "perimeter": TokenType.PERIMETER,
            "scale": TokenType.SCALE
        }
        
        for op, token_type in operations.items():
            if self.text[self.pos:self.pos + len(op)] == op:
                self.pos += len(op)
                self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
                return Token(token_type, op)
        return None

    def math_function(self):
        functions = {
            "sin": TokenType.SIN,
            "cos": TokenType.COS,
            "tan": TokenType.TAN,
            "cotan": TokenType.COTAN,
            "log": TokenType.LOG,
            "pow": TokenType.POW,
            "sqrt": TokenType.SQRT
        }
        
        for func, token_type in functions.items():
            if self.text[self.pos:self.pos + len(func)] == func:
                self.pos += len(func)
                self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
                return Token(token_type, func)
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
                return Token(TokenType.QUESTION, '?')

            if self.current_char == '=':  # Handle the equal sign as a token
                self.advance()
                return Token(TokenType.EQUALS, '=')

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

            operators = {
                '+': TokenType.PLUS, 
                '-': TokenType.MINUS, 
                '*': TokenType.MULTIPLY, 
                '/': TokenType.DIVIDE
            }
            
            if self.current_char in operators:
                token = Token(operators[self.current_char], self.current_char)
                self.advance()
                return token

            # Handle opening parenthesis for functions like sin(), cos(), etc.
            if self.current_char == '(':
                self.advance()
                return Token(TokenType.OPEN_PAREN, '(')

            # Handle closing parenthesis for functions like sin(), cos(), etc.
            if self.current_char == ')':
                self.advance()
                return Token(TokenType.CLOSE_PAREN, ')')

            raise ValueError(f"Invalid character: {self.current_char}")

        return None

# Example usage
def main():
    text = input("Enter your input (e.g., 'rectangle: 2.5 5.8 area=? sin(45) log(2)'): ")
    lexer = Lexer(text)

    # Use the new regex-based tokenizer
    tokens = lexer.tokenize()
    print("Tokens:", tokens)

if __name__ == "__main__":
    main()
