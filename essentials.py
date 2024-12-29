# Introduction to Python 🐍
# Download Python: https://www.python.org/downloads/
# Download VS Code: https://code.visualstudio.com/

print("Hello, World! Welcome to Python 🐍")  # Your first Python command

# 2. Variables ✅
x = 10  # Integer
y = 3.14  # Float
name = "Bryan"  # String
is_coding = True  # Boolean
print(f"Variables: x={x}, y={y}, name={name}, is_coding={is_coding}")

# 3. Arithmetic 🧮
sum = x + y
product = x * y
division = x / y
integer_division = x // 3
modulo = x % 3
print("Arithmetic:\nSum:", sum, "\nProduct:", product, "\nDivision:", division, "\nInteger Division:", integer_division, "\nModulo:", modulo)

# 4. Typecasting 💱
integer_value = int(y)  # Float to integer
string_value = str(x)  # Integer to string
float_value = float(x)  # Integer to float
print(f"Typecasting: Integer={integer_value}, String='{string_value}', Float={float_value}")

# 5. User Input ⌨
# Uncomment the lines below to use input interactively
# user_name = input("What's your name? ")
# print(f"Hello, {user_name}! Welcome to Python 🐍")

# 6. If Statements 🤔
age = 20
if age < 18:
    print("You're a minor.")
elif age == 18:
    print("You're 18!")
else:
    print("You're an adult.")

# 7. Logical Operators 🔣
number = 10
if number > 5 and number < 15:
    print("The number is between 5 and 15.")
if number < 5 or number > 15:
    print("The number is outside the range 5 to 15.")
if not number == 20:
    print("The number is not 20.")

# 8. While Loops ♾
i = 0
while i < 5:
    print(f"While loop iteration {i}")
    i += 1

# 9. For Loops 🔂
for i in range(5):
    print(f"For loop iteration {i}")

# 10. Countdown Timer 🎊
import time
countdown = 5
while countdown > 0:
    print(countdown)
    time.sleep(1)
    countdown -= 1
print("Happy New Year! 🎉")

# 11. Lists, Tuples, Sets 📃
# List (Mutable)
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(f"List: {fruits}")

# Tuple (Immutable)
vegetables = ("carrot", "broccoli", "spinach")
print(f"Tuple: {vegetables}")

# Set (Unique values, Unordered)
unique_numbers = {1, 2, 2, 3, 4}
unique_numbers.add(5)
print(f"Set: {unique_numbers}")
