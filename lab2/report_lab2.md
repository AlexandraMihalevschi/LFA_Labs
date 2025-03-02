# Laboratory Work: Determinism in Finite Automata. Conversion from NDFA to DFA. Chomsky Hierarchy.

**Course:** Formal Languages & Finite Automata\
**Author:** Mihalevschi Alexandra

## Theory

### **Introduction**

A **finite automaton (FA)** is a theoretical model of computation used to represent processes or computations that can be described with a finite set of states. These automata are important in formal language theory and are often used to recognize regular languages. The concept of a finite automaton can be likened to a **state machine**, as both structures share similar properties. They represent a system that moves through a series of states based on inputs, ultimately determining whether the input string is accepted or rejected.

The term "finite" in finite automaton emphasizes that the system has a **finite number of states**. The automaton has a **starting state** and a set of **final states**, which define the beginning and the end of a process. This structural feature ensures that the process modeled by the automaton has a clear starting point and an endpoint.

The **deterministic** or **non-deterministic** nature of an automaton plays a critical role in how the system behaves. Understanding the difference between deterministic and non-deterministic automata is essential for analyzing and converting between different types of finite automata.

### **Determinism in Finite Automata**

In the context of finite automata, **determinism** refers to a situation where, for any given state and input, there is exactly one transition that leads to a next state. This characteristic makes the behavior of the system predictable and traceable, as the next state of the system is uniquely determined by the current state and the input symbol.

Formally, a **deterministic finite automaton (DFA)** is defined as a 5-tuple (Q, Σ, δ, q₀, F) where:

- **Q** is a finite set of states.
- **Σ** is a finite set of input symbols (the alphabet).
- **δ: Q × Σ → Q** is the transition function, which defines the state transition for each input symbol.
- **q₀** is the start state, from which the automaton begins.
- **F** is the set of final or accepting states.

In a **DFA**, for each state and input symbol, there is exactly one transition to a new state. This means that the transition function δ does not map to multiple states for the same input. Thus, the behavior of the system is predictable: given an input string, the DFA will follow a unique path through its states, ultimately determining whether the string is accepted (i.e., it ends in a final state) or rejected (it does not end in a final state).

### **Non-Determinism in Finite Automata**

On the other hand, **non-determinism** occurs when, for a given state and input symbol, there are multiple possible states that the automaton could transition to. This feature introduces **ambiguity** in the system's behavior, as the next state is not uniquely determined by the current state and input symbol.

Formally, a **non-deterministic finite automaton (NDFA)** is defined as a 5-tuple (Q, Σ, δ, q₀, F), but with the key difference that the transition function δ maps to a set of possible next states, rather than a single state. Specifically, δ: Q × Σ → P(Q) where P(Q) represents the power set of Q, meaning δ can map to multiple states or even to the empty set.

In an NDFA, there may be multiple possible ways to process the input string, and the automaton can "choose" between these paths. This allows the automaton to explore multiple possibilities simultaneously, which makes it "non-deterministic." However, despite the non-deterministic nature of these automata, they can still recognize the same class of languages (regular languages) as DFAs.

### **Deterministic vs Non-Deterministic Automata**

The key difference between deterministic and non-deterministic automata lies in the **transition function**:

- In a DFA, the transition function is **deterministic**, meaning there is only one possible transition for each input symbol at each state.
- In an NDFA, the transition function is **non-deterministic**, allowing multiple possible transitions for the same input symbol from a given state.

Non-determinism may appear in a variety of ways, such as:

- **Multiple transitions for the same symbol**: A single state may have multiple transitions for the same input symbol.
- **Epsilon transitions**: An NDFA may transition from one state to another without consuming any input (i.e., through an epsilon or ε-transition).

Despite the non-deterministic behavior, an NDFA can still be used to recognize regular languages, which are the same languages recognized by a DFA. This is due to the fact that every NDFA can be converted into an equivalent DFA, which has the advantage of being more predictable and easier to process for certain types of computations.

### **Conversion from NDFA to DFA**

One of the key operations in automata theory is the **conversion from a non-deterministic finite automaton (NDFA) to a deterministic finite automaton (DFA)**. While an NDFA can recognize the same class of languages as a DFA (i.e., regular languages), the DFA is easier to implement and analyze due to its deterministic nature.

The process of converting an NDFA to a DFA involves the technique called **subset construction** (or **powerset construction**). This algorithm involves creating new states in the DFA that correspond to sets of states in the NDFA. Each state of the DFA represents a combination of states from the NDFA, and the transitions are determined by considering the possible transitions in the NDFA from each set of states.

The steps involved in converting an NDFA to a DFA are:

