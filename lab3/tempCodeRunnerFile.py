import re
import cmath
import math

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

# Example usage
def main():
    text = input("Enter your input (e.g., 'rectangle: 2.5 5.8 area=? sin(45) log(2)'): ")
    lexer = Lexer(text)

    tokens = []
    token = lexer.get_next_token()
    while token is not None:
        tokens.append(token)
        token = lexer.get_next_token()

    print("Tokens:", tokens)

if __name__ == "__main__":
    main()
