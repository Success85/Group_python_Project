def create_message(name, age, name_binary, age_binary):
    message_lines = [
        f"Hello {name}, you are {age} years old"
        f"Name in binary: {name_binary}"
        f"Age in binary: {age_binary}"
    ]


full_message = "\n".join(message_lines)
return full_message
