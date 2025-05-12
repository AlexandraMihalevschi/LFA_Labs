from lexer import *
from enum import Enum

# AST Nodes

class ASTNode:
    pass

class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"

class ShapeNode(ASTNode):
    def __init__(self, shape_type, parameters, operation=None):
        self.shape_type = shape_type
        self.parameters = parameters
        self.operation = operation

    def __repr__(self):
        return f"Shape({self.shape_type.name}, {self.parameters}, op={self.operation.name if self.operation else None})"

class FunctionCallNode(ASTNode):
    def __init__(self, func_type, argument):
        self.func_type = func_type
        self.argument = argument

    def __repr__(self):
        return f"{self.func_type.name}({self.argument})"

# Parser

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, expected_type=None):
        token = self.current_token()
        if token is None:
            return None
        if expected_type and token.type != expected_type:
            raise ValueError(f"Expected {expected_type} but got {token.type}")
        self.pos += 1
        return token

    def parse(self):
        nodes = []
        while self.current_token() is not None:
            token = self.current_token()

            if token.type in {
                TokenType.RECTANGLE, TokenType.SQUARE, TokenType.CIRCLE,
                TokenType.TRIANGLE, TokenType.PENTAGON, TokenType.TRAPEZOID
            }:
                nodes.append(self.parse_shape())

            elif token.type in {
                TokenType.SIN, TokenType.COS, TokenType.TAN,
                TokenType.COTAN, TokenType.LOG, TokenType.POW, TokenType.SQRT
            }:
                nodes.append(self.parse_math_function())

            elif token.type in {TokenType.FLOAT, TokenType.INTEGER}:
                number_token = self.eat()
                nodes.append(NumberNode(number_token.value))

            else:
                print("Unknown node type", token)
                self.pos += 1  # skip unknown

        return nodes

    def parse_shape(self):
        shape_token = self.eat()  # shape type (e.g., RECTANGLE)
        parameters = []

        # Expecting dimensions (float or int)
        while self.current_token() and self.current_token().type in {TokenType.FLOAT, TokenType.INTEGER}:
            token = self.eat()
            parameters.append(NumberNode(token.value))

        # Optional operation: area, perimeter, scale
        operation = None
        if self.current_token() and self.current_token().type in {
            TokenType.AREA, TokenType.PERIMETER, TokenType.SCALE
        }:
            op_token = self.eat()
            operation = op_token.type

            # optionally skip '=' and '?'
            if self.current_token() and self.current_token().type == TokenType.EQUALS:
                self.eat()
            if self.current_token() and self.current_token().type == TokenType.QUESTION:
                self.eat()

        return ShapeNode(shape_token.type, parameters, operation)

    def parse_math_function(self):
        func_token = self.eat()  # SIN, COS, etc.
        self.eat(TokenType.OPEN_PAREN)
        arg_token = self.eat()
        self.eat(TokenType.CLOSE_PAREN)

        if arg_token.type in {TokenType.INTEGER, TokenType.FLOAT}:
            return FunctionCallNode(func_token.type, NumberNode(arg_token.value))
        else:
            raise ValueError(f"Invalid argument for function {func_token.value}")



def main():
    text = input("Enter expression: ")
    lexer = Lexer(text)
    tokens = lexer.tokenize()
    print("Tokens:", tokens)

    parser = Parser(tokens)
    ast_nodes = parser.parse()
    print("AST:")
    for node in ast_nodes:
        print(" ", node)

if __name__ == "__main__":
    main()