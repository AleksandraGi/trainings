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
# window.geometry("500x600")                                  # size of the window
window.title("GUI")                                         # window's title

icon = PhotoImage(file='images\\cat.png')                   # path to window's icon
window.iconphoto(True, icon)                                # window's icon

window.config(background=BACKGROUND_COLOUR)                 # background colour

# labels
"""
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
"""

#buttons
"""
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

"""

# user input
"""
# # ------- USER INPUT -------
# def submit():   
#     username = entry.get()                              # saves input into a variable
#     print(username)

# def delete():
#     entry.delete(0, END)                                # deletes the whole line of text

# def backspace():
#     entry.delete(len(entry.get())-1, END)               # deletes last character

# submit_button = Button(window, text="Submit", command=submit)
# submit_button.pack(side="left")

# delete_button = Button(window, text="Delete", command=delete)
# delete_button.pack(side="right")

# backspace = Button(window, text="Backspace", command=backspace)
# backspace.pack(side="right")

# def limit_size(new_text):
#     return len(new_text) <= 10

# entry = Entry(window,
#     font=("Times New Roman", 50),
    
#     bg="pink",
#     fg="dark blue",
#     width=12,
#     show="*",                                               # replaces everything we write into *
#     validate="key"
# )
# # entry.insert(0, "teXt")                                   # text visible when you open the app
# # entry.config(state=DISABLED)                              # ACTIVE or DISABLED

# vcmd = (window.register(limit_size), "%P")
# entry.config(validatecommand=vcmd)

# entry.pack()

"""

#checkbuttons
"""
# # ------- CHECKBUTTONS -------
# x = IntVar()
# y = IntVar()

# def display():
#     if x.get() == 1 and y.get() == 0:
#         print("You chose red")
#     elif x.get() == 0 and y.get() == 1:
#         print("You chose pink")
#     elif x.get() == 0 and y.get() == 0:
#         print("You didn't choose your colour")
#     else:
#         print("You chose both colours")

# red_photo = PhotoImage(file='images\\red.png')
# pink_photo = PhotoImage(file='images\\pink.png')

# checkbox_red = Checkbutton(
#     window, 
#     text="Red", 
#     bg=BACKGROUND_COLOUR,
#     fg="red",
#     variable=x,
#     onvalue=1,                              # what x is equal to when the button is checked
#     offvalue=0,                             # what x is equal to when the button is unchecked
#     command=display
#     )

# checkbox_red.config(
#     font=("Arial", 20),
#     activeforeground="red"
#     )

# checkbox_red.config(
#     image=red_photo,
#     compound="left"
# )
# checkbox_red.config(padx=25, pady=10, width=250, height=50)
# checkbox_red.config(anchor="w")
# checkbox_red.pack()


# checkbox_pink = Checkbutton(
#     window, text="Pink", 
#     bg=BACKGROUND_COLOUR,
#     fg="pink",
#     variable=y,
#     onvalue=1,                              # what x is equal to when the button is checked
#     offvalue=0,                             # what x is equal to when the button is unchecked
#     command=display
#     )
# checkbox_pink.config(
#     font=("Arial", 20),
#     activeforeground="pink"
#     )

# checkbox_pink.config(
#     image=pink_photo,
#     compound="left"
# )
# checkbox_pink.config(padx=25, pady=10, width=250, height=50)
# checkbox_pink.config(anchor="w")


# checkbox_pink.pack()
"""

# radiobuttons
"""
# ------- RADIOBUTTONS ------- (you can select only one from a group)
food = ["pizza", "hamburger", "hotdog"]

def order():
    if x.get() == 0:
        print("You ordered pizza")
    elif x.get() == 1:
        print("You ordered a burger")
    elif x.get() == 2:
        print("You ordered a hot dog")
    else:
        print("nah")

x = IntVar()

photo_pizza = Image.open('images\\pizza.png')
photo_pizza = photo_pizza.resize((125,125))
photo_pizza = ImageTk.PhotoImage(photo_pizza)

photo_burger = Image.open('images\\burger.png')
photo_burger = photo_burger.resize((125,125))
photo_burger = ImageTk.PhotoImage(photo_burger)

photo_hotdog = Image.open('images\\hot-dog.png')
photo_hotdog = photo_hotdog.resize((125,125))
photo_hotdog = ImageTk.PhotoImage(photo_hotdog)


# photo_pizza = PhotoImage(file='images\\pizza.png')
# photo_burger = PhotoImage(file='images\\burger.png')
# photo_hotdog = PhotoImage(file='images\\hot-dog.png')
food_images = [photo_pizza, photo_burger, photo_hotdog]

for index in range(len(food)):
    radiobutton = Radiobutton(window,       
                              text=food[index],         # adds text to radiobutttons
                              variable=x,               # groups radiobuttons together if thety share the same variable
                              value=index,              # assigns each radiobutton a different value
                              padx=25,                  # adds padding on x-axis
                              font=("Impact", 50),
                              image=food_images[index], # adds image to radiobutton
                              compound="left",          # adds image and text (left side)
                              indicator=0,              # eliminates circle indicators
                              width=500,                # sets width of buttons
                              command=order             # set command of buttons to function
    )
    # print(x, index)           # PY_VAR0 0     PY_VAR0 1   PY_VAR0 2

    radiobutton.pack(anchor=W)
"""



window.mainloop()                                           # place window on a screen