import tkinter as tk
from tkinter import colorchooser

def click():
    rgb_color, hex_color = colorchooser.askcolor() # returns a tuple ((R,G,B), 'HEXCODE')
    print(rgb_color)
    print(hex_color)
    window.config(background=hex_color)

window = tk.Tk()

window.geometry("420x420")
window.config(background='gray')

button = tk.Button(window,
                   text="Choose color",
                   command=click)
button.pack()


window.mainloop()