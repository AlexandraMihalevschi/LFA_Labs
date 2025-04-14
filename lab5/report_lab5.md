# Laboratory Work: Chomsky Normal Form

**Course:** Formal Languages & Finite Automata\
**Author:** Mihalevschi Alexandra

## Theory

Chomsky Normal Form (CNF) is an important representation of context-free grammars used in the fields of compiler construction, formal language theory, and automated parsing. The process of converting a grammar to CNF is essential for simplifying certain algorithms, especially those related to parsing, such as the CYK (Cocke-Younger-Kasami) algorithm. In CNF, each production rule in a grammar must follow one of two strict forms: either a non-terminal producing exactly two non-terminals (A → BC) or a non-terminal producing a single terminal (A → a). The only exception is the start symbol, which may produce the empty string (ε) under specific conditions. This standardization allows algorithms to operate more efficiently and consistently.

A context-free grammar (CFG) is said to be in **Chomsky Normal Form** if all production rules conform to one of the following forms:

- A → BC, where A, B, and C are non-terminal symbols and neither B nor C is the start symbol,
- A → a, where A is a non-terminal and a is a terminal,
- S → ε, where S is the start symbol and ε is the empty string (only allowed if ε is in the original language).

One of the most powerful theoretical results associated with CNF is the **language preservation theorem**, which states:

> _For every context-free grammar G, there exists a grammar G′ in Chomsky Normal Form such that L(G) = L(G′), except possibly for the inclusion or exclusion of the empty string ε._

This theorem guarantees that transforming a grammar into CNF does not alter the language it generates, making it an equivalence-preserving transformation. This is crucial for correctness in compilers and formal verification systems.

The conversion of a general context-free grammar to CNF involves multiple transformation steps. First, ε-productions are eliminated. These are production rules that allow a non-terminal to produce the empty string. Removing them involves identifying nullable non-terminals and updating the grammar so that it preserves the original language without relying on ε. Following that, unit productions are removed. These are rules where one non-terminal leads directly to another, such as A → B. Such rules can be redundant or cause infinite loops, so they are replaced by copying the corresponding rules of the target non-terminal. Finally, all remaining rules are checked to ensure they adhere to the CNF format. If any rule violates the format, it's replaced with two or more rules that adhere to the CNF format. This process ensures that the grammar is in CNF, making it easier to analyze and manipulate for various applications.

Another necessary step in the process is eliminating non-productive and inaccessible symbols. Non-productive symbols are those that cannot derive any terminal string and thus do not contribute to the generation of valid strings in the language. Inaccessible symbols, on the other hand, are never reached from the start symbol and therefore have no effect on the language. Both types of symbols are removed to streamline the grammar and reduce unnecessary complexity. Finally, the grammar is transformed into CNF by replacing each production rule with a sequence of rules that adhere to the CNF format. This process ensures that the grammar is in a standard and efficient form, making it easier to analyze and manipulate.

Once the grammar is simplified, the next phase involves adjusting the production rules to comply with CNF format. This includes replacing terminals in rules that contain both terminals and non-terminals with new non-terminal variables that represent those terminals. For instance, if a rule contains a terminal like 'a' in the middle of a production, it is replaced with a new non-terminal such as T1, and a new rule T1 → a is added. In addition, productions with more than two symbols on the right-hand side are binarized by introducing new intermediate variables. This ensures that all rules either have one terminal or two non-terminals on the right-hand side. Finally, any remaining non-terminal symbols that have only one production rule are replaced with their corresponding terminal symbols. This final step ensures that all non-terminals in the grammar have at least two production rules, adhering to the strict CNF format.

In addition to the practical advantages and implementation details already discussed, there are several critical theoretical aspects of CNF that further its utility in formal language theory and computational applications.

