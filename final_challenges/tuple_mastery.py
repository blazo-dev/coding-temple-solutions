"""👾💻Final Challenge: Tuple Mastery
Now that you’ve explored the basics, let’s put everything together!"""

# Create a Tuple: Create a tuple with at least 6 elements. Feel free to mix different data types like integers, strings, and floats.
my_tuple = (10, "Python", 3.14, "Code", 5, "Immutable")

# Access and Print Elements: Access and print the third and fifth elements using indexing.
print("Third element:", my_tuple[2])
print("Fifth element:", my_tuple[4])

# Slice the Tuple: Slice the tuple to extract elements from the second to the fifth ipositon.
sliced_tuple = my_tuple[1:5]
print("Sliced tuple:", sliced_tuple)

# Count Occurrences: Use the count() method to find how many times a specific value appears in your tuple.
count_code = my_tuple.count("Code")
print("Count of 'Code':", count_code)

# Unpack the Tuple: Unpack the tuple into individual variables and print them.
a, b, c, d, e, f = my_tuple
print(a, b, c, d, e, f)

# Concatenate Tuples: Concatenate your tuple with another tuple and print the new tuple.
new_tuple = my_tuple + ("New", "Tuple")
print("Concatenated tuple:", new_tuple)
