"""
Your task is to make a function that can take any non-negative 
integer as an argument and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.
"""


def descending_order(num):
    if num < 0:
        return num

    list_number = list(str(num))
    list_number.sort(reverse=True)

    return int("".join(list_number))


# Tests

assert descending_order(42145) == 54421, "Should return 54421 for 42145"
assert descending_order(145263) == 654321, "Should return 654321 for 145263"
assert descending_order(123456789) == 987654321, "Should return 987654321 for 123456789"

print("All tests passed! :D")
