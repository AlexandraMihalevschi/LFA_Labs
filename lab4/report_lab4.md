# Laboratory Work: Regular Expressions

**Course:** Formal Languages & Finite Automata\
**Author:** Mihalevschi Alexandra

## Theory

Regular expressions, commonly known as regex, are powerful tools used for pattern matching and manipulation in strings. They are widely utilized in programming, text processing, data validation, and even data scraping to search, match, extract, and replace text based on defined patterns. A regex defines a search pattern using a combination of literal characters and metacharacters, allowing users to express complex text rules concisely. Regular expressions are highly versatile, providing unmatched flexibility in handling text and string operations, but they can be challenging to master due to their cryptic syntax. However, once mastered, regex can significantly enhance the efficiency of text-based tasks. In this laboratory work, I will explore the fundamental concepts of regular expressions, their syntax, and their applications in various programming languages. I will also discuss the history and evolution of regular expressions, their components, and their significance in the field of computer science.

### History and Evolution of Regular Expressions

The concept of regular expressions was introduced in the 1950s by mathematician Stephen Kleene, who developed a notation to describe regular languages. The term "regular expression" itself was coined as part of automata theory and formal language theory. Ken Thompson later implemented regex in text editors for early Unix systems, which significantly influenced the popularity of regular expressions in computer science. Over time, support for regular expressions expanded across programming languages, making it a fundamental tool for pattern matching.

### Components of Regular Expressions

1.  **Literals**: These are ordinary characters that match themselves. For instance, the regex "hello" matches the string "hello" exactly. Literals can include letters, digits, and symbols that are not treated as special characters by the regex engine. For example, "hello" matches "hello", "Hello", and "h3llo".

2.  **Metacharacters**: These are special characters that define the behavior of the regex pattern. For example:

    - `.`: Matches any character except a newline. For instance, "c.t" matches "cat", "cot", or "cut".

    - `^`: Anchors the pattern to the start of the string, ensuring the match only occurs at the beginning.

    - `$`: Anchors the pattern to the end of the string, ensuring the match only occurs at the end.

    - `*`: Matches zero or more occurrences of the preceding character, making it highly versatile.

    - `+`: Matches one or more occurrences of the preceding character.

    - `?`: Matches zero or one occurrence of the preceding character, often used for optional characters.

    - `|`: Acts as a logical OR, allowing one of multiple options to match. For example, "dog|cat" matches either "dog" or "cat".

3.  **Character Classes and Ranges**: Character classes allow matching a set of characters. Ranges are defined within square brackets:

    - `[a-z]`: Matches any lowercase letter from a to z.

    - `[A-Z]`: Matches any uppercase letter from A to Z.

    - `[0-9]`: Matches any digit from 0 to 9.

    - `[^a-z]`: Negates the match, matching any character except lowercase letters.

    - Predefined character classes include:

      - `\d`: Matches any digit (equivalent to [0-9]).

      - `\w`: Matches any word character (alphanumeric and underscore).

      - `\s`: Matches any whitespace character (spaces, tabs, newlines).

4.  **Grouping and Capturing**: Parentheses `()` group patterns together and capture matched substrings. For example, `(\d{3})-(\d{4})` matches phone numbers like 123-4567 and captures groups. Capturing groups allow retrieval of specific parts of the match. Non-capturing groups, `(?:pattern)`, group without storing the match. They are useful for grouping without capturing.

5.  **Quantifiers**: Specify how many times a character or group should match. Common quantifiers include:

    - `{n}`: Matches exactly n times.

    - `{n,}`: Matches at least n times.

    - `{n,m}`: Matches between n and m times.

### Using Regular Expressions in Programming

In Python, the `re` module provides powerful regex capabilities. Here are some common functions:

- `re.match`: Determines if the pattern matches at the start of the string.

- `re.search`: Finds the first match of the pattern in the string.

- `re.findall`: Returns a list of all matches in the string.

- `re.sub`: Replaces matched patterns with a replacement string.

- `re.split`: Splits a string by occurrences of a pattern.

### Advanced Concepts in Regular Expressions

