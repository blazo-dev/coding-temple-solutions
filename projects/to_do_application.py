"""
To-Do List Application (CLI)

Project Overview:
In this project, you will build a functional To-Do List Application using Python. 
This assignment will help you strengthen your understanding of Python concepts such as syntax, data types, control structures, functions, and error handling.

Requirements:
- User Interface (UI) and Storage Method:
    - Build a simple Command Line Interface (CLI) that welcomes users and displays a menu with options to add, view, delete tasks, or quit the application.
    - The tasks should be stored in a Python list.

- Core Features:
    - Add tasks
    - View tasks
    - Delete tasks
    - Quit the application ✅

- User Interaction:
    - Use input() to capture user selections and ensure proper input validation to handle invalid choices. ✅
    
- Error Handling:
    - Implement error handling using try, except, else, and finally blocks to catch errors. ✅
    - Alert the user if they provide invalid input. ✅
    - Alert the user if there are no tasks to view. ✅
    - Alert the user if they try to delete a task that doesn't exist.
    - Alert the user if they select an option on the main menu that doesn't exist.

- Code Organization:
    - Organize your code into functions to improve clarity and maintainability. ✅
    - Use descriptive function names and add comments/docstrings where necessary. ✅

- Testing and Debugging:
    - Thoroughly test your application, considering edge cases such as empty lists and invalid input.

Instructions:
1. Create a new .py file and implement the To-Do List application.
2. Use a Python list to store the tasks.
3. Implement a loop that displays the menu until the user decides to quit.
4. Handle all error scenarios gracefully and ensure the program continues running after an invalid input.
5. Ensure that all user actions (adding, viewing, deleting tasks) are validated and feedback is given when necessary.

Good luck with your project!

"""

import time


# 🛠 Utility Functions
def handle_option(option: int, tasks: list[dict]):
    """Handle the selected option."""
    if option == 1:
        time.sleep(1)
        print("➕ Adding a task...")
    elif option == 2:
        time.sleep(1)
        view_tasks(tasks)
    elif option == 3:
        time.sleep(1)
        view_tasks(tasks)
        delete_task(tasks)
    elif option == 4:
        time.sleep(1)
        print("\n👋 Thank you for using the To-Do List App! Have a productive day! 🚀")
        exit()
    else:
        print("🚫 This should never happen.")


# 📋 Menu Display
def display_menu(menu_options: dict[int, str]):
    """Display the main menu with available options."""
    time.sleep(1)
    print("\nWhat would you like to do now? 🤔")
    for i, option in menu_options.items():
        print(f"{i}. {option}")
    time.sleep(1)


# ➕ Add Task
def add_task(tasks):
    """Prompt the user to enter a new task and add it to the list."""
    pass


# 👀 View Tasks
def view_tasks(tasks: list[dict]):
    """Display the tasks in the list or notify if the list is empty."""
    if len(tasks) == 0:
        raise ValueError(
            "⚠️  Error: The task list is empty. Please add tasks before proceeding! 📝"
        )

    print("\n📝 Here is the list of tasks:\n")
    for task in tasks:
        print(f"{task['id']} - {task['text']}")


# ❌ Delete Task
def delete_task(tasks: list[dict]):
    """Allow the user to delete a specific task from the list."""
    id_selected = get_valid_int("\n🔢 Select a task by entering the number: ")
    tasks_ids = [task["id"] for task in tasks]
    validate_option(
        id_selected,
        tasks_ids,
        "⚠️ The task you're trying to delete doesn't exist. Please select a valid task.",
    )
    
    


# ✅ Validations
def validate_option(
    option: int,
    valid_options: list[int],
    error_message="🚫 Invalid option. Please choose a valid menu item.",
):
    """Validate the user input to ensure it's one of the valid choices."""
    if option in valid_options:
        return
    else:
        raise KeyError(error_message)


def get_valid_int(prompt: str) -> int:
    """Prompt the user for an integer input, raising an exception for invalid input."""
    user_input = input(prompt)
    if not user_input.isdigit():
        raise ValueError(
            f"❌ Error: '{user_input}' is not a valid number. 🔢 Please enter a valid integer."
        )
    return int(user_input)


# 🔢 Menu Options Setup
def get_menu_options() -> dict[int, str]:
    return {
        1: "➕ Add tasks",
        2: "👀 View tasks",
        3: "❌ Delete tasks",
        4: "🚪 Quit",
    }


# 🚀 Main Program
def main():
    """Main function to run the To-Do List application."""
    print("🎉 Welcome to the To-Do List Application! 🎉")

    tasks: list[dict] = [
        {"id": 1, "text": "🛒 Buy groceries"},
        {"id": 2, "text": "📞 Call mom"},
        {"id": 3, "text": "💻 Complete Python project"},
        {"id": 4, "text": "🏋️‍♂️ Go to the gym"},
        {"id": 5, "text": "📚 Read a book"},
    ]

    while True:
        menu_options = get_menu_options()
        display_menu(menu_options)

        try:
            option_selected = get_valid_int(
                "\n🔢 Select an option by entering the number: "
            )
            validate_option(option_selected, menu_options.keys())

            handle_option(option_selected, tasks)
        except (ValueError, KeyError) as e:
            print(e)
            time.sleep(1)
            continue


# Start the program
main()
