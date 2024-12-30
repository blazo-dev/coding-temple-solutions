# Code Exercises

This folder contains solutions to coding problems. Below is a detailed explanation of each solution.

---

## Solution 1: Even or Odd

**Link**: [Even or Odd Kata](https://www.codewars.com/kata/53da3dbb4a5168369a0000fe)

### Problem:

Write a function that takes an integer as input and returns whether the number is "Even" or "Odd".

### Explanation:

- The modulo operator (`%`) is used to check if the number is divisible by 2.
- If the remainder is `0`, the number is even; otherwise, it is odd.
- A **ternary operator** is used to return either "Even" or "Odd" based on the result of the condition.

### Learn More:

- For details about the modulo operator, check [Basic Arithmetic Operations](https://docs.python.org/3/tutorial/introduction.html#basic-arithmetic-operations).

---

## Solution 2: Convert a Number to a String

**Link**: [Convert a Number to a String Kata](https://www.codewars.com/kata/5265326f5fda8eb1160004c8)

### Problem:

Write a function that converts a number to a string.

### Explanation:

- The `str()` function is used to convert a number (either integer or float) into its string representation.

### Learn More:

- To learn more about type conversions in Python, visit the [Standard Types Documentation](https://docs.python.org/3/library/stdtypes.html#str).

---

## Solution 3: Vowel Count

**Link**: [Vowel Count Kata](https://www.codewars.com/kata/54ff3102c1bad923760001f3)

### Problem:

Write a function that counts the number of vowels in a given string.

### Explanation:

- A list of vowels `["a", "e", "i", "o", "u"]` is defined.
- A **generator expression** iterates over each letter in the sentence and generates `1` for every vowel it finds.
- The `sum()` function is used to add up the `1`s and return the total count of vowels.

### Learn More:

- To learn more about **list comprehensions** and **sum()**, check out the following resources:
  - [List Comprehensions in Python](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
  - [sum() Function in Python](https://docs.python.org/3/library/functions.html#sum)

---

### General Learning Suggestions:

- **Modulo Operator (`%`)**: Useful for checking divisibility and remainders.
- **Type Conversion (`str()`)**: Converting numbers to strings.
- **List Comprehensions**: Efficient way to create sequences and perform operations on them.
