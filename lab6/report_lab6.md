# Laboratory Work: Parser & Building an Abstract Syntax Tree

**Course:** Formal Languages & Finite Automata  
**Author:** Mihalevschi Alexandra

## Theory

Parsing is the process of analyzing a sequence of symbols (typically text) to determine its grammatical structure according to a given formal grammar. In programming language theory and compiler design, parsing transforms a linear sequence of tokens into a structured representation, often in the form of a parse tree or an abstract syntax tree (AST). The parser plays a critical role in compiling or interpreting source code by identifying syntactic constructs like expressions, statements, loops, and declarations. Parsing can be done using various algorithms, such as recursive descent, LL, or LR parsing, depending on the complexity and structure of the grammar.

An essential preliminary step to parsing is **lexical analysis**, where the input text is divided into tokens—basic meaningful units such as keywords, identifiers, operators, or punctuation. These tokens are typically categorized using a `TokenType` enum or similar construct. Regular expressions are widely used in this stage to match patterns in the text and assign appropriate token types. For instance, a regular expression like `[a-zA-Z_][a-zA-Z0-9_]*` might be used to identify identifiers, while `\d+` could match numeric literals. This classification simplifies the job of the parser by providing a clean sequence of syntactically meaningful elements.

Once tokens are generated, parsing proceeds to generate a **parse tree** or more abstractly, an **Abstract Syntax Tree (AST)**. Unlike the parse tree, which represents every detail of the syntax including punctuation and hierarchy defined by the grammar, the AST omits unnecessary syntactic details to focus on the structural and semantic content of the code. This simplification is beneficial in later stages such as semantic analysis, optimization, or code generation. For instance, a binary expression like `3 + 5` would be represented in an AST with a root node for `+`, and child nodes `3` and `5`.

The design of an AST requires defining appropriate data structures that reflect the kinds of constructs the parser is expected to handle. For example, an expression node might have fields for an operator and its left and right operands, while a function node might contain a name, parameters, and a body. These nodes are usually implemented as classes or records, often forming a tree-like hierarchy where each subclass corresponds to a specific syntactic construct. This kind of structural abstraction allows for recursive processing of code constructs and enables easier manipulation and transformation of the program representation.

In the context of this laboratory task, extending the third lab’s work would involve introducing a `TokenType` enumeration to categorize tokens identified during lexical analysis. This will be used in combination with regular expressions to systematically scan and classify the input text. Following this, a simple parser should be implemented that reads the list of tokens and builds the corresponding AST. The parser can be implemented manually using recursive functions or pattern matching, which process tokens according to grammar rules and construct the appropriate AST nodes.

Overall, the practice of building a tokenizer, defining a `TokenType`, and constructing an AST forms the foundation of many programming tools including interpreters, compilers, linters, and even code formatters. Understanding how to parse and represent the syntactic and semantic structure of code enables the creation of tools that can analyze, transform, or execute programs. It also deepens one’s understanding of how programming languages are understood by computers and lays the groundwork for more advanced compiler construction concepts.

Building upon the foundation of lexical analysis, parsing, and AST construction, it is crucial to understand the underlying grammar that governs the structure of the language or data being parsed. Grammars are usually expressed in forms such as Backus-Naur Form (BNF) or Extended BNF (EBNF), which formally define how tokens can be combined to form valid statements and expressions. These grammars consist of rules with non-terminal symbols that describe how higher-level constructs are built from simpler ones, and terminal symbols that correspond to actual tokens identified by the lexer. A parser operates by applying these rules to validate the structure of input and to guide the construction of the parse tree or AST.

There are two main types of parsers: **top-down** and **bottom-up** parsers. Top-down parsers, such as recursive descent parsers, begin analysis from the start symbol of the grammar and attempt to derive the input tokens by applying production rules. These are relatively easier to implement by hand and work well with simpler, LL(1) grammars. Bottom-up parsers, like those used in LR parsing, work in the opposite direction by recognizing input tokens and reducing them to non-terminals using grammar rules, eventually reaching the start symbol. These are more powerful and can handle more complex grammars but are often generated using parser generators such as YACC, Bison, or ANTLR.

In practical programming environments, the AST is often enriched with semantic information, such as variable types, scope details, or evaluation results. This transformation from syntax to semantics is a critical phase known as **semantic analysis**, which follows parsing in the compilation pipeline. For instance, after building the AST, the compiler might perform type checking to ensure that operations are semantically valid (e.g., not adding a string to an integer unless allowed). These semantic annotations make the AST a powerful representation not only for analyzing correctness but also for later stages like optimization and code generation.

Moreover, the design of the AST can be influenced by the desired operations to be performed on it. In many implementations, the **Visitor design pattern** is used to traverse and process AST nodes in a flexible way. Each node in the AST implements an interface that accepts a visitor object, allowing operations such as pretty-printing, interpretation, or code generation to be separated from the data structure itself. This modular design allows for reusability and extensibility, especially in tools that support multiple analyses or transformations over the same syntactic structure.

