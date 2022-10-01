import tkinter as tk
from turtle import back, color

def intialize():
    window = tk.Tk()

    label = tk.Label(text="Hello World",foreground="black",background="white")
    #show the label in the window
    label.pack()
    window.mainloop()


def main():
    intialize()

main()