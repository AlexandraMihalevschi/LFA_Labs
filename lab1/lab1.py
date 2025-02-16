import random

class Grammar:
    def __init__(self, VN, VT, P, start_symbol):
        self.VN = VN  # Non-terminals
        self.VT = VT  # Terminals
        self.P = P    # Production rules
        self.start_symbol = start_symbol

    def generate_string(self, symbol=None):
        if symbol is None:
            symbol = self.start_symbol

        if symbol in self.VT:
            return symbol
        
        if symbol not in self.P:
            return ""
        
        production = random.choice(self.P[symbol])
        return "".join(self.generate_string(s) for s in production)

    def generate_n_strings(self, n=5):
        
        return [self.generate_string() for _ in range(n)]

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

class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, start_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states

    def accepts(self, input_string):
        return self._accepts_helper(input_string, self.start_state)

    def _accepts_helper(self, remaining, current_state):
        if not remaining:
            return current_state in self.final_states
        symbol = remaining[0]
        next_states = self.transitions.get((current_state, symbol), set())
        for state in next_states:
            if self._accepts_helper(remaining[1:], state):
                return True
        return False

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