Lastly, parsing and AST construction are not limited to compilers—they are also foundational in many other domains of software engineering. For example, Integrated Development Environments (IDEs) use them to provide features such as syntax highlighting, code completion, and refactoring. Static analyzers and linters use ASTs to enforce coding standards and detect potential bugs. Even applications like custom configuration file processors, domain-specific languages, or automated code transformers rely on parsing techniques. By mastering the concepts of lexical analysis, parsing, and AST construction, developers gain access to a wide array of powerful tools for program understanding, transformation, and automation.

## Objectives

The primary objectives of this laboratory work were:

1.  Get familiar with parsing, what it is and how it can be programmed [1].
2.  Get familiar with the concept of AST [2].
3.  In addition to what has been done in the 3rd lab work do the following:
    1.  In case you didn't have a type that denotes the possible types of tokens you need.
    2.  Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
    3.  Implement a simple parser program that could extract the syntactic information from the input text.

## Implementation Description

The Parser class in the implementation plays a crucial role in the compilation process by transforming the flat sequence of tokens produced by the lexer into a structured Abstract Syntax Tree (AST). This class is responsible for analyzing the syntactic structure of the input according to the grammar rules of our language, ensuring that the tokens follow valid patterns and relationships.

The Parser works by implementing a recursive descent parsing algorithm, which processes tokens in a top-down manner, starting with high-level language constructs and breaking them down into their constituent parts. It maintains internal state including the current position in the token stream and the current token being processed, allowing it to navigate through the input methodically.

When parsing, the class recognizes different types of language constructs such as shape definitions (rectangles, circles, etc.), mathematical expressions, function calls, and operations on shapes. For each recognized construct, it creates appropriate AST nodes that capture not just the individual tokens but their semantic relationships and hierarchical structure.

The resulting AST serves as an intermediate representation that preserves the meaning of the original input while organizing it in a way that facilitates further processing, such as semantic analysis, optimization, or code generation. This tree structure makes it much easier to reason about and manipulate the program compared to the flat token sequence.

Specialized Geometric and Mathematical Processing
The parser is specifically designed to handle a domain-specific language focused on geometric shapes and mathematical operations. It can process:

Shape Definitions: The parser recognizes various geometric shapes (rectangle, square, circle, triangle, pentagon, trapezoid) along with their dimensional parameters, creating structured representations that capture both the shape type and its defining measurements.

Shape Operations: Operations like area calculation, perimeter computation, and scaling are parsed into operation nodes that link the operation type with the target shape, preserving the relationship between shapes and the operations performed on them.

Mathematical Expressions: The parser handles complex mathematical expressions including arithmetic operations, function calls (sin, cos, tan, log, etc.), and supports various number types (integers, floating-point, and imaginary numbers).

Queries and Assignments: The language supports both querying properties (e.g., "area=?") and assigning values, which the parser differentiates and represents appropriately in the AST.

The AST is built using a hierarchy of node classes that represent different language constructs:

1. NumberNode: Represents numeric literals (integers, floats, complex numbers)
2. BinOpNode: Represents binary operations like addition and multiplication
3. UnaryOpNode: Represents unary operations like negation
4. FunctionCallNode: Represents mathematical function calls with their arguments
5. ShapeNode: Represents geometric shapes with their dimensions
6. OperationNode: Represents operations performed on shapes
   This node hierarchy allows the parser to capture the full semantic structure of the input, making it possible to perform complex operations on geometric shapes and evaluate mathematical expressions in a structured and type-safe manner.

By separating syntactic analysis from lexical analysis, the Parser completes the second major phase of the front-end compilation process, transforming raw tokens into a structured representation that captures the grammatical relationships between different elements of the program, particularly focusing on geometric and mathematical concepts.

### Overview

The parser takes tokens generated by a lexer and constructs an Abstract Syntax Tree (AST) representing the input. The AST consists of nodes for numbers, shapes, and mathematical function calls. The parser uses a recursive descent approach to parse the input tokens and build the AST. The parser handles various shape types, including rectangle, circle, and triangle, and supports mathematical functions like addition, subtraction, multiplication, and division. The parser also handles errors such as invalid shape types, missing parameters, and invalid function arguments. The parser also includes error handling for invalid function arguments and missing parameters.

### AST Node Classes

### Base Node

```python
class ASTNode:
    pass
```

### Number Node

Represents numeric values (integers or floats).

```python
class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value
```

### Shape Node

Represents geometric shapes with optional operations.

```python
class ShapeNode(ASTNode):
    def __init__(self, shape_type, parameters, operation=None):
        self.shape_type = shape_type
        self.parameters = parameters  # List of NumberNodes
        self.operation = operation    # Optional: AREA, PERIMETER, SCALE
```

### Function Call Node

Represents mathematical function calls.

