
from helper_functions import validate_input, convert_to_binary, create_message
from file_manager import save_message, read_message
from greetings import show_intro, show_exit_message


def get_user_info():
    """Collect user name and age with validation (without using .isdigit())."""
    while True:
        name = input("Enter your name: ").strip()
        if not validate_input(name):
            print("Invalid name! Please try again.")
            continue

        age = input("Enter your age: ").strip()

        # Manual digit check (instead of .isdigit())
        valid_age = True
        for ch in age:
            if ch < '0' or ch > '9':
                valid_age = False
                break

        if not valid_age or age == "":
            print("Invalid age! Please enter a number.")
            continue

        return name, age


if __name__ == "__main__":
    show_intro()

    name, age = get_user_info()
    name_binary = convert_to_binary(name)
    age_binary = convert_to_binary(age)

    message = create_message(name, age, name_binary, age_binary)
    print(message)

    save_message(message)
    read_message()

    show_exit_message()