1. Foundations and Historical Perspective
   CNF was developed as a standard form that simplifies the structure of context-free grammars while preserving their generative capacity. Its formulation was instrumental in the development of parsing algorithms—most notably, the CYK (Cocke-Younger-Kasami) algorithm—which exploits the binary branching structure of CNF grammars for efficient membership testing. In the early days of compiler design, having a grammar with uniform and predictable rule formats significantly lowered the complexity of syntax analysis.

2. Formal Constraints and Structural Uniformity
   The strict forms allowed in CNF (A → BC and A → a, with an allowance for S → ε) impose a regular structure on grammars that is not present in more general forms. This uniformity results in several theoretical benefits:

   - Deterministic Parsing: The binary format reduces ambiguity and aids in constructing deterministic parsers.
   - Complexity Reduction: Many problems related to context-free languages, such as checking membership or emptiness, have simpler algorithms when the grammar is in CNF.
   - Language Equivalence: Despite the transformations applied during conversion, CNF preserves the language generated by the original grammar (aside from the possible exclusion of the empty string when it is not allowed by CNF). This preservation is a non-trivial theoretical guarantee, with rigorous proofs rooted in automata theory.

3. Conversion Complexity and Algorithms
   The process of converting an arbitrary context-free grammar to CNF typically involves several computationally intensive steps:

   - Epsilon Production Elimination: Identifying nullable symbols requires a fixed-point algorithm that iteratively updates the set of non-terminals capable of deriving an empty string. Although this may seem computationally expensive, it is guaranteed to converge in a finite number of steps since the number of non-terminals is finite.
   - Unit Production Removal: This step involves the transitive closure computation over the unit production relation. The procedure ensures that any chain of unit productions is replaced by direct productions, thus avoiding redundant derivations.
     Binarization: For productions with more than two non-terminal symbols, new non-terminal variables (often called intermediate symbols) are introduced to systematically reduce right-hand sides to binary forms. The creation of these new symbols maintains the language’s integrity while conforming to CNF constraints.

4. Theoretical Implications for Parsing Algorithms
   One of the primary motivations for converting grammars to CNF is its direct applicability to the CYK algorithm, which operates in O(n^3) time for an input string of length n. In CNF, every production is structured so that each derivation step of a string corresponds to a binary split, thereby allowing dynamic programming techniques to efficiently determine if the string can be generated by the grammar. This efficiency is crucial in applications such as natural language processing and compiler construction, where parsing speed can be a significant bottleneck.

5. Relations to Other Normal Forms
   CNF is one of several normal forms for context-free grammars. Others, like Greibach Normal Form (GNF), emphasize different properties—such as the form A → aα, where α is a (possibly empty) string of non-terminals—to facilitate top-down parsing. While GNF is particularly useful for constructing recursive descent parsers, CNF’s binary production structure is more amenable to bottom-up parsing techniques and thus showcases the interplay between grammar normalization and parsing methodology.

6. Practical Consequences in Compiler Construction
   Modern compilers leverage the theoretical properties of CNF indirectly through parser generators that optimize for efficiency and correctness. The intermediate representation of grammars in CNF allows for error-checking, conflict resolution, and better support for optimizations during syntax analysis. This structured format also facilitates formal verification of the parser’s correctness, a key aspect in safety-critical systems.

By deepening our understanding of these theoretical aspects, we gain further insight into why CNF remains a cornerstone in the study of context-free grammars and why its systematic conversion process (as implemented in the GrammarCNFConverter class) is both practically significant and theoretically justified.

The Python implementation of this process, through a class named `GrammarCNFConverter`, allows these steps to be executed systematically. The class receives the grammar's non-terminals, terminals, production rules, and start symbol, and then applies each transformation in sequence. After conversion, the grammar is guaranteed to be in CNF format, which is suitable for use in further computational analysis or algorithmic applications. This class serves as a fundamental tool for preparing context-free grammars for various computational tasks. The class is designed to be flexible and adaptable, allowing for customization and integration into different computational contexts.

This project demonstrates the practical application of theoretical concepts in formal language theory. By implementing the conversion to CNF programmatically, it becomes possible to handle more complex grammars efficiently and prepare them for processing in real-world scenarios such as compiler design and language processing systems. The structured approach to grammar conversion also reinforces a deeper understanding of the underlying principles of context-free grammars and their transformations.

