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
    - Add tasks ✅
    - View tasks ✅
    - Delete tasks ✅
    - Quit the application ✅

- User Interaction:
    - Use input() to capture user selections and ensure proper input validation to handle invalid choices. ✅
    
- Error Handling:
    - Implement error handling using try, except, else, and finally blocks to catch errors. ✅
    - Alert the user if they provide invalid input. ✅
    - Alert the user if there are no tasks to view. ✅
    - Alert the user if they try to delete a task that doesn't exist. ✅
    - Alert the user if they select an option on the main menu that doesn't exist. ✅

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


# 🛠 Utility Functions
def handle_option(option: int, tasks: list):
    """Handle the selected option using a hash table (dictionary)."""

    if option == 1:
        add_task(tasks)
    elif option == 3:
        view_tasks(tasks)
        delete_task(tasks)
    elif option == 4:
        exit_application()

    if option in [1, 2, 3]:
        view_tasks(tasks)


def exit_application():
    """Displays a farewell message and exits the program."""
    print("\n👋 Thank you for using the To-Do List App! Have a productive day! 🚀")
    exit()


# 📋 Menu Display
def display_menu(menu_options: dict[int, str]):
    """Display the main menu with available options."""
    print("\nWhat would you like to do now? 🤔")
    for i, option in menu_options.items():
        print(f"{i}. {option}")


# ➕ Add Task
def add_task(tasks: list[str]):
    """Prompt the user to enter a new task and add it to the list."""

    task_description = input("\n📝 Please enter the description for the new task: ")

    if not task_description:
        raise ValueError(
            "❌ Task description cannot be empty. Please enter a valid description."
        )

    tasks.append(task_description)


# 👀 View Tasks
def view_tasks(tasks: list[str]):
    """Display the tasks in the list or notify if the list is empty."""
    if len(tasks) == 0:
        raise ValueError(
            "⚠️  Error: The task list is empty. Please add tasks before proceeding! 📝"
        )

    print("\n📝 Here is the list of tasks:\n")
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]}")


# ❌ Delete Task
def delete_task(tasks: list[str]):
    """Allow the user to delete a specific task from the list."""
    id_selected = get_valid_int("\n🗑️  Enter the task number to delete it: ")
    id_selected -= 1
    tasks_ids = [i for i in range(len(tasks))]
    validate_option(
        id_selected,
        tasks_ids,
        f"⚠️  Task number {id_selected + 1} doesn't exist. Please select a valid task.",
    )

    task_to_delete = tasks[id_selected]

    tasks.remove(task_to_delete)
    print(f"\n✅ Task '{task_to_delete}' has been deleted.")


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
        1: "➕ Add a new task",
        2: "👀 View your tasks",
        3: "️❌ Remove a task",
        4: "🚪 Exit the app",
    }


# 🚀 Main Program
def main():
    """Main function to run the To-Do List application."""
    print("\n🎉 Welcome to the To-Do List Application! 🎉")

    tasks: list[str] = []

    while True:
        menu_options = get_menu_options()
        display_menu(menu_options)

        try:
            option_selected = get_valid_int(
                "\n👉 Choose an option by entering its number: "
            )
            validate_option(option_selected, menu_options.keys())

            handle_option(option_selected, tasks)
        except (ValueError, KeyError) as e:
            print(f"\n{e}")
            continue


# Start the program
main()
