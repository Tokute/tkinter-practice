import tkinter as tk


def add():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())

def submit():
    food = []

    for i in listbox.curselection():
        food.insert(i, listbox.get(i))

    print("You ordered: ")

    for i in food:
        print(i)

def delete():
    #listbox.delete(listbox.curselection())
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())

window = tk.Tk()

listbox = tk.Listbox(window,
                     bg="gray",
                     font=('Arial', 30),
                     width=12,
                     selectmode=tk.MULTIPLE)

listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Garlic Bread")
listbox.insert(4, "Soup")
listbox.insert(5, "Salad")

listbox.config(height=listbox.size())
listbox.pack()

entry_box = tk.Entry(window)
entry_box.pack()

add_button = tk.Button(window,
                       text="Add",
                       command=add)
add_button.pack()

submit_button = tk.Button(window,
                       text="Submit",
                       command=submit)
submit_button.pack()

delete_button = tk.Button(window,
                        text="Delete",
                        command=delete)
delete_button.pack()


window.mainloop()