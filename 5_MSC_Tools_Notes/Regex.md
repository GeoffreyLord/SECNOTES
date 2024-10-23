
# Regular Expressions (Regex) Notes
## Overview
Regular Expressions (Regex) are sequences of characters that form search patterns. They are used for pattern matching, text searching, and replacing within strings. Regex is widely used in various programming languages (e.g., Python, JavaScript) and command-line tools (e.g., grep, sed) to filter, search, and manipulate text.

## Common Regex Symbols
1. Basic Characters
    - Description: Matches literal characters.
    - Example:
        - ```hello```: Matches the exact string "hello".
2. Dot (```.```)
    - Description: Matches any single character except newline.
    - Example:
        - ```h.llo```: Matches "hello", "hallo", "hxllo".
3. Asterisk (```*```)
    - Description: Matches 0 or more occurrences of the preceding element.
    - Example:
        - ```a*```: Matches "", "a", "aa", "aaa", etc.
4. Plus (```+```)
    - Description: Matches 1 or more occurrences of the preceding element.
    - Example:
        - ```a+```: Matches "a", "aa", "aaa" (but not "").
5. Question Mark (```?```)
    - Description: Matches 0 or 1 occurrence of the preceding element.
    - Example:
        - ```colou?r```: Matches "color" or "colour".
6. Caret (```^```)
    - Description: Matches the start of a string.
    - Example:
        - ```^hello```: Matches "hello" at the beginning of a string.
7. Dollar Sign (```$```)
    - Description: Matches the end of a string.
    - Example:
        - ```world$```: Matches "world" at the end of a string.
8. Square Brackets (```[]```)
    - Description: Matches any one character from a set.
    - Example:
        - ```[aeiou]```: Matches any vowel ("a", "e", "i", "o", "u").
9. Dash (```-```)
    - Description: Specifies a range of characters inside square brackets.
    - Example:
        - ```[0-9]```: Matches any digit between 0 and 9.
        - ```[a-z]```: Matches any lowercase letter.
10. Pipe (```|```)
    - Description: Acts as an OR operator.
    - Example:
        - ```cat|dog```: Matches either "cat" or "dog".

## Quantifiers
1. Exact Number ```{n}```
    - Description: Matches exactly ```n``` occurrences of the preceding element.
    - Example:
        - ```a{3}```: Matches "aaa" only.
2. Range ```{n,m}```
    - Description: Matches between ```n``` and ```m``` occurrences.
    - Example:
        - ```a{2,4}```: Matches "aa", "aaa", or "aaaa".

## Special Sequences
1. Word Boundaries (```\b```)
    - Description: Matches a word boundary (start or end of a word).
    - Example:
        - ```\bword\b```: Matches "word" as a whole word.
2. Digit (```\d```)
    - Description: Matches any digit (equivalent to [0-9]).
    - Example:
        - ```\d```: Matches any digit, such as "1", "9", "0".
3. Non-Digit (```\D```)
    - Description: Matches any non-digit character.
    - Example:
        - ```\D```: Matches any non-digit character.
4. Whitespace (```\s```)
    - Description: Matches any whitespace character (space, tab, newline).
    - Example:
        - ```\s```: Matches a space, tab, or newline.
5. Non-Whitespace (```\S```)
    - Description: Matches any non-whitespace character.
    - Example:
        - ```\S```: Matches any character except whitespace.

## Grouping and Backreferences
1. Parentheses (```()```)
    - Description: Groups multiple tokens together.
    - Example:
        - ```(abc)+```: Matches "abc", "abcabc", etc.
2. Backreference (```\1```, ```\2```, etc.)
    - Description: Refers to matched groups in the regular expression.
    - Example:
        - ```(.)\1```: Matches two consecutive identical characters (e.g., "aa", "bb").

## Escape Special Characters
- Description: Use a backslash (``` \ ```) to escape special characters and treat them as literals.
    - Example:
        - ```\.```: Matches a literal period (".").

## Final Notes
- Regex is a powerful tool for text manipulation and pattern matching.
- Best Practices: Always test your regular expressions with tools like regex101.com to ensure they behave as expected.