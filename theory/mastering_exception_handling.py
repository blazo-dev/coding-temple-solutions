# 📌 Brief Overview
# By the end of this lesson, you will have a solid understanding of Python's exception handling mechanisms,
# enabling you to write more robust and error-tolerant code. You'll learn how to identify and handle common exceptions
# using the try, except, else, and finally blocks, as well as how to raise predefined and custom exceptions.

# 🐍 Safeguarding Your Code - Python Exception Handling

# What are Errors and Exceptions?
# Definition:
# - Syntax errors occur when the Python interpreter encounters a statement that breaks the rules of the language syntax.
# - Exceptions are errors detected during execution.

# Common Exception Types:
# - ZeroDivisionError: Trying to divide by zero.
# - TypeError: An operation or function is applied to an object of inappropriate type.
# - ValueError: A function receives an argument of the right type but inappropriate value.

# Examples of Common Exceptions:
# # Syntax Error
# if True
#     print("Hello")  # Missing colon at the end of if statement

# # Runtime Exception
# x = 1 / 0  # This will raise ZeroDivisionError

# Basic Exception Handling with try and except
# The try block lets you test a block of code for errors, while the except block lets you handle the error.

# Basic Syntax:
try:
    # Code that may raise an exception
    x = 10 / 0  # Example of ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by zero!")

# 🧠📓 Engage & Apply:
# Write a program that prompts the user for two numbers, then divides the first by the second.
# Handle the exceptions where the user enters invalid data (non-numeric) or tries to divide by zero.

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("You must enter valid numbers.")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(f"The result is {result}")
finally:
    print("Execution complete!")

# Catching Multiple Exceptions
# You can handle multiple exceptions by specifying multiple except blocks or catching multiple exceptions in a single block.

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")

# Catching Multiple Exceptions in One Block:
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")

# Catching Any Exception in One Block:
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except:
    print(f"An error occurred!")

# else and finally Clauses
# The else block is executed if no exceptions occur in the try block.
# The finally block is executed no matter what, regardless of whether an exception occurred.

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result is {result}")
finally:
    print("Execution complete!")

# Best Practices for Exception Handling:
# - Catch specific exceptions rather than a generic except.
# - Only use exceptions for error handling, not for regular control flow.
# - Avoid swallowing exceptions silently without logging or taking action.
