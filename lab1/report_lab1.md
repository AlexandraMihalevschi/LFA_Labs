# Laboratory Work: Intro to formal languages. Regular grammars. Finite Automata.

**Course:** Formal Languages & Finite Automata\
**Author:** Mihalevschi Alexandra

## Theory

A **formal language** is a structured system that organizes symbols according to a set of predefined rules. It consists of three main components. The **alphabet (VT)** is the collection of valid symbols that can be used in the language. Using these symbols, we can form a **vocabulary**, which consists of valid words or sequences. Lastly, the **grammar (P)** defines the rules for constructing valid sequences from the vocabulary, ensuring that the language follows a structured form.

A **finite automaton (FA)** is a mathematical model used to recognize patterns within formal languages. It consists of several components that define how it processes input. The **states (Q)** represent different conditions the system can be in, while the **alphabet (Σ)** defines the set of input symbols the automaton reads. The **transition function (δ)** determines how the system moves between states based on the input. Every FA has an **initial state (q0)** where processing begins and **final states (F)** that indicate successful recognition of a string.

### Fundamentals of Formal Languages

Formal languages follow strict mathematical principles to define their structure. A **string** is simply a sequence of symbols from the alphabet, similar to how letters form words in natural languages. There is also a special case known as the **empty string (ε)**, which contains no symbols at all. A **language** is a collection of strings that follow specific rules, defining what is considered valid within that system. One important operation in formal languages is **concatenation**, which refers to joining two strings end to end to create a longer string.

### Properties of Regular Grammars

Regular grammars are a special type of grammar that define **regular languages**, one of the simplest classes of formal languages. These grammars follow a set of unique characteristics. Each rule, or **production**, can have at most one non-terminal symbol on the right-hand side. Additionally, non-terminal symbols in a production generally appear either at the beginning or the end of the sequence. A key property of regular grammars is their equivalence to finite automata, meaning they can express the same types of languages.

### Types of Productions in Regular Grammars

Regular grammars use different types of rules to form valid strings. **Terminal productions** directly generate a symbol, such as A → a. **Non-terminal productions** involve both symbols and variables, following structures like A → aB or A → Ba, where B represents another non-terminal. Some grammars allow **empty productions**, such as A → ε, which produce an empty string. These rules define how words are formed in a regular language and ensure consistency in structure.

### Understanding Finite Automata

A finite automaton functions based on a few essential components. The **state register** keeps track of the current state, while the **input tape** holds the string being processed. The **transition function** determines how the automaton moves between states depending on the input symbols it reads. Finally, the **control unit** manages the entire process, ensuring that the correct transitions take place according to the rules defined by the automaton.

### How Regular Grammars and Finite Automata Are Related

There is a strong relationship between regular grammars and finite automata. Any regular grammar can be converted into a corresponding finite automaton that recognizes the same language. Likewise, every finite automaton has an equivalent regular grammar that expresses the same structure. Both are used to describe **regular languages**, meaning they share the same language recognition capabilities. This equivalence allows easy conversion between the two representations without altering the meaning of the language.

### Recognizing a Language

For a string to be **recognized** by an automaton, it must satisfy certain conditions. First, the input string must be completely processed. Second, the automaton must end in a **final state** after reading all the input symbols. Lastly, all transitions taken during the processing must be valid according to the rules of the automaton. If these conditions are met, the string is considered accepted by the automaton.

### Closure Properties of Regular Languages

Regular languages possess several important properties that make them useful in different computational tasks, such as compiler design and text processing. They are **closed under** various operations, meaning applying these operations to regular languages will still result in a regular language. These operations include **union**, where two languages are combined, and **intersection**, which finds common elements between two languages. Other operations include **concatenation**, which joins two languages, and the **Kleene star**, which allows repetition of strings. Regular languages are also closed under **complement**, which creates a language that contains all strings **not** in the original language, and **reverse**, which flips the order of strings in the language.

