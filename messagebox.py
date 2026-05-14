import tkinter as tk
from tkinter import messagebox

def click():
    #messagebox.showinfo(title="This is an info message box",
    #                    message="Hello")
    #messagebox.showwarning(title="Warning!",
    #                       message="You are skibidi!")
    #messagebox.showerror(title="Error",
    #                     message="Something went wrong.")
    """
    if messagebox.askokcancel(title="Ask ok cancel",
                           message="Do you want to do the thing?"):
        messagebox.showinfo(title="The thing", message="You did the thing!")
        print("You did the thing!")
    else:
        messagebox.showinfo(title="The thing", message="You did not do the thing.")
        print("You did not do the thing.")
    """

    if messagebox.askokcancel(title="Ask ok cancel",
                           message="Do you want to do the thing?"):
        print("You did the thing!")
    else:
        print("You did not do the thing.")

    # if messagebox.askretrycancel() returns (also 1 or 0?)
    # if messagebox.askyesno() # returns True or False (or 1 or 0?)
    # if messagebox.askyesnocancel() returns True, False, None, icon=["warning", "info", "error"]
    # answer = messagebox.askquestion()


        


window = tk.Tk()

button = tk.Button(window,
                command=click,
                text="Click me!")
button.pack()

window.mainloop()