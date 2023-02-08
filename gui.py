import tkinter as tk
from tkinter import *
from tkinter import messagebox
from generator import *

# Nikhil Patil
# February 7th 2023
# GUI for python password generator

def PopUp():
    '''
    Was originally supposed to be the first thing a user sees when they open the program
    Not utilized due it altering functionality
    '''
    messagebox.showinfo("Welcome!","Hi! Welcome to the password generator, this was just a passion project, so its functionality is quite limited (for now)\nThanks for checking it out! \(^-^)/")

def createCanvas(window, width, height):
    '''
    Function to create a canvas, takes parameters for the window, width, and the height
    '''
    canvas = tk.Canvas(window,width=width,height=height)
    return canvas

def intialize():
    '''
    Intializes and creates the GUI 
    '''
    window = tk.Tk()
    window.geometry("360x360")
    
    canvas = createCanvas(window,360,360)
    canvas.pack()


    welcomeLabel = tk.Label(window, text="Hi! Welcome to the password generator, this was just a passion project, so its functionality is quite limited (for now)\nThanks for checking it out! \(^-^)/", wraplength=150)
    canvas.create_window(180,50,window=welcomeLabel)

  
    entry = tk.Entry(window)
    canvas.create_window(180,300,window=entry)

    def getEntry():
        '''
        Function to retrieve the information the user input into the entry box
        '''
        entryValue = entry.get()
        return entryValue
    
    def genPassword():
        '''
        This function is called whenever a user presses the button, to generate their password and present it on a label
        '''
        label = tk.Label(window, text=gui_integerLenPassword(getEntry()))
        canvas.create_window(180,240, window=label)
        
    button = tk.Button(text="Generate Password", command=genPassword)

    canvas.create_window(180,180,window=button)

    entry.focus()
    window.mainloop()


def main():
    intialize()

if __name__ == "__main__":
    main()