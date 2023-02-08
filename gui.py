import tkinter as tk
from tkinter import *
from generator import *

# Nikhil Patil
# February 7th 2023
# GUI for python password generator

def intialize():
    window = tk.Tk()

    window.geometry("480x480")

    label = tk.Label(text="Hello World",foreground="black",background="white")
    
    #show the label in the window
    label.pack()
    window.mainloop()


def main():
    intialize()
    pass
    # print(integerLenPassword())

main()