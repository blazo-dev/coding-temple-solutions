# 📌 Overview
# Learn to create decision-making logic in Python using if, elif, else, and nested conditionals.

# 🐍 Conditional Logic in Python

# Conditional statements allow decisions based on conditions:
# if: Tests if a condition is true.
# elif: Checks multiple conditions.
# else: Executes if none of the above conditions are true.

# Example:
raining = True
if raining:
    print("Bring an Umbrella")
else:
    print("Wear Sunglasses")

# 📝 Syntax
# Python uses indentation to define the scope.
# Example:
x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# 🛠 Comparison and Logical Operators:
# Comparison Operators: ==, !=, >, <, >=, <=
# Logical Operators: and, or, not
age = 25
is_student = True
if age >= 18 and is_student:
    print("Eligible for student discount.")

# 🧠📓 Engage & Apply:
# Program to suggest an activity based on weather and mood.
weather = input("Weather: sunny or raining? ").lower()
mood = input("Mood: happy or tired? ").lower()

if weather == "sunny" and mood == "happy":
    print("Go for a hike!")
elif weather == "raining" or mood == "tired":
    print("Relax indoors.")

# 🏞 Nested Conditional Statements:
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive and even.")
    else:
        print("Positive and odd.")
else:
    print("Not positive.")

# 🛑 Common Pitfalls and Tips:
# 1. Incorrect Indentation: Use consistent 4 spaces.
# 2. Using multiple ifs instead of elif: Use elif for mutually exclusive conditions.
x = 5
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# 3. Confusing = (assignment) with == (comparison):
bootcamp = "coding temple"
if bootcamp == "coding temple":
    print("Best bootcamp ever!")
