# 📌 Brief Overview
# By the end of this lesson, you will be able to create, manipulate, and perform basic operations on Python lists.

# 🐍 Exploring the Power of Lists in Python

# What is a List? A list is a collection of items that can hold multiple values. Lists are mutable (can be changed).
# Lists are defined with square brackets [] and can contain different data types like integers, floats, strings, or even other lists.
my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "apple", 3.14, True]

# Key Characteristics of Lists:
# - Order: Items have a specific order.
# - Indexing: Items are indexed starting from 0.

# Accessing Elements:
# Elements are accessed by their index.
my_list = ["apple", "banana", "cherry"]
print(my_list[0])  # Output: apple
print(my_list[-1])  # Output: cherry

# Modifying Lists:
# - Add an item: .append() adds an item to the end.
my_list.append("orange")
# - Insert at a specific index: .insert(index, item)
my_list.insert(1, "blueberry")
# - Remove an item: .remove(item) removes the first matching item.
my_list.remove("apple")
# - Delete by index: Use del or .pop()
del my_list[0]  # Deletes the first item
my_list.pop(1)  # Removes and returns the item at index 1

# Slicing Lists: Allows access to a subset of items.
my_list = [1, 2, 3, 4, 5, 6]
subset = my_list[1:4]  # [2, 3, 4]
print(my_list[:3])  # [1, 2, 3]
print(my_list[3:])  # [4, 5, 6]

# 🧠📓 Engage & Apply: Manipulate Python Lists, their characteristics, and operations.

# Define a list called "fruits"
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])  # Output: "apple"
print(fruits[-1])  # Output: "date"

# Add and Insert Items
fruits.append("elderberry")
fruits.insert(1, "blueberry")
print(
    fruits
)  # Output: ["apple", "blueberry", "banana", "cherry", "date", "elderberry"]

# Remove Items
fruits.remove("banana")
del fruits[0]
print(fruits)  # Output: ["blueberry", "cherry", "date", "elderberry"]

# Slice the List: Create and print a subset of the list
citrus_fruits = fruits[2:4]  # ["cherry", "date"]
print(citrus_fruits)  # Output: ["cherry", "date"]

# List Functions and Methods
# Built-in Functions:
print(len(fruits))  # Output: 4
print(min([5, 3, 8]))  # Output: 3
print(max([5, 3, 8]))  # Output: 8

# Common List Methods:
numbers = [4, 1, 7, 3]
numbers.sort()  # Output: [1, 3, 4, 7]
numbers.reverse()  # Output: [7, 4, 3, 1]
list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2)  # Output: [1, 2, 3, 4, 5]

# Nested Lists: A list can contain other lists.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][1])  # Output: 2
