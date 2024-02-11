"""
Accept a string as input. Your task is to determine if the input string is a valid password or not. 
For a string to be a valid password, it must satisfy all the conditions given below:
(1) It should have at least 8 and at most 32 characters
(2) It should start with an uppercase or lowercase letter
(3) It should not have any of these characters: / \ = ' "
(4) It should not have spaces
It could have any character that is not mentioned in the list of characters to be avoided (points 3 and 4). 
Output True if the string forms a valid password and False otherwise.
"""

import re

PASSWORD_REGEX: str = re.compile(r'^[a-zA-Z](?!.*[\/\\=\'\" ]).{6,30}$')


def check_password_v1(password: str = "password") -> bool:
    unallowed_chars = ("/", "\\", "=", "'", '"')
    blank_space = " "
    if len(password) < 8 or len(password) > 32:
        print("Length of the password must be between 8 and 32 characters.")
        return False
    if not password[0].isalpha():
        print("The password must begin with an alphabetic character.")
        return False
    for item in unallowed_chars:
        if item in password:
            print(f"The password cannot contain the illegal character:\t'{item}'.")
            return False
    if blank_space in password:
        print("The password cannot contain a blank space.")
        return False

    return True

def check_password_v2(password:str="password") -> bool:
    return bool(re.match(PASSWORD_REGEX, password))

def main():
    password = "passwo\\rd"
    # print(check_password_v1(password=password))
    print(check_password_v2(password=password))

if __name__=="__main__":
    main()