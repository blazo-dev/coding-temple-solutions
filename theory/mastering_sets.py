"""
Python Sets: A Comprehensive Guide

Sets are a special collection data type in Python, and they're useful for storing unique items.
Here are some important characteristics of sets:

- Unordered: You won’t know the order of elements.
- Mutable: You can change the set’s contents by adding or removing items.
- Unique: Sets automatically remove duplicate items.
- No Indexing: Unlike lists or tuples, sets don't have a defined order, so you can't access items using an index.

"""

# Creating Sets
# Example 1: Creating an Empty Set
empty_set = set()  # This creates an empty set
print(type(empty_set))  # Output: <class 'set'>

# Example 2: Creating a Set with Values
new_set = {'one', 'two', 'three'}
print(new_set)  # Output: {'one', 'two', 'three'}

# Removing Duplicates from Lists Using Sets
alist = ['item', 'item', 'stuff', 'thing', 'oddity']
set_list = set(alist)  # Converting list to a set
print(set_list)  # Output: {'stuff', 'item', 'thing', 'oddity'}

# Exercise 1: Practice Creating Sets
hobbies = ['reading', 'gaming', 'hiking', 'gaming', 'swimming', 'hiking']
hobbies_set = set(hobbies)
print("Original List:", hobbies)
print("Set with Duplicates Removed:", hobbies_set)

# Looping Over Sets
asset = {'apple', 'orange', 'banana'}
for fruit in asset:
    print(fruit)  # Items printed in random order

# Exercise 2: Loop Through a Set
favorite_movies = {'Inception', 'The Matrix', 'Interstellar', 'The Dark Knight', 'Gladiator'}
for movie in favorite_movies:
    print(movie)

# Set Methods
# Membership Checks
my_set = {'superman', 'batman', 'wonder woman', 'the flash'}
print('superman' in my_set)  # Output: True
print('spider man' in my_set)  # Output: False

# Adding Items to a Set
my_set.add('green lantern')
print(my_set)  # Output: {'superman', 'batman', 'wonder woman', 'the flash', 'green lantern'}

# Exercise 3: Set Modification Practice
foods = {'pizza', 'sushi', 'pasta', 'ice cream'}
foods.add('burger')  # Adding a new item
print('pasta' in foods)  # Checking for an item
print(foods)

# Advanced Set Methods
# Subset and Superset Checks
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))  # Output: True
print(set2.issuperset(set1))  # Output: True

# Exercise 4: Comparing Sets
set1 = {'basketball', 'soccer', 'tennis'}
set2 = {'basketball', 'soccer'}
print(set2.issubset(set1))  # Is set2 a subset of set1?
print(set1.issuperset(set2))  # Is set1 a superset of set2?

# Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6}

# Intersection
print(set1.intersection(set2))  # Output: {3, 4}

# Difference
print(set1.difference(set2))  # Output: {1, 2}

# Symmetric Difference
print(set1.symmetric_difference(set2))  # Output: {1, 2, 5, 6}

# Exercise 5: Working with Set Operations
set1 = {'Paris', 'Tokyo', 'New York'}
set2 = {'London', 'Paris', 'Rome'}

# Union
print("All unique destinations:", set1.union(set2))

# Intersection
print("Common destinations:", set1.intersection(set2))

# Difference
print("Destinations only in set1:", set1.difference(set2))
