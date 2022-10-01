# Author: Nikhil Patil
# Python Password Generator
# Generates Passwords

import string
import secrets

LETTERS = string.ascii_letters
DIGITS = string.digits
SPECIALCHARS = string.punctuation
ALPHABET = LETTERS+DIGITS+SPECIALCHARS  # Concatnate to create the alphabet


def main():
    pwdLength = int(input("Please input an integer: "))
    password = ""
    for i in range(pwdLength):
        password += "".join(secrets.choice(ALPHABET))
    print(password)


main()