1. **Start state**: The start state of the DFA corresponds to the set of states in the NDFA that can be reached from the start state by epsilon transitions (if any).
2. **New states**: Each new state in the DFA corresponds to a set of states in the NDFA.
3. **Transitions**: For each symbol in the alphabet, calculate the set of states that the NDFA can transition to from any state in the current set. This forms the transition for the DFA.
4. **Final states**: If any state in the set corresponds to a final state in the NDFA, then the new state in the DFA is a final state.

This subset construction ensures that the DFA is equivalent to the NDFA in terms of the languages they recognize, but with the added benefit of determinism. Although the DFA may have exponentially more states than the NDFA (in the worst case), it provides a deterministic path for input processing.

### **Chomsky Hierarchy**

The **Chomsky hierarchy** is a classification of formal languages based on their generative power. It divides languages into four types, each corresponding to a different class of automata or grammar. The hierarchy is structured as follows:

1. **Type 0** (Recursively enumerable languages): These are the most general type of languages, which can be recognized by a **Turing machine**. They are capable of describing any computable process.
2. **Type 1** (Context-sensitive languages): These languages are recognized by a **linear-bounded automaton** (LBA). Context-sensitive languages can be more complex than regular languages but still have a structure that can be analyzed by an automaton with limited resources.
3. **Type 2** (Context-free languages): These languages can be generated by a **context-free grammar** (CFG) and are recognized by a **pushdown automaton** (PDA). Context-free languages are widely used to describe the syntax of programming languages and are the second-most powerful class in the hierarchy.
4. **Type 3** (Regular languages): These are the simplest class of languages and can be generated by a **regular grammar**. Regular languages can be recognized by a **finite automaton** (DFA or NDFA). They are used in lexical analysis, text processing, and pattern matching.

Regular languages, which are the class of languages that finite automata (both deterministic and non-deterministic) recognize, are classified as **Type 3** in the Chomsky hierarchy. Despite the simplicity of regular languages, they are incredibly powerful in many practical applications, including lexical analysis, regular expressions, and finite state machines.

### **The Role of Finite Automata in the Chomsky Hierarchy**

Finite automata, whether deterministic or non-deterministic, are used to recognize **regular languages**, which belong to **Type 3** in the Chomsky hierarchy. The simplicity of finite automata allows them to efficiently process regular languages, making them invaluable tools in areas such as text processing, compilers, and formal verification.

While regular languages (Type 3) are the simplest in the Chomsky hierarchy, the other types (Type 1, Type 2, and Type 0) allow for more complex structures and computations. However, finite automata are restricted to recognizing only regular languages, and thus cannot handle the more complex languages in Type 1 and Type 2 without additional computational resources.

A **formal language** is a structured system that organizes symbols according to a set of predefined rules. It consists of three main components. The **alphabet (VT)** is the collection of valid symbols that can be used in the language. Using these symbols, we can form a **vocabulary**, which consists of valid words or sequences. Lastly, the **grammar (P)** defines the rules for constructing valid sequences from the vocabulary, ensuring that the language follows a structured form.

A **finite automaton (FA)** is a mathematical model used to recognize patterns within formal languages. It consists of several components that define how it processes input. The **states (Q)** represent different conditions the system can be in, while the **alphabet (Σ)** defines the set of input symbols the automaton reads. The **transition function (δ)** determines how the system moves between states based on the input. Every FA has an **initial state (q0)** where processing begins and **final states (F)** that indicate successful recognition of a string.

## Objectives

1. Classify Grammar Based on Chomsky Hierarchy
2. Add a function in the grammar type/class to classify the grammar according to the Chomsky hierarchy.
3. Convert FA to Regular Grammar: Implement a function to convert a finite automaton (FA) to a regular grammar.
4. Check Determinism: Determine if FA is deterministic or non-deterministic.
5. Convert NDFA to DFA: Implement functionality to convert a non-deterministic finite automaton (NDFA) to a deterministic finite automaton (DFA).
6. Graphical Representation (Optional): Represent the finite automaton graphically.

## Implementation Description

This implementation demonstrates the process of converting a Finite Automaton (FA) into a Regular Grammar and also converts a Non-Deterministic Finite Automaton (NDFA) to a Deterministic Finite Automaton (DFA). The key components of this implementation include the `Grammar` and `FiniteAutomaton` classes, which handle the respective tasks for grammar classification and automaton manipulation.

### Grammar Class

The `Grammar` class is designed to represent a formal grammar consisting of non-terminals, terminals, and production rules. The main functionality of this class is to classify the grammar based on the given production rules. In the current implementation, the grammar is classified as **Type 3 (Regular)** if the rules follow the regular grammar format, where the left-hand side (LHS) consists of a single non-terminal, and the right-hand side (RHS) can either be a terminal symbol or a combination of a terminal followed by a non-terminal.

