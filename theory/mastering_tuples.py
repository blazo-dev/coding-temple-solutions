# 📝 Brief Overview
# In Python, tuples are a type of data structure that allow you to store multiple items in a single variable.
# Key features:
# - Ordered: Items are indexed starting from 0.
# - Immutable: Values cannot be changed after creation.
# - Heterogeneous: Can store elements of different data types.

# 🧠 Why Use Tuples?
# - Faster: Tuples are generally faster than lists for iteration and access.
# - Data Integrity: Ensures the collection of data remains constant.
# - Dictionary Keys: Tuples can be used as dictionary keys since they are immutable.

# ✍️ Creating a Tuple
# 1. Using parentheses ()
tuple1 = (10, "Python", 3.14)

# 2. Without parentheses (tuple packing)
tuple2 = 10, "Python", 3.14

# 3. Single-element tuple (must include a trailing comma)
single_element_tuple = (5,)

# 4. Empty tuple
empty_tuple = ()

# 5. Using the tuple() constructor
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3)

# 🔍 Tuple Manipulation

# Accessing Tuple Elements
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[0])  # Output: "apple"
print(my_tuple[1])  # Output: "banana"

# Slicing Tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])  # Output: (2, 3, 4)

# Looping Over Tuples
for num in my_tuple:
    print(num)

# Tuple Immutability
my_tuple = (10, 20, 30)
# my_tuple[1] = 40  # This raises an error

# Reassigning the Entire Tuple
my_tuple = (40, 50, 60)  # This works, creating a new tuple

# 🎁 Packing and Unpacking Tuples

# Packing
person_info = "Alice", 30, "Developer"

# Unpacking
name, age, profession = person_info
print(name)  # Output: Alice
print(age)  # Output: 30
print(profession)  # Output: Developer

# Extended Unpacking
numbers = (1, 2, 3, 4, 5)
first, *rest = numbers
print(first)  # Output: 1
print(rest)  # Output: [2, 3, 4, 5]

# Ignoring Values with Underscore (_)
person_info = ("Eve", 35, "Artist", "New York")
name, _, profession, _ = person_info
print(name)  # Output: Eve
print(profession)  # Output: Artist


# Tuple Packing and Unpacking with Functions

# Returning Multiple Values
def get_user_info():
    return "Bob", 29, "Engineer"


name, age, profession = get_user_info()


# Passing Multiple Values with Unpacking
def display_info(name, age, profession):
    print(f"{name} is {age} years old and works as a {profession}.")


info_tuple = ("Charlie", 28, "Designer")
display_info(*info_tuple)

# 🔧 Tuple Methods
my_tuple = (1, 2, 2, 3, 2)
print(my_tuple.count(2))  # Output: 3

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.index(3))  # Output: 2
