from typing import Set, Dict, List
from collections import defaultdict, deque

class GrammarCNFConverter:
    def __init__(self, non_terminals: Set[str], terminals: Set[str],
                 productions: Dict[str, List[List[str]]], start_symbol: str):
        self.VN = non_terminals
        self.VT = terminals
        self.P = productions
        self.S = start_symbol

    def eliminate_epsilon_productions(self):
        nullable = set()
        changed = True
        while changed:
            changed = False
            for A in self.P:
                for prod in self.P[A]:
                    if all(symbol in nullable or symbol == 'ε' for symbol in prod):
                        if A not in nullable:
                            nullable.add(A)
                            changed = True

        new_P = defaultdict(list)
        for A in self.P:
            for prod in self.P[A]:
                options = [[]]
                for symbol in prod:
                    new_options = []
                    for option in options:
                        if symbol in nullable:
                            new_options.append(option[:])  # omit symbol
                        new_options.append(option + [symbol])  # include symbol
                    options = new_options
                for option in options:
                    if option and option != ['ε']:
                        new_P[A].append(option)
        self.P = new_P

    def eliminate_unit_productions(self):
        unit_pairs = set()
        for A in self.P:
            for prod in self.P[A]:
                if len(prod) == 1 and prod[0] in self.VN:
                    unit_pairs.add((A, prod[0]))

        while True:
            new_pairs = set(unit_pairs)
            for (A, B) in unit_pairs:
                for prod in self.P.get(B, []):
                    if len(prod) == 1 and prod[0] in self.VN:
                        new_pairs.add((A, prod[0]))
            if new_pairs == unit_pairs:
                break
            unit_pairs = new_pairs

        new_P = defaultdict(list)
        for A in self.P:
            for prod in self.P[A]:
                if not (len(prod) == 1 and prod[0] in self.VN):
                    new_P[A].append(prod)
        for (A, B) in unit_pairs:
            for prod in self.P.get(B, []):
                if not (len(prod) == 1 and prod[0] in self.VN):
                    new_P[A].append(prod)
        self.P = new_P

    def eliminate_non_productive_symbols(self):
        productive = set()
        changed = True
        while changed:
            changed = False
            for A in self.P:
                for prod in self.P[A]:
                    if all(symbol in productive or symbol in self.VT for symbol in prod):
                        if A not in productive:
                            productive.add(A)
                            changed = True

        self.VN = {A for A in self.VN if A in productive}
        self.P = {A: [prod for prod in self.P[A] if all(symbol in productive or symbol in self.VT for symbol in prod)]
                  for A in self.VN}

    def eliminate_inaccessible_symbols(self):
        reachable = set()
        queue = deque([self.S])
        while queue:
            A = queue.popleft()
            if A not in reachable:
                reachable.add(A)
                for prod in self.P.get(A, []):
                    for symbol in prod:
                        if symbol in self.VN:
                            queue.append(symbol)

        self.VN = reachable
        self.P = {A: self.P[A] for A in self.VN}

    def convert_to_cnf(self):
        terminal_map = {}
        counter = 1
        new_productions = defaultdict(list)

        for A in self.P:
            for prod in self.P[A]:
                new_prod = []
                for symbol in prod:
                    if symbol in self.VT and len(prod) > 1:
                        if symbol not in terminal_map:
                            new_var = f"T{counter}"
                            counter += 1
                            terminal_map[symbol] = new_var
                            self.VN.add(new_var)
                            new_productions[new_var].append([symbol])
                        new_prod.append(terminal_map[symbol])
                    else:
                        new_prod.append(symbol)
                new_productions[A].append(new_prod)

        def binarize(prod):
            nonlocal counter
            if len(prod) <= 2:
                return [prod]
            result = []
            curr = prod[0]
            for i in range(1, len(prod) - 1):
                new_var = f"X{counter}"
                counter += 1
                self.VN.add(new_var)
                result.append([curr, new_var])
                curr = new_var
            result.append([curr, prod[-1]])
            return result

        final_productions = defaultdict(list)
        for A in new_productions:
            for prod in new_productions[A]:
                if len(prod) <= 2:
                    final_productions[A].append(prod)
                else:
                    bins = binarize(prod)
                    final_productions[A].append(bins[0])
                    for rule in bins[1:]:
                        final_productions[rule[0]].append(rule)

        self.P = final_productions

    def convert(self):
        self.eliminate_epsilon_productions()
        self.eliminate_unit_productions()
        self.eliminate_non_productive_symbols()
        self.eliminate_inaccessible_symbols()
        self.convert_to_cnf()

    def print_grammar(self):
        print("\n--- Grammar ---")
        print("Non-terminals:", self.VN)
        print("Terminals:", self.VT)
        print("Start Symbol:", self.S)
        print("Productions:")
        for A in self.P:
            for prod in self.P[A]:
                print(f"  {A} → {' '.join(prod)}")


def input_grammar():
    print("Enter comma-separated non-terminals (e.g., S,A,B):")
    non_terminals = set(input().strip().split(','))
    
    print("Enter comma-separated terminals (e.g., a,b):")
    terminals = set(input().strip().split(','))
    
    print("Enter start symbol:")
    start_symbol = input().strip()

    print("Enter productions (e.g., S->aB|bA|B; A->b|aD|AS|bAB|ε):")
    productions_input = input().strip().split(';')
    productions = defaultdict(list)
    for line in productions_input:
        head, body = line.split('->')
        options = body.split('|')
        for option in options:
            if option == 'ε':
                productions[head.strip()].append(['ε'])
            else:
                productions[head.strip()].append(list(option.strip()))
    return non_terminals, terminals, productions, start_symbol


if __name__ == "__main__":
    choice = input("Use example grammar? (y/n): ").lower()
    if choice == 'y':
        non_terminals = {"S", "A", "B", "C", "D"}
        terminals = {"a", "b"}
        productions = {
            "S": [["a", "B"], ["b", "A"], ["B"]],
            "A": [["b"], ["a", "D"], ["A", "S"], ["b", "A", "B"], ["ε"]],
            "B": [["a"], ["b", "S"]],
            "C": [["A", "B"]],
            "D": [["B", "B"]]
        }
        start_symbol = "S"
    else:
        non_terminals, terminals, productions, start_symbol = input_grammar()

    grammar = GrammarCNFConverter(non_terminals, terminals, productions, start_symbol)
    print("\nOriginal Grammar:")
    grammar.print_grammar()

    grammar.convert()
    print("\nConverted to Chomsky Normal Form:")
    grammar.print_grammar()
