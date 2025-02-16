# Laboratory Work: Intro to formal languages. Regular grammars. Finite Automata.

**Course:** Formal Languages & Finite Automata\
**Author:** Mihalevschi Alexandra

## Theory

A formal language is a structured set of symbols governed by specific rules. It consists of three primary components:

- **Alphabet (VT)**: A finite set of valid symbols.
- **Vocabulary**: A set of valid words constructed using the alphabet.
- **Grammar (P)**: A set of production rules that define valid sequences.

A finite automaton (FA) is a computational model used to recognize patterns in formal languages. It consists of:

- **States (Q)**: A finite set of states.
- **Alphabet (Σ)**: A set of input symbols.
- **Transition Function (δ)**: Rules for moving between states.
- **Initial State (q0)**: The starting state.
- **Final States (F)**: Accepting states.

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

- A constructor to initialize **VN** (non-terminals), **VT** (terminals), **P** (production rules), and **S** (start symbol).
- A method to generate valid strings based on the grammar rules.
- A method to convert the grammar into a finite automaton.

```python
import random

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

The `FiniteAutomaton` class includes:

- A constructor to initialize states, alphabet, transition functions, start state, and final states.
- A method to check if an input string belongs to the language defined by the FA.

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

## References

- Introduction of Finite Automata - GeeksforGeeks - https://www.geeksforgeeks.org/introduction-of-finite-automata/
- Laboratory work guide - https://github.com/filpatterson/DSL_laboratory_works/blob/master/1_RegularGrammars/task.md
- Formal languages and compiler design - Irina Cojuhari - presentation
