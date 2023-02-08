# Author: Nikhil Patil
# Python Password Generator
# Generates Passwords

import string
import secrets


LETTERS = string.ascii_letters
DIGITS = string.digits
SPECIALCHARS = string.punctuation
ALPHABET = LETTERS+DIGITS+SPECIALCHARS  # Concatnate to create the alphabet

def cli_integerLenPassword():
    '''
    Name: integerLenPassword
    Purpose: Creates a password of variable length as indicated by user
    Return: Strings
    '''
    failsafe = 0
    while(True):
        choice = input("Enter a choice:\n1 create password\n2 Exit\nChoice: ")
        if(choice == "1"):
            password = ""
            passwordLen = int(input("Please enter the length of your password: "))
            for i in range(passwordLen):
                password += "".join(secrets.choice(ALPHABET))
            return password
        elif(choice == "2"):
            return "The program is exiting..."
        elif(failsafe == 2):
            return "The failsafe has engaged. Exiting..."
        else:
            print("\nThe value entered is invalid\n")
            failsafe += 1

def mkInt(s):
    s = s.strip()
    return int(s) if s else 0

def gui_integerLenPassword(length):
    password = ""
    length = mkInt(length)
    for i in range(length):
        password += "".join(secrets.choice(ALPHABET))
    return password
    
if __name__ == "__main__":
    print(gui_integerLenPassword("10"))