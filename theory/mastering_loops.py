# Python Loops Overview

# Loops repeat a block of code until a condition is met. There are two main types:
# - for loop: Iterates over a sequence.
# - while loop: Repeats code while a condition is True.

# For Loop Example 1: Looping Through a List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output: apple, banana, cherry

# For Loop Example 2: Using range() in a For Loop
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# While Loop Example
count = 0
while count < 5:
    print(count)
    count += 1
# Output: 0, 1, 2, 3, 4

# Example: Print even numbers from 1 to 20 using a while loop.
number = 1
while number <= 20:
    if number % 2 == 0:
        print(number)
    number += 1
# Output: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20

# Control Flow in Loops:
# - break: Stops the loop.
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0, 1, 2, 3, 4

# - continue: Skips the current iteration.
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output: 0, 1, 2, 4