Regular expressions also support backreferences, lookahead, and lookbehind assertions. These advanced features enhance the expressiveness of regex patterns. Backreferences allow referencing previously matched groups, while lookahead and lookbehind assertions enable conditional matching based on surrounding text. These features are particularly useful in complex pattern matching scenarios:

- **Backreferences**: Refer to previously matched groups using `\1`, `\2`, etc., enabling repeated patterns. For instance, `(\w+)\s+\1` matches repeated words.

- **Lookahead and Lookbehind**: Allow matching based on the surrounding text without consuming it. They are useful for complex pattern matching. For example:

  - Positive Lookahead: `(?=pattern)` ensures the match is followed by the pattern.

  - Negative Lookahead: `(?!pattern)` ensures the match is NOT followed by the pattern.

  - Positive Lookbehind: `(?<=pattern)` ensures the match is preceded by the pattern.

  - Negative Lookbehind: `(?<!pattern)` ensures the match is NOT preceded by the pattern.

### Regex Generator Code Example

The provided regex generator code demonstrates how regex patterns can be interpreted to generate valid strings. It handles groups, repetition, power operators, and OR operators. This example illustrates how regex logic can be used creatively, not only for pattern matching but also for string generation. By understanding the core concepts of regular expressions, developers can craft efficient, powerful patterns for text manipulation. The code snippet showcases the versatility of regex patterns in various programming languages and applications. The code snippet is a testament to the power and versatility of regular expressions in text processing. It showcases how regex patterns can be interpreted to generate valid strings, highlighting their versatility in text manipulation.

### Conclusion

Regular expressions are indispensable tools in software development and data processing. Despite their complexity, mastering regex unlocks unparalleled capabilities for parsing, validating, and transforming text. Whether filtering logs, extracting data, or validating inputs, regex is a versatile tool that can handle a wide array of text-based tasks efficiently. By understanding the core concepts and mastering the syntax, developers can harness the full potential of regex to streamline their workflows and enhance the robustness of their applications.

## Objectives

The primary objectives of this laboratory work were:

1. Write and cover what regular expressions are, what they are used for;

2. Take a variant depending on your number in the list of students and do the following:

3. Write a code that will generate valid combinations of symbols conform given regular expressions (examples will be shown).

4. In case you have an example, where symbol may be written undefined number of times, take a limit of 5 times (to evade generation of extremely long combinations);

5. Bonus point: write a function that will show sequence of processing regular expression (like, what you do first, second and so on)

## Implementation Description

The regex generator code is a practical demonstration of how regular expressions can be parsed and used to generate valid strings based on a given regex pattern. This approach not only deepens understanding of regular expressions but also showcases how such patterns can be evaluated programmatically. The implementation handles multiple regex constructs, including groups, repetition, the OR operator, and a power operator.

#### **Code analysis**

1.  **Imports and Configuration:** The script begins by importing two essential modules: `re` for regex handling (though not directly used in the generation process) and `random` for generating random repetitions and selections. A constant `MAX_REPETITION` is set to control how many times a pattern can be repeated, preventing excessively long or infinite strings.

2.  **The** `generate_strings_from_regex` **Function:** This function serves as the entry point, accepting a regex string and invoking the nested `parse_expression` function to handle pattern interpretation and string generation. The output is a list containing valid strings that match the input regex.

3.  **The** `parse_expression` **Function:** This core function recursively parses the regex expression:

    - It iterates over the input expression, analyzing each character to determine its role.

    - **Groups:** When encountering a '(', the function locates the matching closing parenthesis using `find_closing_parenthesis` to isolate the subexpression, recursively generating a string based on the contained pattern.

    - **Repetition (Metacharacters \* + ?):** The function handles quantifiers by determining the number of repetitions and appending the result accordingly.

    - **OR Operator (|):** The logic handles alternation by accumulating options between '|' symbols and selecting one randomly.

    - **Power Operator (^):** This unique feature multiplies the preceding pattern a specified number of times.

    - **Literal Characters:** If the character is not a special operator, it is treated as a literal and appended to the result.

