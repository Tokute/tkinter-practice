from tkinter import *

def submit():
    username = entry.get()
    print("Hello " + username)

def clear():
    entry.delete(0, END)

window = Tk()

title_label = Label(window,
                    text="Login Screen",
                    font=("Arial", 50, 'bold'),
                    fg='white',
                    bg='gray',
                    padx=20,
                    pady=20,
                    relief=RAISED,
                    bd=20)
title_label.pack(side='top')

entry = Entry(window,
              font=("Arial", 20))
entry.pack(side="left")

submit_button = Button(window,
                       text="submit",
                       command=submit)
submit_button.pack(side="right")

clear_button = Button(window,
                       text="clear",
                       command=clear)
clear_button.pack(side="right")


window.mainloop()