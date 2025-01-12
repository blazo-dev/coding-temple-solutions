# Managing Data Interactively: TV Show Manager
# Let’s build a more advanced program for managing a list of TV shows. We’ll use regular expressions to store and retrieve structured data from the file.

import re


# Function to write TV shows to a file
def write_show(shows: list):
    with open('shows_list.txt', 'w') as shows_file:
        for show in shows:
            shows_file.write(f"{show['Title']}-:-{show['Platform']}-:-{show['Genre']}\n")


# Function to add a show to our shows list in dictionary format, and write it to our file with the write_show function
def add_show(shows: list):
    title = input("What is the title of the show? ")
    platform = input("Where can we watch it? ")
    genre = input("what is the genre? ")
    shows.append({'Title': title, 'Platform': platform, 'Genre': genre})
    write_show(shows)


# Function to edit a show
def edit_show(shows: list):
    view(shows)
    show_id = int(input("\n\nChoose a number for the show you'd like to edit: ")) - 1

    if 0 <= show_id < len(shows):
        show = shows[show_id]

        title = input(f"Title [{show['Title']}]: ") or show['Title']
        platform = input(f"Platform [{show['Platform']}]: ") or show['Platform']
        genre = input(f"Genre [{show['Genre']}]: ") or show['Genre']

        shows[show_id] = {'Title': title, 'Platform': platform, 'Genre': genre}
        write_show(shows)

        print("Show edited successfully!")
    else:
        print("Invalid input. Please try again.")
        edit_show(shows)


# Function to read TV shows from a file
def read_shows():
    shows_list = []
    with open('shows_list.txt', 'r') as shows_file:
        for shows_line in shows_file:
            data = re.search(r"([\w\s]+)-:-([\w\s]+)-:-([\w\s]+)", shows_line)
            shows_list.append({'Title': data.group(1), 'Platform': data.group(2), 'Genre': data.group(3).strip()})
    return shows_list


# Function to print the list of shows for the user in a formatted way
def view(shows: list):
    print("Shows List")
    print('-----------------------')
    for idx, show in enumerate(shows):
        vowels = ['a', 'e', 'i', 'o', 'u']
        a_or_an = 'an' if show['Genre'][0].lower() in vowels else 'a'
        print(f"{idx + 1}.) {show['Title']} is {a_or_an} {show['Genre']} show on {show['Platform']}")


# Function to show our current list of shows and allow the user to choose which to remove
def remove_show(shows: list):
    view(shows)
    option = int(input("\n\nChoose a number for the show you'd like to remove: "))
    show = shows.pop(option - 1)  # index - 1
    print(f"\n{show['Title']} was successfully removed!")
    write_show(shows)


def main():
    while True:
        shows_list = read_shows()
        action = input('''
Options
-----------------------
1 - Add a TV Show
2 - Edit a TV Show
3 - Remove a TV Show
4 - View List of TV Shows
5 - Quit
''')
        if action == '1':
            add_show(shows_list)
        elif action == '2':
            edit_show(shows_list)
        elif action == '3':
            remove_show(shows_list)
        elif action == '4':
            view(shows_list)
        elif action == '5':
            print("Thanks for using this app!")
            break


main()