Chomsky Normal Form is more than a syntactic restriction on grammar structures—it is a foundational principle in the theory of computation, automata, and language design. Its role in algorithm design, parsing theory, formal verification, and NLP reflects the deep interplay between theory and practice. Mastering CNF means mastering the structural heart of context-free grammars, and the ability to convert arbitrary grammars into CNF is a crucial skill in both academic and applied computer science domains.

## Objectives

The primary objectives of this laboratory work were:

1. Learn about Chomsky Normal Form (CNF).
2. Get familiar with the approaches of normalizing a grammar.
3. Implement a method for normalizing an input grammar by the rules of CNF.
   The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).
   The implemented functionality needs executed and tested.
4. BONUS point would be given if the student will make the aforementioned function to accept any grammar, not only the one from the student's variant.

## Implementation Description

The implementation of the Chomsky Normal Form (CNF) conversion involves a series of transformations that ensure the grammar is in a standard form suitable for various computational tasks. The process involves several steps.

This Python project implements a tool for converting a context-free grammar (CFG) into **Chomsky Normal Form (CNF)**. CNF is a normalized structure of CFGs that enables efficient parsing and theoretical analysis. The program facilitates this transformation by handling all the necessary intermediate steps: removing ε-productions, unit productions, non-productive symbols, and inaccessible symbols, and finally converting the grammar into binary productions with terminal isolation.

### Class: `GrammarCNFConverter`

#### Initialization

```python
def __init__(self, non_terminals, terminals, productions, start_symbol)
```

- `non_terminals`: A set of non-terminal symbols (`VN`)
- `terminals`: A set of terminal symbols (`VT`)
- `productions`: A dictionary where each non-terminal maps to a list of production rules (right-hand side as a list of symbols)
- `start_symbol`: The initial symbol of the grammar (`S`)

### 1. **Eliminate ε-Productions**

```python
def eliminate_epsilon_productions(self)
```

- Identifies all **nullable** non-terminals (those that can derive ε).
- Rewrites productions by generating all possible subsets of productions excluding ε.
- Ensures ε is only retained when it is necessary for the start symbol.

#### Why?

ε-productions can make parsing unpredictable. Removing them simplifies grammar structure.

### 2. **Eliminate Unit Productions**

```python
def eliminate_unit_productions(self)
```

- Finds all **unit pairs** (e.g., `A → B`).
- Expands these pairs by copying the production rules from target non-terminals (`B`) into the source (`A`).
- Removes original unit productions from the grammar.

#### Why?

Unit productions can introduce unnecessary recursion and complexity.

### 3. **Eliminate Non-Productive Symbols**

```python
def eliminate_non_productive_symbols(self)
```

- Detects **productive non-terminals** (those that eventually produce terminal strings).
- Filters out rules and symbols that never lead to a valid string of terminals.

#### Why?

Non-productive symbols serve no functional purpose in generating valid strings.

### 4. **Eliminate Inaccessible Symbols**

```python
def eliminate_inaccessible_symbols(self)
```

- Traverses the grammar starting from the start symbol.
- Removes symbols that are never reached in any derivation.

#### Why?

Inaccessible symbols are effectively dead code and clutter the grammar.

### 5. **Convert to CNF**

```python
def convert_to_cnf(self)
```

- **Terminal Isolation**: Terminal symbols in productions longer than one symbol are replaced by new non-terminals (e.g., `T1 → a`).
- **Binarization**: Productions with more than two symbols are broken down into binary rules using intermediate non-terminals (e.g., `A → B C D` becomes `A → B X1`, `X1 → C D`).

#### Why?

CNF requires all productions to be of the form:

- `A → a`
- `A → B C`

This format is optimal for algorithms like CYK.

### `convert()`

A wrapper method that runs all transformation steps in the proper order:

