
from helper_functions import validate_input, convert_to_binary, create_message
from file_manager import save_message, read_message
from greetings import show_intro, show_exit_message

def get_user_info():
    
    while True:
        name = input("Please enter your name: ").strip()
        if validate_input(name):
            break
        else:
            print("Invalid input: Name cannot be empty. Please try again.")
            
    while True:
        age = input("Please enter your age: ").strip()
        if age.isdigit() and int(age) > 0:
            break 
        else:
            print("Invalid input: Age must be a positive number. Please try again.")
            
    return name, age

def main():
    show_intro()
    name, age = get_user_info()
  
    name_binary = convert_to_binary(name)
    age_binary = convert_to_binary(age)
    
    message = create_message(name, age, name_binary, age_binary)
    
    print("\n--- Your Personalized Message ---")
    print(message)
    print("---------------------------------")
    
    save_message(message)
    
    read_message()
    
    show_exit_message()

if __name__ == "__main__":
    main()
