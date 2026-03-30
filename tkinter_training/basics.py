# https://www.youtube.com/watch?v=lyoyTlltFVU&list=PLZPZq0r_RZOOeQBaP5SeMjl2nwDcJaV0T

from tkinter import *
from PIL import Image, ImageTk


BACKGROUND_COLOUR = "#FFFFFF"
TEXT_COLOUR = "#6A1411"
BUTTON_COLOUR = "#522990"
BUTTON_TEXT_COLOUR = "#FFFFF9"
BUTTON_ACTIVE_BACK_COLOUR = "#ED10ED"
BUTTON_ACTIVE_FRONT_COLOUR = "#000000"


# ------- WINDOW ------- (serves as a container to keep widgets)
window = Tk()                                               # instantiate an instance of a window
window.geometry("500x600")                                  # size of the window
window.title("GUI")                                         # window's title

icon = PhotoImage(file='tkinter_training\images\cat.png')   # path to window's icon
window.iconphoto(True, icon)                                # window's icon

window.config(background=BACKGROUND_COLOUR)                 # background colour


# # ------- LABELS ------- (an area widget that hold texts and/or an image within a window)   https://www.tutorialspoint.com/python/tk_label.htm
# photo = Image.open('tkinter_training\\images\\cat_drawing.jpg')
# photo = photo.resize((125,125))
# photo = ImageTk.PhotoImage(photo)

# label = Label(window, 
#               text="Hello", 
#               font=("Arial", 40,'bold'), 
#               bg=BACKGROUND_COLOUR, 
#               fg=TEXT_COLOUR,
#               relief=RAISED,                                # border style
#               bd=10,                                        # size of the border
#               padx=20,                                      # space between text and border (horizontal padding)
#               pady=20,                                      # vertical padding
#               image=photo,
#               compound="bottom"
# )

# # label.place(x=0, y=0)                                     # place the label in a specific place
# label.pack()


# # ------- BUTTON ------- (click it and sth happens)
# count = 0
# def click():
#     global count
#     count += 1
#     label2.config(text=f"Counter: {count}")
#     label3.pack()

# button = Button(window, text="Click me")
# button.config(command=click)                                # performs call back of function
# button.config(font=('Ink Free', 25, 'italic'))
# button.config(bg=BUTTON_COLOUR, fg=BUTTON_TEXT_COLOUR)
# button.config(activebackground=BUTTON_ACTIVE_BACK_COLOUR, activeforeground=BUTTON_ACTIVE_FRONT_COLOUR)

# button_icon = Image.open("tkinter_training\\images\\arrow-with-scribble.png")
# button_icon = button_icon.resize((50,50))
# button_icon = ImageTk.PhotoImage(button_icon)
# button.config(image=button_icon)
# button.config(compound="top")

# # button.config(state=DISABLED)                               # disables button (DISABLED or ACTIVE)

# label2 = Label(window, text="Counter", font=("Monospace", 15), bg=BACKGROUND_COLOUR)
# label2.pack()

# label3 = Label(window, image=button_icon)

# button.pack()


# ------- USER INPUT -------
def submit():
    username = entry.get()
    print(username)

def delete():
    entry.delete(0, END)



submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side="left")

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side="right")


def limit_size(new_text):
    return len(new_text) <= 10

entry = Entry(window,
    font=("Times New Roman", 50),
    bg="pink",
    fg="dark blue",
    width=12,
    show="*",                                               # replaces everything we write into *
    validate="key"
)
# entry.insert(0, "teXt")                                   # text visible when you open the app
# entry.config(state=DISABLED)                              # ACTIVE or DISABLED

vcmd = (window.register(limit_size), "%P")
entry.config(validatecommand=vcmd)



entry.pack()




window.mainloop()                                           # place window on a screen