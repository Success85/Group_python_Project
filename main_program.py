from helper_functions import validate_input, convert_to_binary, create_message
from file_manager import save_message, read_message
from greetings import show_intro, show_exit_message

def get_user_info():
    while True:
        name=input("What is your name? ")
        age=input("How old are you? ")
        print()
        valid, name, age = helper_functions.validate_input(name, age)
        if valid:
            return name, age

def main():
    show_intro()
    name, age = get_user_info()

    binary_name, binary_age = helper_functions.convert_to_binary(name, age)

    message = create_message(name, age, name_binary, age_binary)

    print("\n--- Your Personalized Message ---")
    print(message)
    print("---------------------------------")

    save_message(message)

    read_message()

    show_exit_message()

main()

if __name__ == "__main__":
    main()
  