4.  **The** `find_closing_parenthesis` **Function:** This helper function identifies matching parentheses by counting nested pairs, preventing errors from unbalanced expressions.

5.  **Generating Strings:** After parsing, the script calls the generator twice to produce two example strings. The results demonstrate how different patterns can produce varied outputs based on repetition and alternation.

#### **Strengths and Limitations**

The regex generator code efficiently handles basic regex patterns and introduces a unique power operator. However, it has limitations:

- It does not fully parse or respect complex regex constructs, such as character classes, lookahead, and lookbehind assertions.

- Infinite repetition (e.g., unbounded \*) can cause long or hanging executions without a MAX_REPETITION cap.

#### Key Components of the Code

1. **`generate_strings_from_regex` Function**:
   This is the main function responsible for parsing the regular expression and generating strings based on it. It contains a helper function `parse_expression` which recursively processes the regex string.

   - **Input**: A regex pattern provided by the user (e.g., `(ab|cd)*`).
   - **Output**: A list of valid strings that match the given regex pattern.

2. **`parse_expression` Function**:
   This function is responsible for parsing different components of the regex and generating the corresponding string.

   - **Group Handling**: Parentheses `()` in regex are treated as grouping. When the parser encounters a group, it looks for the closing parenthesis and recursively processes the inner expression.

     ```python
     if char == "(":  # Handle groups
         end_idx = find_closing_parenthesis(expression, index)
         sub_exp = expression[index + 1:end_idx]
         index = end_idx
         sub_result = parse_expression(sub_exp)
         result.append(random.choice(sub_result))
     ```

   - **Repetition Operators**: Operators like `*`, `+`, and `?` modify the number of repetitions for the preceding element.

     - `*` allows zero or more repetitions.
     - `+` requires one or more repetitions.
     - `?` makes the preceding element optional (zero or one repetition).

     ```python
     elif char in "*+?":  # Handle repetition
         prev = result.pop() if result else ""
         if char == "*":
             result.append(prev * random.randint(0, MAX_REPETITION))
         elif char == "+":
             result.append(prev * random.randint(1, MAX_REPETITION))
         elif char == "?":
             result.append(prev if random.choice([True, False]) else "")
     ```

   - **Alternation (`|`)**: The OR operator in regex allows for one of several options. The parser processes all the alternatives and selects one at random.

     ```python
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
     ```

   - **Literal Characters**: Any character that is not part of a special regex operation is treated as a literal and is directly added to the result string.
     ```python
     else:  # Literal characters
         result.append(char)
     ```

3. **Helper Functions**:

   - **`find_closing_parenthesis`**: This function helps find the corresponding closing parenthesis for a given opening parenthesis in the regex. It's essential for handling groups correctly.
     ```python
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
     ```

4. **Randomness**:
   The function uses randomness at various points:

   - When deciding which option to choose in the alternation (`|`).
   - When determining how many repetitions to apply for the `*`, `+`, and `?` operators.
     This introduces variability in the output, so each time the function is run, it generates different valid strings based on the regex pattern.

5. **Input and Output**:

   - **Input**: The user is prompted to enter a regex pattern.
   - **Output**: The program generates two random valid strings that match the given pattern and prints them.

   Example:

   ```python
   regex_input = input("Enter a regular expression: ")
   valid_strings = [generate_strings_from_regex(regex_input) for _ in range(2)]
   print("Generated Strings:")
   for s in valid_strings:
       print(s)
   ```

## Expected Results

The expected results of running this code will depend on the regular expression (regex) provided by the user. The code is designed to generate two valid strings based on the given regex pattern. Here’s a breakdown of what each type of regex component would lead to in terms of output:

### 1. **Literal Characters**:

If the regex consists only of literal characters (e.g., `abc`), the output will directly match the input string.

**Example:**

- Input: `abc`
- Output: `abc` (or any variation if there are random elements like repetition, but here it’s straightforward).

### 2. **Groups (`()`)**:

When the regex includes groups (e.g., `(ab|cd)`), the program will generate a string that randomly selects one of the options within the group.

**Example:**

- Input: `(ab|cd)`
- Output: Could be either `ab` or `cd`, depending on the random choice made.

