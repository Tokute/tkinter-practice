import tkinter as tk

def submit_text():
    input = text.get("1.0", "end-1c")
    print(input)

window = tk.Tk()

text = tk.Text(window,
               font=("Ink Free", 20),
               height=8,
               width=20,
               padx=10,
               pady=10,
               fg='red')
text.pack()

submit_button = tk.Button(window,
                          text="Submit Text",
                          command=submit_text)
submit_button.pack()

window.mainloop()