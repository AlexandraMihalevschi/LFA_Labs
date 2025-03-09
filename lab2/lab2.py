class Grammar:
    def __init__(self, non_terminals, terminals, productions):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.productions = productions

    def classify(self):
        is_regular = True
        is_context_free = True
        is_context_sensitive = True

        for production in self.productions:
            lhs, rhs = production.split('→')  # Split the rule into lhs and rhs
            lhs = lhs.strip()  # Remove any extra spaces
            rhs = rhs.strip()

            # Type 3 (Regular Grammar) check
            if not (len(lhs) == 1 and lhs.isupper() and 
                    (rhs.islower() or (len(rhs) == 2 and rhs[0].islower() and rhs[1].isupper()))):
                is_regular = False  # If any rule does not match the regular grammar format

            # Type 2 (Context-Free Grammar) check
            if not (len(lhs) == 1 and lhs.isupper()):
                is_context_free = False  # If any rule has a left-hand side longer than 1 symbol

            # Type 1 (Context-Sensitive Grammar) check
            if len(lhs) > len(rhs):
                is_context_sensitive = False  # If any LHS is longer than RHS, it's not context-sensitive

        # Determine the grammar type based on the checks
        if is_regular:
            return "Type 3 (Regular)"
        elif is_context_free:
            return "Type 2 (Context-Free)"
        elif is_context_sensitive:
            return "Type 1 (Context-Sensitive)"
        else:
            return "Type 0 (Recursively Enumerable)"

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

    def convert_ndfa_to_dfa(self):
        # NDFA to DFA conversion using subset construction
        dfa_states = [frozenset([self.start_state])]
        dfa_transitions = {}
        dfa_final_states = set()

        state_map = {frozenset([self.start_state]): 'A'}
        unprocessed_states = [frozenset([self.start_state])]  # List to keep track of states to process

        print("NFA to DFA State Mapping:")
        while unprocessed_states:
            current_state = unprocessed_states.pop()
            current_state_name = state_map[current_state]
            print(f"NFA State: {sorted(current_state)} -> DFA State: {current_state_name}")

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

# Define the FA based on the provided transitions
states = ['q0', 'q1', 'q2', 'q3']
alphabet = ['a', 'b', 'c']
transitions = {
    'q0': {'a': ['q0', 'q1']},
    'q1': {'b': ['q2']},
    'q2': {'a': ['q2'], 'b': ['q3']},
    'q3': {'a': ['q3']}
}
start_state = 'q0'
final_states = ['q3']

fa = FiniteAutomaton(states, alphabet, transitions, start_state, final_states)

# Check if the FA is deterministic
is_deterministic = fa.is_deterministic()
print(f"The FA is deterministic: {is_deterministic}")

# Convert FA to regular grammar
non_terminals, grammar_rules = fa.convert_to_regular_grammar()
print(f"Non-terminals: {non_terminals}")
print(f"Grammar rules: {grammar_rules}")

# Define the regular grammar based on the FA conversion
productions = grammar_rules
grammar = Grammar(non_terminals={key for key in non_terminals.values()}, terminals=set(alphabet), productions=productions)

# Classify the grammar
classification = grammar.classify()
print(f"The grammar is classified as: {classification}")

# Convert NDFA to DFA
dfa_states, dfa_transitions, dfa_final_states = fa.convert_ndfa_to_dfa()
print(f"DFA States: {dfa_states}")
print(f"DFA Transitions: {dfa_transitions}")
print(f"DFA Final States: {dfa_final_states}")

# Generate DFA DOT file
fa.write_dfa_to_dot(dfa_states, dfa_transitions, dfa_final_states)
print("DFA DOT file has been generated as dfa.dot.")

# Define the grammar components for the given variant
vn = {'S', 'A', 'B', 'C'}
vt = {'a', 'b'}
p = [
    'S → aA',
    'A → bS',
    'S → aB',
    'B → aC',
    'C → a',
    'C → bS'
]

# Create a Grammar instance
specific_grammar = Grammar(vn, vt, p)

# Classify the grammar
grammar_type = specific_grammar.classify()

# Print results
print("\nGrammar Analysis Results:")
print("Non-terminals (VN):", vn)
print("Terminals (VT):", vt)
print("Productions (P):", p)
print("Grammar Classification:", grammar_type)