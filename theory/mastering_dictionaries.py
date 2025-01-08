# 📌 Brief Overview
# Python 🐍 dictionaries are a versatile data structure used to store data in key-value pairs.
# They allow you to organize and access data efficiently, much like a real-world dictionary 📖, where you can quickly look up information using a key (which can be various data types, such as strings, numbers, or tuples).
# In Python, dictionaries are especially useful for associating data with unique identifiers, making them great for scenarios like looking up user profiles by username, storing configuration settings, or managing inventory by product ID.

# Introduction to Dictionaries
# In Python are defined using curly braces {} and consist of key-value pairs.
# Each key in a dictionary must be unique and immutable (e.g., strings, numbers, or tuples), while the values can be of any data type and can be duplicated.
# Starting from Python 3.7, dictionaries maintain insertion order, which became a part of the language specification in Python 3.8.
# They are also mutable, meaning you can modify them after they are created.

# Example of a Python dictionary
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Accessing Values in a Dictionary
# You can access the values stored in a dictionary by using the keys🔑.

# Accessing Keys
# If the key🔑 'name' is present in the dictionary, the value associated with it will be printed 🖨️.

# Accessing values by key
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

print(my_dict['name'])  # Output: Alice

# The .get() method & avoiding missing keys
# If you try to access a key that does not exist, Python will raise a KeyError ❌.
# To avoid this, you can use the .get() method, which will return None (or a default value you specify) if the key doesn’t exist.

print(my_dict.get('age'))  # Output: 25
print(my_dict.get('address', 'Not Available'))  # Output: Not Available

# Adding, Modifying, and Removing Elements
# Dictionaries are dynamic 🔄, meaning you can add ➕, modify 🖊️, or remove ❌ elements at any time.

# Adding Elements: To add a new key🔑-value pair, simply assign a value to a new key.
my_dict['profession'] = 'Engineer'

# Adding Elements Video Walkthrough:
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'profession': 'Engineer'}

# Modifying Elements: To modify an existing value, assign a new value to an existing key🔑.
my_dict['age'] = 26
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'profession': 'Engineer'}

# Removing Elements: You can use the del statement or the .pop() method to remove ❌ elements from a dictionary.
del my_dict['city']
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'profession': 'Engineer'}

removed_value = my_dict.pop('profession')
print(removed_value)  # Output: Engineer
print(my_dict)  # Output: {'name': 'Alice', 'age': 26}

# Dictionary Methods
# Dictionaries come with many useful 🛠️ methods that help you interact with their data.

# .keys(): Returns a view object that displays a list of all the keys🔑 in the dictionary.
print(list(my_dict.keys()))  # Output: ['name', 'age']

# .values(): Returns a view object of all the values in the dictionary.
print(list(my_dict.values()))  # Output: ['Alice', 26]

# .items(): Returns a view object that displays a list of dictionary’s key🔑-value tuple pairs.
print(list(my_dict.items()))  # Output: [('name', 'Alice'), ('age', 26)]

# Looping Through Dictionaries
# Looping through dictionaries allows you to access and manipulate the data efficiently.

# Looping through Keys Only: You can loop through only the keys in a dictionary using a for loop.
for key in my_dict:
    print(key)  # Output: name, age

# Looping through Values Only: Use the .values() method to loop through the values.
for value in my_dict.values():
    print(value)  # Output: Alice, 26

# Looping through Key-Value Pairs: Use the .items() method to loop through both keys and values.
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output: name: Alice, age: 26

# Nested Dictionaries
# A nested dictionary is simply a dictionary where one or more values are also dictionaries.

# Creating a dictionary of users, where each user has their own dictionary of details
users = {
    'user1': {
        'name': 'Alice',
        'age': 25,
        'address': {
            'street': '123 Main St',
            'city': 'New York',
            'zipcode': '10001'
        }
    },
    'user2': {
        'name': 'Bob',
        'age': 30,
        'address': {
            'street': '456 Elm St',
            'city': 'San Francisco',
            'zipcode': '94107'
        }
    }
}

# Accessing the city of user1 by first accessing 'user1', then 'address', and then 'city'
city_user1 = users['user1']['address']['city']
print(city_user1)  # Output: New York

# Modifying Nested Dictionaries
# You can modify the values in a nested dictionary just like you would in a flat dictionary.
users['user2']['address']['zipcode'] = '94109'
print(users['user2']['address']['zipcode'])  # Output: 94109

# Adding Nested Elements
# You can also add new keys or dictionaries to a nested dictionary.
users['user1']['phone'] = '555-1234'
print(users['user1']['phone'])  # Output: 555-1234

# Looping Through Nested Dictionaries
# When working with nested dictionaries, you can loop through them just as you would with a regular dictionary.

# Looping through the outer dictionary 'users'
for user, info in users.items():
    print(f"User ID: {user}")

    # Looping through the inner dictionary for each user
    for key, value in info.items():
        print(f"  {key}: {value}")

# A List of Dictionaries
# In some cases, you may have multiple dictionaries that you need to manage together as a group.

students = [
    {
        'name': 'Alice',
        'age': 25,
        'major': 'Physics'
    },
    {
        'name': 'Bob',
        'age': 22,
        'major': 'Computer Science'
    },
    {
        'name': 'Charlie',
        'age': 23,
        'major': 'Mathematics'
    }
]

# Accessing the major of the first student in the list
first_student_major = students[0]['major']
print(first_student_major)  # Output: Physics

# Looping Through a List of Dictionaries
# Often, you’ll want to loop through the list to process or display the data for each dictionary.

# Looping through the list of students
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")

# A List within a Dictionary
# In some cases, you'll want to store multiple values under a single key in a dictionary.

favorite_books = {
    'Alice': ['1984', 'To Kill a Mockingbird', 'Pride and Prejudice'],
    'Bob': ['The Great Gatsby', 'Catch-22', 'Moby Dick'],
    'Charlie': ['The Hobbit', 'Harry Potter', 'War and Peace']
}

# Accessing Alice's favorite books
alice_books = favorite_books['Alice']
print(alice_books)  # Output: ['1984', 'To Kill a Mockingbird', 'Pride and Prejudice']

# Accessing Bob's second favorite book
second_favorite_bob = favorite_books['Bob'][1]
print(second_favorite_bob)  # Output: Catch-22

# Looping Through Lists Inside a Dictionary
# You can also loop through the dictionary to access each person and their favorite books.

for person, books in favorite_books.items():
    print(f"{person}'s favorite books:")
    for book in books:
        print(f" - {book}")