```python
class Grammar:
    def __init__(self, non_terminals, terminals, productions):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.productions = productions

    def classify(self):
        # Check if the grammar is regular
        # productions are of the form "A → aB"
        for production in self.productions:
            lhs, rhs = production.split('→')  # Split the rule into lhs and rhs
            lhs = lhs.strip()  # Remove any extra spaces
            rhs = rhs.strip()
            if len(lhs) != 1 or not lhs.isupper():  # LHS should be a single non-terminal
                return "Invalid Grammar"
            if not (rhs.islower() or (len(rhs) == 2 and rhs[0].islower() and rhs[1].isupper())):
                return "Invalid Grammar"
        return "Type 3 (Regular)"  # Since the grammar satisfies regular grammar condition
```

- **Method `classify`**: This method verifies if the grammar follows the structure of a regular grammar. The LHS must be a single non-terminal (denoted by an uppercase letter), and the RHS must either consist of a single terminal or a terminal followed by a non-terminal. If the rules deviate from this form, the grammar is marked as invalid.

### FiniteAutomaton Class

The `FiniteAutomaton` class represents a finite automaton, which is a mathematical model for representing computational systems that can be in one of a finite number of states. This class supports checking if the automaton is deterministic, converting it into a regular grammar, and converting a non-deterministic finite automaton (NDFA) to a deterministic finite automaton (DFA).

```python

class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, start_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states

    def is_deterministic(self):
        # Check if the FA is deterministic (no state has more than one transition for the same symbol)
        for state, transitions in self.transitions.items():
            for symbol in transitions:
                if len(transitions[symbol]) > 1:
                    return False  # Multiple transitions for the same symbol
        return True

```

- **Method `is_deterministic`**: This method checks if the FA is deterministic. A deterministic finite automaton (DFA) requires that each state has exactly one transition for each symbol in the alphabet. If any state has multiple transitions for the same symbol, the FA is deemed non-deterministic.

```python

def convert_to_regular_grammar(self):
        # Mapping states to non-terminals
        non_terminals = {state: chr(65 + i) for i, state in enumerate(self.states)}
        grammar_rules = []

        # Create production rules for each transition
        for state, transitions in self.transitions.items():
            for symbol, next_states in transitions.items():
                for next_state in next_states:
                    grammar_rules.append(f"{non_terminals[state]} → {symbol}{non_terminals[next_state]}")

        # Add production rule for final states (lead to ε)
        for final_state in self.final_states:
            grammar_rules.append(f"{non_terminals[final_state]} → ε")

        return non_terminals, grammar_rules
```

- **Method `convert_to_regular_grammar`**: This method converts a given FA into a regular grammar. It works by mapping each state of the FA to a non-terminal in the grammar and creating production rules based on the state transitions. Additionally, for final states in the FA, it adds production rules that lead to an epsilon (ε) transition, which represents the end of the string in the grammar.

```python

def convert_ndfa_to_dfa(self):
        # NDFA to DFA conversion using subset construction
        dfa_states = [frozenset([self.start_state])]
        dfa_transitions = {}
        dfa_final_states = set()

        state_map = {frozenset([self.start_state]): 'A'}
        unprocessed_states = [frozenset([self.start_state])]  # List to keep track of states to process

        while unprocessed_states:
            current_state = unprocessed_states.pop()
            current_state_name = state_map[current_state]

            for symbol in self.alphabet:
                next_state = set()
                for state in current_state:
                    if symbol in self.transitions.get(state, {}):
                        next_state.update(self.transitions[state].get(symbol, []))

                if next_state:
                    next_state_frozenset = frozenset(next_state)
                    if next_state_frozenset not in state_map:
                        state_map[next_state_frozenset] = chr(65 + len(state_map))  # Assign new state name
                        unprocessed_states.append(next_state_frozenset)  # Add new state to unprocessed list

                    if current_state_name not in dfa_transitions:
                        dfa_transitions[current_state_name] = {}
                    dfa_transitions[current_state_name][symbol] = state_map[next_state_frozenset]

                    if next_state & set(self.final_states):
                        dfa_final_states.add(state_map[next_state_frozenset])

        return list(state_map.values()), dfa_transitions, dfa_final_states
```

- **Method `convert_ndfa_to_dfa`**: This method converts a non-deterministic finite automaton (NDFA) into a deterministic finite automaton (DFA) using the subset construction algorithm. The process involves creating a set of states that correspond to subsets of the original NDFA states, and for each symbol in the alphabet, computing the corresponding transitions. The algorithm ensures that the DFA does not have any non-deterministic transitions, making it suitable for use in practical applications such as lexical analysis in compilers.

