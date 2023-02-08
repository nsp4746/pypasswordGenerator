# Author: Nikhil Patil
# Python Password Generator
# Generates Passwords

import string
import secrets


LETTERS = string.ascii_letters
DIGITS = string.digits
SPECIALCHARS = string.punctuation
ALPHABET = LETTERS+DIGITS+SPECIALCHARS  # Concatnate to create the alphabet


def integerLenPassword():
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



def main():
    print(integerLenPassword())


main()
