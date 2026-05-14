import tkinter as tk

window = tk.Tk()
window.config(background='gray')
scale = tk.Scale(window,
              from_=100, to=0,
              length=500,
              orient=tk.VERTICAL,
              font=('Consolas', 20),
              tickinterval=10,
              showvalue=1,
              resolution=5,
              troughcolor='light blue',
              fg='black',
              bg='white'
              )
scale.pack()

def submit():
    print("The temperature is: " + str(scale.get()) + " degrees C")

button = tk.Button(window,
                   text='Submit',
                   command=submit
                   )
button.pack()

window.mainloop()