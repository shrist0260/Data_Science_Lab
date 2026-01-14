# Write a Python script that takes a list of six student names and uses the random.sample() function to randomly select
# exactly three "Volunteers" for a presentation, ensuring that no student is picked more than once in the selection.

import re

paragraph = """
Python is a popular programming language. London is a beautiful city.
Many Developers love Python for its simplicity and versatility.
"""

# Regular expression to find words starting with uppercase letters
# \b = word boundary, [A-Z] = uppercase letter, \w* = rest of the word
uppercase_words = re.findall(r'\b[A-Z]\w*', paragraph)

print("Words starting with uppercase letters:")
print(uppercase_words)