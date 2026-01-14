# Use the re module to write a script that searches through a paragraph and extracts all words that start with an uppercase 
# letter (e.g., "London", "Python") to identify proper nouns or sentence starters.

import re

paragraph = """Python is a popular programming language. It is begineer friendly. It is high level language.London is beautiful city"""

# Regular expression to find words starting with uppercase letters
# \b = word boundary, [A-Z] = uppercase letter, \w* = rest of the word
uppercase_words = re.findall(r'\b[A-Z]\w*', paragraph)

print("Words starting with uppercase letters:")
print(uppercase_words)