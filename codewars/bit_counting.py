"""
Write a function that takes an integer as input, 
and returns the number of bits that are equal to 
one in the binary representation of that number. 
You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, 
so the function should return 5 in this case

"""


def count_bits(n: int) -> int:
    bit_count = 0
    current_number = n
    while current_number > 0:
        bit_count += current_number % 2
        current_number //= 2

    return bit_count


# Números más grandes
assert count_bits(1234) == 5, "Error: 1234 should have 5 ones in binary"
assert count_bits(1023) == 10, "Error: 1023 should have 10 ones in binary"
assert count_bits(2048) == 1, "Error: 2048 should have 1 one in binary"
assert count_bits(255) == 8, "Error: 255 should have 8 ones in binary"

print("All tests passed! 😊")
