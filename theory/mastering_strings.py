# Creating Strings
name = "John"
greeting = 'Hello!'

# Multi-line Strings
multi_line = '''This is a 
multi-line string.'''

# String Indexing
word = "Python"
print(word[0])  # 'P'
print(word[2])  # 't'

# String Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # 'John Doe'

# Repetition
repeated = "Wow! " * 3  # 'Wow! Wow! Wow!'

# Length of a String
print(len("Python"))  # 6

# String Slicing
language = "Python"
print(language[0:3])  # 'Pyt'
print(language[3:])   # 'hon'
print(language[-1])   # 'n'

# String Methods
message = " Hello, Python! "
print(message.upper())    # ' HELLO, PYTHON! '
print(message.lower())    # ' hello, python! '
print(message.strip())    # 'Hello, Python!'
print(message.replace("Python", "World"))  # ' Hello, World! '
print(message.split())    # ['Hello,', 'Python!']

# Joining Strings
words = ["Python", "is", "fun"]
sentence = " ".join(words)  # 'Python is fun'

# Check Start and End
filename = "report.pdf"
print(filename.endswith(".pdf"))  # True

# String Formatting
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))  # Using format()
print(f"My name is {name} and I am {age} years old.")  # Using f-strings

# Immutability of Strings
text = "hello"
text = "H" + text[1:]  # 'Hello'
