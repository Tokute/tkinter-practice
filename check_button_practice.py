import tkinter as tk

food = ["pizza", "hamburger", "hotdog"]

window = tk.Tk()

x = tk.IntVar()

def display():
    if x.get() == 1:
        print("You agreed to something.")
    else:
        print("You disagreed to something.")

check_button = tk.Checkbutton(window,
                              text="I agree to something.",
                              font=('Arial', 20),
                              fg='#00FF00',
                              bg='black',
                              activeforeground='#00FF00',
                              activebackground='black',
                              variable=x,
                              onvalue=1,
                              offvalue=0,
                              command=display,
                              padx=25,
                              pady=10)
check_button.pack()

y = tk.IntVar()

def order():
    if y.get() == 0:
        print("You ordered pizza.")
    elif y.get() == 1:
        print("You ordered hamburger.")
    elif y.get() == 2:
        print("You ordered hotdog.")

for i in range(len(food)):
    radio_button = tk.Radiobutton(window,
                                  text=food[i],
                                  font=('Impact', 50),
                                  variable=y,
                                  value=i,
                                  padx=25,
                                  indicatoron=0,
                                  width=10,
                                  command=order)
    radio_button.pack(anchor='w')


window.mainloop()