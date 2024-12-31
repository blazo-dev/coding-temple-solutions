"""
Exercise Description:
Write a function that returns the sum of all natural numbers below a given positive integer that are multiples of 3 or 5.

If a number is a multiple of both 3 and 5, count it only once.

For negative inputs, return 0.

Example:

For input 10, the multiples are 3, 5, 6, 9, and their sum is 23.
"""


def sum_multiples_3_5(n: int):
    multi_sum = 0

    if n <= 0:
        return 0

    for i in range(n - 1, 0, -1):
        if i % 3 == 0 or i % 5 == 0:
            multi_sum += i

    return multi_sum


# Tests

assert sum_multiples_3_5(4) == 3, "Should return 3 for 4"
assert sum_multiples_3_5(6) == 8, "Should return 8 for 6"
assert sum_multiples_3_5(10) == 23, "Should return 23 for 10"
assert sum_multiples_3_5(15) == 45, "Should return 45 for 15"
assert sum_multiples_3_5(-1) == 0, "Should return 0 for -1"

print("All tests passed! :D")
