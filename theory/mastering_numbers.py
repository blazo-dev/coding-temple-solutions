# 📌 Brief Overview
# By the end of the lesson, you will understand how to work with integers in Python, perform basic arithmetic operations, and apply integer-related functions.

# 🐍 Working with Python Integers
# What is an Integer? Integers are whole numbers without any fractional or decimal part. They can be positive, negative, or zero.
# Python Representation: How integers are represented in Python.
a = 10  # positive integer
b = -5  # negative integer
c = 0   # zero
# Python allows arithmetic operations on integers, and they can be converted from strings or floats using the int() function.

# Basic Arithmetic Operations
# Addition, Subtraction, Multiplication, Division
x = 10
y = 5
print(x + y)  # --> 15  # Addition
print(x - y)  # --> 5  # Subtraction
print(x * y)  # --> 50  # Multiplication
print(x / y)  # --> 2.0  # Division (float result)

# NOTE: There are 2 ways to divide, "/" which returns a float data type (or a decimal). The second way is with "//", which will divide to the nearest whole number.

# Modulus (remainder of division):
print(x % y)  # --> 0  # Modulus

# Integer Division & Floor Division
# Integer Division: How division behaves when you want to get an integer result.
print(x // y)  # --> 2  # Floor division

# 🧠📓 Engage & Apply: Calculate the total cost of the following items. Then, apply a 10% discount and display the final amount.
milk = 5
eggs = 3
coffee = 10

total_cost = milk + eggs + coffee
final_amount = total_cost - (total_cost * 0.1)

print(f"Total Cost: ${total_cost}")
print(f"Final Amount after 10% discount: ${final_amount}")

# Exponentiation and Powers: Python allows you to raise a number to a specific power using the ** operator or the pow() function.
# Power Operator (**):
print(2 ** 3)  # -->  8 # 2 raised to the power of 3

# pow(): Another way to calculate powers (similar to ** )
print(pow(2, 3))  # --> 8

# Common Integer Functions
# abs(): Returns the absolute value of an integer.
print(abs(-10))  # --> 10

# round(): Rounds a number (if float is involved).
print(round(3.14))  # --> 3
print(round(3.56))  # --> 4

# Type Conversion (Casting)
# Converting Strings to Integers: Often in real-world scenarios, you’ll get numbers as strings.
num_str = "123"
num = int(num_str)
print(num + 1)  # --> 124

# NOTE: You can't perform arithmetic operations on a string data type. You must convert the string into an integer data type.

# 🛑 Common Integer Pitfalls and Tips
# Modulus with Negative Numbers: The result of the modulus operator (%) can be surprising with negative numbers.
# Tip: Remember that a % b always has the same sign as b.
print(-7 % 3)  # --> 2 # Because (-7 + 9) = 2

# Implicit Type Conversion (Coercion): When mixing integers and floats in operations, Python automatically converts the integer to a float.
print(3 + 2.0)  # --> 5.0  # (float), not 5 (integer)
