import re

# Metacharacters

# 1. Dot . - The Wildcard Character
pattern = r"c.t"
test_sentence = "I found a cat, a cot, and a cut in the room."
matches = re.findall(pattern, test_sentence)
print("Matches for 'c.t':", matches)

# 2. Caret ^ - The Beginning Anchor
pattern = r"^Py"
test_sentence = "Python is fun Py"
matches = re.findall(pattern, test_sentence)
print("Matches for '^Py':", matches)

# 3. Dollar $ - The End Anchor
pattern = r"fun$"
test_sentence = "Learning regex is fun"
matches = re.findall(pattern, test_sentence)
print("Matches for 'fun$':", matches)

# 4. Asterisk * - Zero or More Occurrences
pattern = r"ba*"
test_sentence = "I saw a bat, and a ball in my bed, baaah!"
matches = re.findall(pattern, test_sentence)
print("Matches for 'ba*':", matches)

# 5. Plus + - One or More Occurrences
pattern = r"ba+"
test_sentence = "The battle of ba and baat."
matches = re.findall(pattern, test_sentence)
print("Matches for 'ba+':", matches)

# 6. Question Mark ? - Zero or One Occurrence Making a Character Optional
pattern = r"colou?r"
test_sentence = "The color is nice. I like this colour."
matches = re.findall(pattern, test_sentence)
print("Matches for 'colou?r':", matches)

# 7. Backslash \ - Escaping Special Characters
pattern = r"\."
test_sentence = "End of sentence. Start of a new one."
matches = re.findall(pattern, test_sentence)
print("Matches for '\\.':", matches)

# 8. Square Brackets [] - Character Sets
pattern = r"R[aeiou]"
test_word = "Regular Radicals"
matches = re.findall(pattern, test_word)
print("Matches for 'R[aeiou]':", matches)

# 9. Pipe | - The OR Operator
pattern = r"cat|dog|cow|hamster"
test_sentence = "I have a cat and a dog."
matches = re.findall(pattern, test_sentence)
print("Matches for 'cat|dog|cow|hamster':", matches)

# 10. Parentheses () - Grouping
pattern = r"(woof|meow)+"
test_sentence = "The pets say woof woof and meow."
matches = re.findall(pattern, test_sentence)
print("Matches for '(woof|meow)+':", matches)

# Special Sequences

# 11. Curly Braces {} - Specifying Exact Occurrences
pattern = r"lo{2}"
test_sentence = "Look at the loom and the balloon in the room."
matches = re.findall(pattern, test_sentence)
print("Matches for 'lo{2}':", matches)

# 12. \d - Hunts down digits
pattern = r"\d{3}-\d{3}-\d{4}"
test_sentence = "Call me at 123-456-7890 or 987-654-3210."
matches = re.findall(pattern, test_sentence)
print("Matches for '\\d{3}-\\d{3}-\\d{4}':", matches)

# 13. \w - Finds word characters
pattern = r"\w*\d\w*"
test_sentence = "My username is user123 and my password is pass99word."
matches = re.findall(pattern, test_sentence)
print("Matches for '\\w*\\d\\w*':", matches)

# 14. \s - Seeks out whitespace
pattern = r"\s+"
test_sentence = "Welcome to the world of regex!"
matches = re.findall(pattern, test_sentence)
print("Matches for '\\s+':", matches)

# 15. \D - Finds non-digit characters
pattern = r"\D+"
test_sentence = "Room 101 is on floor 3"
matches = re.findall(pattern, test_sentence)
print("Matches for '\\D+':", matches)

# 16. \W - Matches non-word characters
pattern = r"\W"
test_sentence = "Hello, world! Are you ready?"
matches = re.findall(pattern, test_sentence)
print("Matches for '\\W':", matches)

# 17. \S - Identifies non-whitespace characters
pattern = r"\S"
test_sentence = "Python 3.12 - New Features"
matches = re.findall(pattern, test_sentence)
print("Matches for '\\S':", matches)

# 18. \b - Word boundary
pattern = r"\bPy\w*"
test_sentence = "Python is easy. Typing is fun."
matches = re.findall(pattern, test_sentence)
print("Matches for '\\bPy\\w*':", matches)

# 19. \B - Non-word boundary
pattern = r"\Bll\B"
test_sentence = "The yellow mellow mushroom illuminated the room."
matches = re.findall(pattern, test_sentence)
print("Matches for '\\Bll\\B':", matches)
