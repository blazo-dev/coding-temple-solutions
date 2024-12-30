"""
👾💻 Final Challenge: Square Each Number in a List

Objective:
Create a function that takes a list of numbers as an argument, squares each number,
and returns a new list with the squared values.

Example Input:
list_of_numbers = [3, 99, 12, 1, 7]

Steps:
1. Define the function that takes a list of numbers.
2. Create an empty list to store the squared numbers.
3. Loop through the provided list and square each number.
4. Return the new list with the squared values.
"""


def square_numbers(numbers):
    return [number**2 for number in numbers]


# Tests
list_of_numbers = [3, 99, 12, 1, 7]

# Running the test
list_result = square_numbers(list_of_numbers)

print(list_result)


# Test 1: Check if the function correctly squares the numbers in the list
assert square_numbers(list_of_numbers) == [
    9,
    9801,
    144,
    1,
    49,
], "Test failed for input [3, 99, 12, 1, 7]"

# Test 2: Check if an empty list returns an empty list
assert square_numbers([]) == [], "Test failed for empty list"

# Test 3: Check if the function handles a list with one number
assert square_numbers([5]) == [25], "Test failed for input [5]"

# Test 4: Check if the function handles negative numbers
assert square_numbers([-3, -5, -7]) == [9, 25, 49], "Test failed for negative numbers"

# Test 5: Check if the function handles large numbers
assert square_numbers([1000, 9999]) == [
    1000000,
    99980001,
], "Test failed for large numbers"

print("All tests passed!")
