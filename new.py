# Author: Nikhil Patil
# Python Password Generator
# Generates Passwords

import string
import secrets

LETTERS = string.ascii_letters 
DIGITS = string.digits
SPECIALCHARS = string.punctuation
ALPHABET = LETTERS+DIGITS+SPECIALCHARS # Concatnate to create the alphabet

def main():
    print("Hello World")

main()