```python
class FunctionCallNode(ASTNode):
    def __init__(self, func_type, argument):
        self.func_type = func_type   # SIN, COS, TAN, etc.
        self.argument = argument     # NumberNode
```

### Parser Implementation

The Parser class in the implementation plays a crucial role in the compilation process by transforming the flat sequence of tokens produced by the lexer into a structured Abstract Syntax Tree (AST). This class is responsible for analyzing the syntactic structure of the input according to the grammar rules of our language, ensuring that the tokens follow valid patterns and relationships. The `Parser` class processes tokens and builds the AST:

### Key Methods

1. **Initialization**

   ```python
   def __init__(self, tokens):
       self.tokens = tokens
       self.pos = 0
   ```

2. **Token Consumption**

   ```python
   def current_token(self)
   def eat(self, expected_type=None)
   ```

3. **Main Parsing**

   ```python
   def parse(self)
   ```

4. **Shape Parsing**

   ```python
   def parse_shape(self)
   ```

5. **Function Parsing**
   ```python
   def parse_math_function(self)
   ```

### Parsing Logic

1. The parser processes tokens sequentially, creating appropriate AST nodes:

   - Numbers become `NumberNode`
   - Shape keywords become `ShapeNode` with parameters
   - Math functions become `FunctionCallNode`

2. Shape nodes can have optional operations (area, perimeter, scale)

3. The parser handles simple mathematical functions with single numeric arguments

### Example Usage

```python
text = "rectangle 3 4 area"
lexer = Lexer(text)
tokens = lexer.tokenize()
parser = Parser(tokens)
ast_nodes = parser.parse()
```

Would produce an AST containing:

```
Shape(RECTANGLE, [Number(3), Number(4)], op=AREA)
```

### Error Handling

The parser includes basic error checking:

- Verifies expected token types
- Handles malformed input by skipping unknown tokens
- Validates function arguments are numeric

## Expected Results

The expected results of running this code are as follows: The user inputs a mathematical expression, and the program evaluates it using the Shunting Yard algorithm and the AST. The output is the result of the evaluation.

## Output

The output of the program will be the result of the evaluation of the mathematical expression.

Input and output:

```
Enter expression: rectangle: 2.5 5.8 area=? sin(45) log(2)

Tokens: [Token(TokenType.RECTANGLE, 'rectangle'), Token(TokenType.FLOAT, 2.5), Token(TokenType.FLOAT, 5.8), Token(TokenType.AREA, 'area'), Token(TokenType.EQUALS, '='), Token(TokenType.QUESTION, '?'), Token(TokenType.SIN, 'sin'), Token(TokenType.OPEN_PAREN, '('), Token(TokenType.INTEGER, 45), Token(TokenType.CLOSE_PAREN, ')'), Token(TokenType.LOG, 'log'), Token(TokenType.OPEN_PAREN, '('), Token(TokenType.INTEGER, 2), Token(TokenType.CLOSE_PAREN, ')')]
AST:
  Shape(RECTANGLE, [Number(2.5), Number(5.8)], op=AREA)
  SIN(Number(45))
  LOG(Number(2))
```

![Geometric Shapes](/output/screen1.png)

## Conclusions

This laboratory work has successfully implemented a comprehensive lexical analyzer and parser for a domain-specific language focused on geometric shapes and mathematical operations. The implementation demonstrates a practical application of formal language theory and compiler design principles.

The lexer component was enhanced to use regular expressions for token identification, making the pattern matching process more robust and maintainable. This approach allows for clearer token type categorization and easier extension of the language in the future. The TokenType enumeration provides a well-structured way to categorize different elements of the language, from basic arithmetic operators to specialized geometric shapes and mathematical functions.

The parser implementation transforms the flat sequence of tokens into a hierarchical Abstract Syntax Tree (AST), capturing the semantic relationships between different language constructs. This transformation is crucial for understanding and processing the meaning of the input beyond its syntactic structure. The recursive descent parsing technique employed in this work demonstrates how complex language structures can be broken down into manageable parsing functions.

The AST structure designed for this language effectively represents various language constructs including:

- Numeric literals and arithmetic expressions
- Geometric shapes with their dimensions
- Operations on shapes such as area and perimeter calculations
- Mathematical function calls with their arguments
- Queries and assignments
  This laboratory work bridges theoretical concepts with practical implementation, showing how formal language processing can be applied to create a specialized language for geometric and mathematical computations. The modular design of the lexer and parser components follows good software engineering practices, making the code maintainable and extensible.

Through this implementation, we've demonstrated the complete front-end pipeline of a compiler or interpreter, from character-level analysis to the creation of a structured representation that captures the meaning of the program. This foundation could be extended in future work to include semantic analysis, optimization, and execution of the represented operations.

## References

- Laboratory work guide - [https://github.com/filpatterson/DSL_laboratory_works](https://github.com/filpatterson/DSL_laboratory_works)
- Python documentation - [https://docs.python.org/3/](https://docs.python.org/3/)
- Documentation on re module in Python - [https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)