### 3. **Repetition Operators (`*`, `+`, `?`)**:

- `*` means "zero or more" repetitions of the preceding element.
- `+` means "one or more" repetitions of the preceding element.
- `?` means "zero or one" repetition of the preceding element.

The program will randomly generate a number of repetitions between 0 and `MAX_REPETITION`, or between 1 and `MAX_REPETITION` (in the case of `+`), or even omit the repetition entirely (in the case of `?`).

**Example:**

- Input: `a*`
- Output: A string containing from 0 to `MAX_REPETITION` `a`s, such as `aaaa`, `a`, or `""` (empty string).

- Input: `a+`
- Output: A string containing 1 to `MAX_REPETITION` `a`s, such as `aaa` or `aaaa`.

- Input: `a?`
- Output: A string containing either 0 or 1 `a`, such as `a` or `""` (empty string).

### 4. **Alternation (`|`)**:

The `|` operator allows for a choice between different options. The program will randomly choose one of the options.

**Example:**

- Input: `ab|cd`
- Output: Could be either `ab` or `cd`.

### 5. **Power Operator (`^`)**:

The `^` operator specifies that the preceding element should be repeated a certain number of times (defined by the number after `^`). The program will use this to multiply the previous element by a given power.

**Example:**

- Input: `a^3`
- Output: The string `aaa`, as `a` is repeated 3 times.

### Expected Output (Example Run):

For a given input regex like `(ab|cd)*a+`, the expected output might look like this:

**Input**: `(ab|cd)*a+`

- The program will generate strings that:
  - Choose either `ab` or `cd` repeatedly (zero or more times due to `*`).
  - End with one or more `a`s (due to `a+`).

**Possible Outputs**:

- `abca`
- `cdabaaa`
- `ab`
- `abcaaca`

These outputs are random, so each run will likely generate different strings that match the given regex.

## Output

Input:

    Enter a regular expression: M?N^2(O|P)^3Q*R+

Output:

    Generated Strings:
    ['NNPPPQRRRR']
    ['MNNOOOQQQRRRR']

Input:

    Enter a regular expression: (H|i)(J|K)L*N?

Output:

    Generated Strings:
    ['HJLL']
    ['iJLLLLLN']

Input:

    Enter a regular expression:  (X|Y|Z)^3 8+ (9|0)

Output:

    Generated Strings:
    ['YYY 8 9']
    ['YYY 8888 0']

## Conclusions

This lab provided me with a deeper understanding of regular expressions and their practical applications in Python. The ability to generate random strings based on a given regex pattern is a powerful tool for testing and validating various scenarios. The flexibility of the code allows for the generation of strings that adhere to complex patterns, making it a valuable tool for testing and validating systems that rely on regular expressions. The code's modularity and extensibility make it a useful starting point for more advanced projects involving regular expressions. Overall, this lab has enhanced my understanding of regular expressions and their practical applications in Python.

In addition, the hands-on experience allowed me to see the immediate impact of each component of a regular expression. Breaking the problem down—managing grouping, repetition, and alternation—showed me the importance of precision and attention to detail in programming. As I modified and experimented with different regex patterns, I grew more confident in my ability to predict the output and understand the underlying mechanics of the code.

Furthermore, working on this project highlighted the beauty and ingenuity of regular expressions. I came to appreciate how a simple set of rules and symbols can be combined in numerous ways to solve complex text processing challenges. This deeper dive into pattern matching has not only enriched my technical skills but also inspired me to explore more advanced topics within computer science and automation.

Overall, the lab not only bolstered my proficiency with Python's regex functionalities but also encouraged creative problem solving. I now feel better equipped to apply these concepts to real-world applications, whether it's validating user inputs, parsing large datasets, or automating routine tasks. This enriched understanding of regular expressions and their practical significance will undoubtedly serve as a cornerstone for my future projects.

## References

- Laboratory work guide - https://github.com/filpatterson/DSL_laboratory_works
- Python documentation - https://docs.python.org/3/
- Documentation on re module in Python - https://docs.python.org/3/library/re.html
