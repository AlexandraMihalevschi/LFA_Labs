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

    def to_finite_automaton(self):
        """Converts the grammar into a Finite Automaton (FA)"""
        states = set(self.VN)  # Non-terminals become states
        alphabet = set(self.VT)  # Alphabet remains the same
        transitions = {}

        for lhs, rhs_list in self.P.items():
            for rhs in rhs_list:
                if len(rhs) == 1:  # Terminal transition
                    transitions[(lhs, rhs[0])] = rhs
                else:  # Non-terminal transition
                    transitions[(lhs, rhs[0])] = rhs[1]

        start_state = self.start_symbol
        final_states = {s for s in self.VN if any(r in self.VT for r in self.P.get(s, []))}

        return FiniteAutomaton(states, alphabet, transitions, start_state, final_states)


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


# Define the grammar from your variant
VN = {"S", "A", "B", "C"}
VT = {"a", "b"}
P = {
    "S": [["a", "A"], ["a", "B"]],
    "A": [["b", "S"]],
    "B": [["a", "C"]],
    "C": [["a"], ["b", "S"]]
}

# Create a Grammar instance
grammar = Grammar(VN, VT, P, "S")

# Generate 5 valid strings
print("Generated strings:")
for s in grammar.generate_n_strings():
    print(s)

# Convert grammar to finite automaton
fa = grammar.to_finite_automaton()

# Test FA string acceptance
test_strings = ["aab", "aaa", "abb"]
for ts in test_strings:
    print(f"Does FA accept '{ts}'? {fa.accepts(ts)}")
 