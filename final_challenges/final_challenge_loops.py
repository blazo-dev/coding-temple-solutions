"""
👾💻 Final Challenge: Python Loop Control

Objective:
Write a Python program that processes a range of numbers from 1 to 30. The program should:

1. Print all numbers from 1 to 30.
2. Skip the numbers that are divisible by 3 using the `continue` statement.
3. Stop the loop if the number exceeds 25 using the `break` statement.
"""


def process_numbers():
    return [i for i in range(1, 31) if i % 3 != 0 and i <= 25]


# Running the test
processed_numbers = process_numbers()

print(processed_numbers)

# Test 1: Check if numbers from 1 to 30 are processed correctly
assert (
    len(processed_numbers) == 17
), f"Expected 17 numbers, but got {len(processed_numbers)}"

# Test 2: Ensure numbers divisible by 3 are skipped
assert all(
    i % 3 != 0 for i in processed_numbers
), f"Some numbers divisible by 3 are included: {processed_numbers}"

# Test 3: Ensure the loop stops at 25
assert (
    processed_numbers[-1] <= 25
), f"The loop should stop at 25 or before, but the last number is {processed_numbers[-1]}"

# Test 4: Ensure the numbers are in the correct sequence and within the range
expected_numbers = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25]
assert (
    processed_numbers == expected_numbers
), f"Expected numbers: {expected_numbers}, but got {processed_numbers}"

print("All tests passed!")
