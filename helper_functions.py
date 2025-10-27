# creating a function named 'validate_input' that takes name and age and check their validity
def validate_input(name, age):
    # check if the instance 'name' is instance of the object 'str'. And Check if 'name' is not empty
    if isinstance(name, str) and name:
        # if 'name' passed the test. Try to change the 'age' to int
        try:
            age=int(age)
            # if 'age' successfuly changed to int type then check if it is greater than zero and return True, name, age
            if age > 0:
                return True, name, age
            # if age is less than or equal to zero tell the user the age was invalid and return False, name, None(because age was invalid)
            else:
                print("Invalid age")
                return False, name, None
        # if 'age' can not be converted to int type, hence, not a number tell the user the age was invalid and return False, name, None(because age was invalid)
        except ValueError:
            print("Invalid age")
            return False, name, None
        # if the name is not a string or is empty tell the user the name is invalid and return False, None, None(because both name and age were invalid)
    else:
        print("Invalid name")
        return False, None, None
    
# define a function named 'convert_to_binary' that takes 'name' and 'age', and convert them to binary number
def convert_to_binary(name, age):
    # pass age to built-in function called 'bin' that will change  intiger to binary number and store the result in a variable called 'binary_number'
    binary_number = bin(age)
    # convert each character in name to its 8 bit long binary number form, join them and store it in variable called 'binary_value'
    binary_value = ''.join(format(ord(char), '08b') for char in name)
    # return binary number of name and age
    return binary_value, binary_number

def create_message(name, age, name_binary, age_binary):
    message_lines = (
        f"Hello {name}, you are {age} years old\n"
        f"Name in binary: {name_binary}\n"
        f"Age in binary: {age_binary}\n"
    )

    return message_lines
