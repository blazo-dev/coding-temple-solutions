"""
👾💻Final Challenge: Design a simple calculator that performs operations on two integers provided by the user.
Steps:

Ask the user to input two numbers.
Perform basic arithmetic operations (add, subtract, multiply, divide) on the inputs.
Display the results.
"""

print(
    """
👋 Welcome to the Python Integer Calculator! 🚀

Please follow the steps below to perform your calculations:

Let's get started! 🎉
"""
)

f_number = int(input("Enter the first number: "))
s_number = int(input("Enter the second number: "))

print(
    """
Choose the operation you would like to perform by typing the corresponding number:
   1️⃣ ➕ Addition  
   2️⃣ ➖ Subtraction  
   3️⃣ ✖️  Multiplication  
   4️⃣ ➗ Division
"""
)

operations = {
    1: lambda x, y: x + y,
    2: lambda x, y: x - y,
    3: lambda x, y: x * y,
    4: lambda x, y: x / y if y != 0 else "Error: Division by zero!",
}

operator_choice = int(input("Your choice: "))
if operator_choice in operations:
    result = operations[operator_choice](f_number, s_number)
    print(f"The result is: {result}")
else:
    print("Error: Invalid choice! Please select a number between 1 and 4.")