```python
def convert(self):
    self.eliminate_epsilon_productions()
    self.eliminate_unit_productions()
    self.eliminate_non_productive_symbols()
    self.eliminate_inaccessible_symbols()
    self.convert_to_cnf()
```

### `print_grammar()`

Prints the grammar in a readable format:

- Displays non-terminals, terminals, start symbol, and all production rules.

```python
def print_grammar(self)
```

### `input_grammar()`

- Prompts the user to input grammar components interactively.
- Supports standard CFG input formats with `;` as rule separator and `|` as alternative separator.
- Converts input into appropriate internal data structures.

Example Input:

```
S->aB|bA|B; A->b|aD|AS|bAB|ε
```

The script supports two modes:

- **Example Grammar**: Uses a predefined grammar with ε and complex productions.
- **Custom Grammar**: Allows the user to define a CFG interactively.

```python
if __name__ == "__main__":
    ...
```

## Expected Results

The expected results of running this code are as follows: The user is prompted to input a grammar in the form of a string. The program then processes this input and outputs the grammar in Chomsky Normal Form (CNF). The output will be in the form of a dictionary, where each non-terminal maps to a list of production rules. Each rule is represented as a list of symbols.

## Output

The output of the program will be a dictionary representing the grammar in CNF. Each non-terminal will be a key, and its value will be a list of production rules. Each production rule will be a list of symbols.

Input:

    Use example grammar? (y/n): y

    Original Grammar:

    --- Grammar ---
    Non-terminals: {'D', 'C', 'S', 'A', 'B'}
    Terminals: {'b', 'a'}
    Start Symbol: S
    Productions:
    S → a B
    S → b A
    S → B
    A → b
    A → a D
    A → A S
    A → b A B
    A → ε
    B → a
    B → b S
    C → A B
    D → B B

Output:

    Converted to Chomsky Normal Form:

    --- Grammar ---
    Non-terminals: {'S', 'T2', 'D', 'X3', 'A', 'T1', 'B'}
    Terminals: {'b', 'a'}
    Start Symbol: S
    Productions:
    D → B B
    A → b
    A → T1 D
    A → A S
    A → T2 B
    A → T2 X3
    A → T1 B
    A → b
    A → T2 A
    A → a
    A → T2 S
    X3 → X3 B
    T1 → a
    T2 → b
    S → T1 B
    S → b
    S → T2 A
    S → a
    S → T2 S
    B → a
    B → T2 S

## Conclusions

This lab provided me with a deeper understanding of Chomsky Normal Form (CNF) and its profound theoretical and practical implications in formal language processing. By engaging with the process of converting a general context-free grammar into CNF, I learned firsthand how methodically eliminating epsilon productions, unit productions, and even non-productive symbols can transform an otherwise unwieldy grammar into a uniform structure optimized for efficient parsing. The step-by-step transformations—especially the binarization of production rules—highlighted the significance of structured approaches in ensuring that algorithms, such as the CYK algorithm, operate correctly and effectively.

Working through this process underscored the interplay between theory and practice. I came to appreciate that CNF is not merely a theoretical construct, but a practical tool that simplifies the design and implementation of compilers and interpreters. The experience sharpened my ability to analyze and manipulate grammars, reinforcing how careful attention to formal details can simplify complex problems. Moreover, experimenting with different grammars deepened my confidence in predicting and controlling the behavior of parsing algorithms, which is essential in many automated language processing tasks.

In summary, this lab boosted my proficiency in both the theoretical underpinnings and the practical applications of CNF. It laid a strong foundation for future projects involving compiler design and formal language analysis, and it also inspired me to explore further into the optimization of algorithms that rely on formally structured grammars. This enriched understanding will undoubtedly serve as a cornerstone in my continued journey in advanced computer science and automation projects.

## References

- Laboratory work guide - https://github.com/filpatterson/DSL_laboratory_works
- Python documentation - https://docs.python.org/3/
- Documentation on re module in Python - https://docs.python.org/3/library/re.html
