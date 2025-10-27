def save_message(message):
    #Save the message to a text file with error handling
    try:
        file = open("user_message.txt", "w")
        file.write(message)
        file.close()
        print("Message saved successfully.")
    except:
        print("Error: File not saved, try again")


def read_message():
    #Read and print the saved message with simple error handling"
    try:
        print("Reading saved message...")
        file = open("user_message.txt", "r")
        content = file.read()
        file.close()
        print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except:
        print("An unknown error occurred while reading the file.")