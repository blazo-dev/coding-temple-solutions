# 📌 Brief Overview
# This lesson covers the fundamentals of Python functions, including how to define and call functions, use parameters and arguments, and understand function scope (local vs. global variables). By the end, you will be able to write cleaner, modular code using functions.

# 🐍 Function Mastery in Python

# What are Functions?
# Functions are reusable blocks of code designed to perform specific tasks. They improve code organization, reduce duplication, and enhance maintainability.


# Example of defining and calling a function:
def greet():
    print("Hello, welcome to coding temple!")


greet()  # Calls the function, output: Hello, welcome to coding temple!

# Parameters and Arguments:
# Parameters are variables defined in the function signature, and arguments are the values passed to the function when it is called.


def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")


greet("Alice")  # 'Alice' is the argument, output: Hello, Alice!


# 🧠📓 Engage & Apply
# Create a function introduce_yourself that takes a name and a favorite hobby, and prints a personalized greeting.
def introduce_yourself(name, hobby):
    print(
        f"Hello, {name}! Correct me if I'm wrong, but your favorite hobby is {hobby}!"
    )


introduce_yourself(
    "Christian", "coding"
)  # Output: Hello, Christian! Correct me if I'm wrong, but your favorite hobby is coding!
introduce_yourself(
    "Travis", "photography"
)  # Output: Hello, Travis! Correct me if I'm wrong, but your favorite hobby is photography!


# Return Statements:
# Functions can return values using the 'return' keyword, which allows for reusable outputs.
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)
print(result)  # Output: 8

# Function Scope (Local vs Global Variables):
# Local variables are defined inside a function, while global variables are defined outside and can be accessed anywhere.
x = 10  # global variable


def print_number():
    x = 5  # local variable
    print(x)  # Output: 5


print_number()
print(x)  # Output: 10


# Default Parameters & Variable-Length Arguments:
# Default parameters have predefined values used when no argument is passed.
def greet(name="Student"):
    print(f"Hello, {name}!")


greet()  # Output: Hello, Student!
greet("Alice")  # Output: Hello, Alice!


# *args: Allows passing a variable number of non-keyword arguments (received as a tuple).
# **kwargs: Allows passing a variable number of keyword arguments (received as a dictionary).
def add_numbers(*args):
    return sum(args)  # Sums all values passed as non-keyword arguments


print(add_numbers(1, 2, 3))  # Output: 6
print(add_numbers(5, 10))  # Output: 15
