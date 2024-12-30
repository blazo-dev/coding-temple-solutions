# Code Exercises

This folder contains solutions to coding problems. Below is a detailed explanation of each solution.

---

## Solution 1: Even or Odd

**Link**: [Even or Odd](https://www.codewars.com/kata/53da3dbb4a5168369a0000fe)

### Problem:

Write a function that takes an integer as input and returns whether the number is "Even" or "Odd".

### Code:

```python
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"
```

### Explanation:

- The modulo operator (`%`) gives the remainder when dividing `number` by 2.
- If the remainder is `0`, the number is even; otherwise, it’s odd.
- We use a **ternary operator** to return either "Even" or "Odd" based on the condition.

### Learn More:

- For details about the modulo operator, check [Basic Arithmetic Operations](https://docs.python.org/3/tutorial/introduction.html#basic-arithmetic-operations).

---

## Solution 2: Convert a Number to a String

**Link**: [Convert a Number to a String](https://www.codewars.com/kata/5265326f5fda8eb1160004c8)

### Problem:

Write a function that converts a number to a string.

### Code:

```python
def number_to_string(num):
    return str(num)
```

### Explanation:

- The `str()` function converts a number (either integer or float) into its string representation.

### Learn More:

- To learn more about type conversions in Python, visit the [Standard Types Documentation](https://docs.python.org/3/library/stdtypes.html#str).

---

## Solution 3: Vowel Count

**Link**: [Vowel Count](https://www.codewars.com/kata/54ff3102c1bad923760001f3)

### Problem:

Write a function that counts the number of vowels in a given string.

### Code:

```python
def get_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    return sum(1 for letter in sentence if letter in vowels)
```

### Explanation:

- We define a list `vowels` containing the characters "a", "e", "i", "o", "u".
- The **generator expression** (`1 for letter in sentence if letter in vowels`) iterates over each letter in the `sentence`, generating `1` for every vowel it finds.
- The `sum()` function adds up the `1`s generated, giving the total number of vowels.

### Learn More:

- To learn more about **list comprehensions** and **sum()**, check out the following resources:
  - [List Comprehensions in Python](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
  - [sum() Function in Python](https://docs.python.org/3/library/functions.html#sum)

---

### General Learning Suggestions:

- **Modulo Operator (`%`)**: Useful for checking divisibility and remainders.
- **Type Conversion (`str()`)**: Converting numbers to strings.
- **List Comprehensions**: Efficient way to create sequences and perform operations on them.
