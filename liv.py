from tkinter import *
import time

resolution_x = 680
resolution_y = 480
resolution = str(resolution_x) + "x" + str(resolution_y)

window = Tk()
#window.geometry(resolution)
window.title("First GUI Program for Andrew")

icon = PhotoImage(file="app-store.png")
window.iconphoto(True, icon)
window.config(background="black")

photo_liv = PhotoImage(file='liv.png')

label = Label(window,
              text="Segs",           # Text of the label
              font=('Arial', 40, 'bold'),   # font of the text
              fg='white',                 # Foreground which means text color
              bg='black',                   # Background for the label
              relief=RAISED,                # Border style either RAISED or SUNKEN
              bd=10,                        # Border size
              padx=10,                      # padx is the amount of space between the border and the text label. Horizontal spacing
              pady=10,                      # pady is padx but vertical spacing
              image=photo_liv,              # image to put in the label
              compound='top')               # compound is where the image should be compared to text

label.pack()
#label.place(x=resolution_x/2,y=resolution_y/2)

class Shotgun():
    def __init__(self):
        self.ammo = 6

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            print("PEW!")
        else:
            print("No more ammo!")

    def reload(self):
        self.ammo = 6
        print("LOCK AND LOADED!")

    def get_ammo(self):
        return self.ammo

shotgun = Shotgun()

button_reload = Button(window,
                       command=shotgun.reload,
                       text="Reload",
                       font=('Arial', 20),
                       fg='white',
                       bg='black',
                       activeforeground='white',
                       activebackground='yellow',
                       state=ACTIVE)
button_reload.pack(side="bottom")


button_shoot = Button(window,
                      command=shotgun.shoot,        # when pressed, runs the command
                      text="Shoot",
                      font=("Arial, 20"),
                      fg='white',
                      bg='black',
                      activeforeground='white',   # when pressed shows this foreground color
                      activebackground='yellow',    # when pressed shows this background color
                      state=ACTIVE)    
button_shoot.pack(side="bottom")


window.mainloop()