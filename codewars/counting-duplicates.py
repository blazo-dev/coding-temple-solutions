"""
Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive 
alphabetic characters and numeric digits that occur more than once in the input string. 
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
"""

from collections import Counter


def duplicate_count(text: str):
    lower_text = text.lower()
    char_count = Counter(lower_text)

    return sum(1 for count in char_count.values() if count > 1)


assert duplicate_count("abcde") == 0, "Expected 0 for input 'abcde'"
assert duplicate_count("aabbcde") == 2, "Expected 2 for input 'aabbcde'"
assert duplicate_count("aBabcde") == 2, "Expected 2 for input 'aBabcde'"
assert duplicate_count("indivisibility") == 1, "Expected 1 for input 'indivisibility'"
assert (
    duplicate_count("Indivisibilities") == 2
), "Expected 2 for input 'Indivisibilities'"
assert duplicate_count("aA11") == 2, "Expected 2 for input 'aA11'"
assert duplicate_count("ABBA") == 2, "Expected 2 for input 'ABBA'"

print("All tests passed :D")
