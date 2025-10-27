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
    