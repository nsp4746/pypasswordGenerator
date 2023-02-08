import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from generator import *

# Nikhil Patil
# February 7th 2023
# GUI for python password generator

def PopUp():
    messagebox.showinfo("Welcome!","Hi! Welcome to the password generator, this was just a passion project, so its functionality is quite limited (for now)\nThanks for checking it out! \(^-^)/")

def prompt():
    messagebox.showinfo("New Notification","Click okay to proceed")
    
def intialize():
    window = tk.Tk()

    window.geometry("360x360")

    label = tk.Label(window,text="Hello World",foreground="black",background="white")
    label.pack(pady=15)

    ttk.Button(window, text="Open",command=prompt).pack()

#--------------------------------------------
    


    PopUp()
    window.mainloop()

def GUI():
    intialize()

def main():
    intialize()

main()