These closure properties make regular languages essential in fields like **lexical analysis**, which is used in compilers to recognize words in programming languages, and **pattern matching**, which is used in search algorithms and text processing. Because of their well-defined structure, regular languages provide a solid foundation for understanding more complex computational models.

## Objectives

1. Explore the concept of formal languages and understand the requirements for a language to be considered formal.
2. Establish the foundational setup for a semester-long project, either as standalone tasks or as stages of a larger integrated project.
3. Set up a GitHub repository for managing and updating the project effectively.
4. Select a programming language that facilitates problem-solving with minimal setup complexity.
5. Organize and store reports separately to simplify the verification process.
6. Based on a given grammar definition:
   - Implement a class representing the grammar.
   - Develop a function to generate five valid strings from the defined language.
   - Implement functionality to convert a `Grammar` object into a `FiniteAutomaton` object.
   - Create a method in `FiniteAutomaton` to verify if a given string can be generated through state transitions.

## Implementation Description

### Grammar Class

The `Grammar` class is implemented with:

The constructor takes four essential components:

    VN: Set of non-terminal symbols like {"S", "A", "B", "C"} representing states
    VT: Set of terminal symbols like {"a", "b"} that form the final strings
    P: Production rules dictionary where each key is a non-terminal and values are possible transitions
    start_symbol: Initial symbol ("S") where string generation begins

The generate_string method implements an efficient recursive descent algorithm that traverses these production rules, making random selections at each step to produce diverse valid strings. This design allows for both deterministic string generation when needed and random sampling of the language space, making it particularly useful for testing and verification purposes.

```python

class Grammar:
    def __init__(self, VN, VT, P, start_symbol):
        self.VN = VN  # Non-terminals
        self.VT = VT  # Terminals
        self.P = P    # Production rules (dictionary)
        self.start_symbol = start_symbol

    def generate_string(self, symbol=None):
        """Recursively generates a valid string from the grammar"""
        if symbol is None:
            symbol = self.start_symbol

        if symbol in self.VT:  # If it's a terminal, return it
            return symbol

        if symbol not in self.P:  # No production rules for this symbol
            return ""

        # Randomly choose a production rule
        production = random.choice(self.P[symbol])
        return "".join(self.generate_string(s) for s in production)

    def generate_n_strings(self, n=5):
        """Generates n valid strings using the grammar"""
        return [self.generate_string() for _ in range(n)]
```

### Finite Automaton Class

The FiniteAutomaton class represents a robust implementation of a finite state machine that effectively processes and validates strings according to the language rules. The constructor sets up the fundamental components needed for string recognition: states for tracking positions, an alphabet of valid symbols, transition functions defining the rules, a designated start state, and final accepting states. The accepts() method systematically processes input strings by maintaining the current state and following transitions based on each input symbol.

The transition system works like a state machine:

- Current state tracks position in the automaton
- Each input symbol triggers a state change
- The transitions dictionary maps (state, symbol) pairs to next states

```python
class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, start_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states

    def accepts(self, input_string):
        """Checks if an input string is accepted by the finite automaton"""
        current_state = self.start_state

        for symbol in input_string:
            if (current_state, symbol) in self.transitions:
                current_state = self.transitions[(current_state, symbol)]
            else:
                return False

        return current_state in self.final_states
```

### Conversion from Grammar to Finite Automaton

The conversion from Grammar to Finite Automaton is implemented as follows:

```python
def to_finite_automaton(self):

        transitions = {}
        for lhs, rules in self.P.items():
            for rhs in rules:
                key = (lhs, rhs[0])
                if len(rhs) == 1:
                    transitions.setdefault(key, set()).add("q_f")
                elif len(rhs) == 2:
                    transitions.setdefault(key, set()).add(rhs[1])
                else:
                    pass


        states = set(self.VN)
        states.add("q_f")
        alphabet = set(self.VT)
        start_state = self.start_symbol
        final_states = {"q_f"}
        return FiniteAutomaton(states, alphabet, transitions, start_state, final_states)
```

