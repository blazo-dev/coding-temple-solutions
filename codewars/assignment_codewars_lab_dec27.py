# Solution 1: Even or Odd
# Link: https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


# Solution 2: Convert a Number to a String
# Link: https://www.codewars.com/kata/5265326f5fda8eb1160004c8
def number_to_string(num):
    return str(num)


# Solution 3: Vowel Count
# Link: https://www.codewars.com/kata/54ff3102c1bad923760001f3
def get_count(sentence):
    # List of vowels
    vowels = ["a", "e", "i", "o", "u"]

    return sum(1 for letter in sentence if letter in vowels)
