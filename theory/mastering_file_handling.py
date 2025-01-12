# 📌 Brief Overview
# In this lesson, you'll learn the fundamentals of Python file handling—how to open, read, write, and append to files.
# You will also explore how to manage structured data, such as lists, dictionaries, and custom data formats, using files.
# By the end of this lesson, you'll be able to build a simple program that interacts with files to store and retrieve data interactively.

# Learning Objectives:
# - Understand how to open, read, write, and append to files in Python.
# - Store and retrieve structured data using text files.
# - Build interactive programs for data management.
# - Practice advanced file handling with real-world examples.

# 1. Opening and Writing to Files
# Let’s start by exploring how to open and write to files in Python. You can write data into a file using the open() function and specifying the mode ('w' for write or 'a' for append).

# Open a file in 'w' mode to write data
file = open('new_file.txt', 'w')
file.write('Writing to a file from Python!\n')
file.close()  # Always close the file after writing

# Appending data to the file without overwriting
file = open('new_file.txt', 'a')
file.write('Adding more content with "a" mode\n')
file.close()

# Explanation: The 'w' mode overwrites the file if it already exists, while 'a' mode adds data to the file without removing existing content. Always ensure you close the file after writing to it using file.close().

# 2. Reading Files
# Now, let’s look at how to read data back from files. Python provides different methods for reading files, such as read(), readline(), and readlines().

# Reading the file with 'r' mode
with open('new_file.txt', 'r') as file:
    content = file.read()  # Read the entire file content
    print(content)

# Explanation: Using with open ensures the file is properly closed after reading, even if an error occurs in your program.

# Engage & Apply: Mid-Lesson Exercise
# Task: Create a simple Python program that:

# Allows the user to add favorite foods to a list.
# Stores the data in a file.
# Lets the user view or remove items from the list.
# Example solution for managing a list of favorite foods
def write_foods(foods):
    with open('foods.txt', 'w') as food_file:
        for food in foods:
            food_file.write(food + '\n')

def read_foods():
    foods_list = []
    with open('foods.txt', 'r') as food_file:
        for line_read in food_file:
            foods_list.append(line_read.strip())
    return foods_list

def main():
    foods = read_foods()
    while True:
        action = input("1 - Add Food, 2 - View Foods, 3 - Remove Food, 4 - Quit\n")
        if action == '1':
            new_food = input("Enter the name of the food: ")
            foods.append(new_food)
            write_foods(foods)
        elif action == '2':
            print("Your favorite foods:")
            for food in foods:
                print(food)
        elif action == '3':
            idx = int(input("Which food to remove? "))
            foods.pop(idx - 1)
            write_foods(foods)
        elif action == '4':
            break

main()

# 3. Storing and Extracting Data from Lists and Dictionaries
# Now that you have experience writing and reading from files, let’s move on to more structured data like lists and dictionaries.

# Storing Lists:
flowers = ["Wisteria", "Sunflowers", "Orchids", "Marigolds"]

with open('garden.txt', 'w') as file:
    for flower in flowers:
        file.write(flower + '\n')

# Extracting Lists:
flowers = []

with open('garden.txt', 'r') as file:
    for line in file:
        flowers.append(line.strip())
print(flowers)

# Explanation: The strip() method removes unwanted whitespace, and you can loop through each line to append the cleaned-up data to your list.

# Storing and Extracting Dictionaries:
clubs = {
    'Driver': 'Cobra',
    'Irons': 'Sirio',
    'Hybrid': 'Calloway',
    'Putter': 'Ping'
}

with open('golf_bag.txt', 'w') as file:
    for club, brand in clubs.items():
        file.write(f"{club}: {brand}\n")

# Extracting dictionary data
golf_clubs = {}

with open('golf_bag.txt', 'r') as file:
    for line in file:
        club, brand = line.strip().split(': ')
        golf_clubs[club] = brand
print(golf_clubs)