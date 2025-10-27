def validate_input(user_input):
    if not isinstance(user_input, str):
        print("Error: Input must be a string.")
        return False
    if user_input.strip() == "":
        print("Error: Input cannot be empty.")
        return False
    return True


def convert_to_binary(text):
    if text.isdigit():
        number = int(text)
        binary_number = bin(number)
        return binary_number
    else:
        binary_chars = ord(char)
        binary_char = format(ascii_value, '08b')
        binary_chars.append(binary_char)
        return ''.join(binary_chars)


def create_message(name, age, name_binary, age_binary):
    message_lines = [
        f"Hello {name}, you are {age} years old"
        f"Name in binary: {name_binary}"
        f"Age in binary: {age_binary}"
    ]


full_message = "\n".join(message_lines)
return full_message
