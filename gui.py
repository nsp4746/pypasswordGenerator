import tkinter as tk
from tkinter import *
from tkinter import messagebox
from generator import *

# Nikhil Patil
# February 7th 2023
# GUI for python password generator

def PopUp():
    messagebox.showinfo("Welcome!","Hi! Welcome to the password generator, this was just a passion project, so its functionality is quite limited (for now)\nThanks for checking it out! \(^-^)/")

def prompt():
    messagebox.showinfo("New Notification","Click okay to proceed")


def createCanvas(window, width, height):
    canvas = tk.Canvas(window,width=width,height=height)
    return canvas





def intialize():
    window = tk.Tk()
    window.geometry("360x360")
    
    canvas = createCanvas(window,360,360)
    canvas.pack()
    
    entry = tk.Entry(window)
    canvas.create_window(180,300,window=entry)
    length = entry.get()

    def genPassword():
        label = tk.Label(window, text=gui_integerLenPassword(length))
        canvas.create_window(180,240, window=label)
        
    button = tk.Button(text="Generate Password", command=genPassword)

    canvas.create_window(180,180,window=button)

    #PopUp()
    window.mainloop()
    
def GUI():
    intialize()

def main():
    GUI()

if __name__ == "__main__":
    main()