```python

def write_dfa_to_dot(self, dfa_states, dfa_transitions, dfa_final_states):
        with open("dfa.dot", "w") as f:
            f.write("digraph DFA {\n")
            f.write("    rankdir=LR;\n")
            f.write("    node [shape = circle];\n")


            for state in dfa_states:
                if state in dfa_final_states:
                    f.write(f"    {state} [shape = doublecircle];\n")
                else:
                    f.write(f"    {state};\n")

            for state, transitions in dfa_transitions.items():
                for symbol, next_state in transitions.items():
                    f.write(f"    {state} -> {next_state} [label = \"{symbol}\"];\n")

            f.write("}")

```

- **Method `write_dfa_to_dot`**: This method generates a DOT file that represents the DFA's states, transitions, and final states. This file can be used with visualization tools like Graphviz to generate graphical representations of the DFA, helping users visualize how the automaton processes input strings.

### Workflow

1.  **Check if FA is Deterministic**: The first step in the process is checking if the finite automaton is deterministic. This is done using the `is_deterministic` method, which examines the transitions to ensure that each state has exactly one outgoing transition per symbol in the alphabet.

2.  **Convert FA to Regular Grammar**: If the FA is deterministic, the `convert_to_regular_grammar` method is used to convert the FA into a regular grammar. This involves mapping each state of the FA to a non-terminal in the grammar and creating production rules based on the state transitions. This regular grammar can then be used for formal language analysis and recognition.

3.  **Classify the Grammar**: After the FA has been converted to a regular grammar, the `Grammar` class's `classify` method is used to verify whether the grammar is indeed a regular grammar (Type 3). This classification ensures that the grammar follows the rules for regular languages, making it useful for tasks such as lexical analysis and finite state machine modeling.

4.  **Convert NDFA to DFA**: If the FA is a non-deterministic finite automaton (NDFA), the `convert_ndfa_to_dfa` method is used to convert it into a deterministic finite automaton (DFA) using the subset construction method. The DFA is deterministic by nature, ensuring that each state has exactly one transition per symbol.

5.  **Generate DOT File for DFA**: Finally, the `write_dfa_to_dot` method generates a DOT file that represents the DFA's states, transitions, and final states. This file can be used with visualization tools like Graphviz to generate graphical representations of the DFA, helping users visualize how the automaton processes input strings.

## Results

After running the code, the following **results are expected**:

**_Check if the FA is Deterministic_**
If the FA is deterministic:
`True`

If the FA is non-deterministic:
`False`

**_Convert FA to Regular Grammar_**

Non-terminals and grammar rules:
Non-terminals: {'q0': 'A', 'q1': 'B'}
Grammar rules: ['A → aB', 'B → bA', 'B → ε']

**_Classify Grammar_**

If the grammar is regular:
Type 3 (Regular)
If the grammar is not regular:
Invalid Grammar

**_Convert NDFA to DFA_**

DFA states:
['A', 'B']
DFA transitions:
{'A': {'a': 'A', 'b': 'B'}, 'B': {'a': 'A', 'b': 'B'}}
DFA final states:
{'B'}

**_Generate DFA DOT File_**

A file named dfa.dot will be generated.

![The manual created output](/outputs/manualDFA.png)

## Output

The FA is deterministic: False <br>
Non-terminals: {'q0': 'A', 'q1': 'B', 'q2': 'C', 'q3': 'D'} <br>
Grammar rules: ['A → aA', 'A → aB', 'B → bC', 'C → aC', 'C → bD', 'D → aD', 'D → ε'] <br>
The grammar is classified as: Type 3 (Regular) <br>
DFA States: ['A', 'B', 'C', 'D'] <br>
DFA Transitions: {'A': {'a': 'B'}, 'B': {'a': 'B', 'b': 'C'}, 'C': {'a': 'C', 'b': 'D'}, 'D': {'a': 'D'}} <br>
DFA Final States: {'D'} <br>
DFA DOT file has been generated as dfa.dot. <br>

![The generated output](/outputs/generatedDFA.png)

Generated output by the code

## Conclusions

This lab gave me a practical understanding of formal languages and automata theory. By working with a grammar and converting it into a finite automaton, I was able to connect theoretical concepts to real-world applications. I learned how to define a grammar, create production rules, and then convert them into a finite automaton, which showed how to generate valid strings for a given language and check inputs against specified rules.

Testing different inputs and seeing how the automaton processes them helped me understand how state transitions and acceptance conditions work. The process of converting a non-deterministic finite automaton (NDFA) to a deterministic finite automaton (DFA) was particularly insightful in understanding state management. Additionally, generating a DFA in DOT format demonstrated how automata can be visualized for better understanding.

Overall, the lab not only deepened my understanding of the theory behind automata and grammars but also showed me how these concepts are applied in fields like programming language design and text processing.

## References

- Introduction of Finite Automata - GeeksforGeeks - https://www.geeksforgeeks.org/introduction-of-finite-automata/
- Laboratory work guide - https://github.com/filpatterson/DSL_laboratory_works
- Finite automata. Part 1- Irina Cojuhari - presentation
