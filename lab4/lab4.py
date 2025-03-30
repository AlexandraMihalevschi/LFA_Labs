import re
import random

MAX_REPETITION = 5

# Helper function to parse regex and generate valid strings
def generate_strings_from_regex(regex):
    def parse_expression(expression):
        result = []
        index = 0

        while index < len(expression):
            char = expression[index]

            if char == "(":  # Handle groups
                end_idx = find_closing_parenthesis(expression, index)
                sub_exp = expression[index + 1:end_idx]
                index = end_idx
                sub_result = parse_expression(sub_exp)
                result.append(random.choice(sub_result))

            elif char in "*+?":  # Handle repetition
                prev = result.pop() if result else ""
                if char == "*":
                    result.append(prev * random.randint(0, MAX_REPETITION))
                elif char == "+":
                    result.append(prev * random.randint(1, MAX_REPETITION))
                elif char == "?":
                    result.append(prev if random.choice([True, False]) else "")

            elif char == "|":  # Handle OR operator correctly
                options = []
                current_option = ""

                options.append(result.pop() if result else "")

                while index < len(expression) and expression[index] != ")":
                    if expression[index] == "|":
                        index += 1  # Skip the | character
                        current_option = ""
                        while index < len(expression) and expression[index] != "|" and expression[index] != ")":
                            current_option += expression[index]
                            index += 1
                        options.append(current_option)
                    else:
                        index += 1
                result.append(random.choice(options))

            elif char == "^":  # Handle power operator
                prev = result.pop() if result else ""
                power_value = ""
                index += 1
                while index < len(expression) and expression[index].isdigit():
                    power_value += expression[index]
                    index += 1
                index -= 1
                result.append(prev * int(power_value))

            else:  # Literal characters
                result.append(char)

            index += 1
        return ["".join(result)]

    def find_closing_parenthesis(expression, start_index):
        open_count = 1
        for i in range(start_index + 1, len(expression)):
            if expression[i] == "(":
                open_count += 1
            elif expression[i] == ")":
                open_count -= 1
                if open_count == 0:
                    return i
        raise ValueError("Unmatched parenthesis in expression")

    return parse_expression(regex)

# Generate two valid strings from input regex
regex_input = input("Enter a regular expression: ")
valid_strings = [generate_strings_from_regex(regex_input) for _ in range(2)]
print("Generated Strings:")
for s in valid_strings:
    print(s)