The conversion from Grammar to Finite Automaton is implemented through a systematic transformation process. The method iterates through the production rules (P) of the grammar, where each rule's left-hand side (lhs) represents a state and the right-hand side (rhs) determines the transitions. For each production rule, it creates a transition key consisting of the current state and the first symbol of the right-hand side.

The final automaton is constructed by combining the non-terminal symbols (VN) with an additional final state "q_f" to form the complete set of states, using the terminal symbols (VT) as the alphabet, maintaining the original start symbol, and establishing "q_f" as the sole final state. This conversion preserves the language recognition capabilities of the original grammar while transforming it into an equivalent finite automaton structure.

### Example Usage

```python
VN = {"S", "A", "B", "C"}
VT = {"a", "b"}
P = {
    "S": [["a", "A"], ["a", "B"]],
    "A": [["b", "S"]],
    "B": [["a", "C"]],
    "C": [["a"], ["b", "S"]]
}

grammar = Grammar(VN, VT, P, "S")


print("Generated strings:")
for s in grammar.generate_n_strings():
    print(s)

fa = grammar.to_finite_automaton()

print("\nEnter strings to check (or 'exit'):")
while True:
    input_string = input("Enter string: ").strip()
    if input_string.lower() == 'exit':
        break
    is_valid = fa.accepts(input_string)
    print(f"String '{input_string}' is {'valid' if is_valid else 'invalid'}")
```

This example demonstrates the practical application of the grammar and finite automaton implementation. The code initializes a grammar with four non-terminals (S, A, B, C) and two terminals (a, b), along with their production rules. The grammar is used to generate random valid strings through the generate_n_strings() method, showcasing possible strings that conform to the language rules. Then, it converts the grammar to a finite automaton and provides an interactive interface where users can input strings to check if they belong to the language. The program continues to accept input strings until the user types 'exit', providing immediate feedback on whether each entered string is valid or invalid according to the language rules.

## Results

- Implemented a grammar-based string generator.
- Converted a given grammar into a finite automaton.
- Implemented a function to check if a string belongs to the language.

## Output

**Output nr.1**

`Generated strings:
abababaabaaa
abaababaabaaa
ababaabaaa
ababaabaaa
abababaabaabababaaa

Enter strings to check (or 'exit'):
Enter string: abababaabaaa
String 'abababaabaaa' is valid
Enter string: aS
String 'aS' is invalid
Enter string: asddadadad
String 'asddadadad' is invalid
Enter string: aaa
String 'aaa' is valid
Enter string: a
String 'a' is invalid
Enter string: exit
`

**Output nr.2**

`Generated strings:
aabaababababaababaaa
abababaabaaa
abaaa
abababaababababaaa
aaa

Enter strings to check against the grammar (type 'exit' to quit):
Enter string: aaa
String 'aaa' is valid according to the grammar.
Enter string: a
String 'a' is invalid according to the grammar.
Enter string: abaaa
String 'abaaa' is valid according to the grammar.
Enter string: aabaababababaababaaa
String 'aabaababababaababaaa' is valid according to the grammar.
Enter string: exit
`

## Conclusions

This laboratory work provided insight into formal languages and automata theory. By implementing a grammar and converting it into a finite automaton, the practical application of theoretical concepts was demonstrated. The implementation allows for generating language-compliant strings and validating inputs against defined rules.
By working through the process of defining a grammar, creating production rules, and translating them into a finite automaton, the fundamental principles of language recognition became clearer. Additionally, testing different inputs and observing how the automaton processes them helped in understanding the mechanics of state transitions and acceptance conditions. This practical approach not only deepened comprehension but also highlighted the significance of formal languages in areas such as programming language design and text processing.

## References

- Introduction of Finite Automata - GeeksforGeeks - https://www.geeksforgeeks.org/introduction-of-finite-automata/
- Laboratory work guide - https://github.com/filpatterson/DSL_laboratory_works/blob/master/1_RegularGrammars/task.md
- Formal languages and compiler design - Irina Cojuhari - presentation
