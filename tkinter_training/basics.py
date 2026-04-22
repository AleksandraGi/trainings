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

# scale
"""
# ------- SCALE -------
def submit():
    print("The temperature: " + str(scale.get()) + " degrees C")

fire_image = Image.open('images\\fire.png')
fire_image = fire_image.resize((75,75))
fire_image = ImageTk.PhotoImage(fire_image)
fire_label = Label(image=fire_image)
fire_label.pack()


scale = Scale(window, 
              from_=100, 
              to=0,
              length=600,
              orient=VERTICAL,          # orientation of scale
              font=("Consolas", 20),
              tickinterval=10,          # adds numeric indicators for value
            #   showvalue=0,              # hide current value
              resolution=5,             # increment of slider
              troughcolor="#69EAFF",
              fg="#FF1C00",
              bg="#111111",

              )
scale.set(((scale['from']-scale['to']) / 2) + scale['to'])

scale.pack()


ice_image = Image.open('images\\snowflake.png')
ice_image = ice_image.resize((75,75))
ice_image = ImageTk.PhotoImage(ice_image)
ice_label = Label(image=ice_image)
ice_label.pack()

button = Button(window, text="sumbit", command=submit)
button.pack()
"""

# listboxes
"""
# ------- LISTBOXES ------- (listing of selectable text items within it's own container)
def submit():
    # print("Your order: ", listbox.get(listbox.curselection()))      # works if selectmode jest dla jednego wyboru
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    
    print("You have ordered: ")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())           # adjust size dynamically

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    # listbox.delete(listbox.curselection())          # works only for selectmode=single
    listbox.config(height=listbox.size())           # adjust size dynamically


listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 35),
                  width=12,
                  selectmode=MULTIPLE
                  )
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.config(height=listbox.size())           # adjust size dynamically

entry_box = Entry(window)
entry_box.pack()
add_button = Button(window, text="add", command=add)
add_button.pack()

delete_button = Button(window, text="delete", command=delete)
delete_button.pack()

submit_button = Button(window, text="submit", command=submit)
submit_button.pack()
"""

# messageboxes
"""
# ------- MESSAGEBOXES ------- 
from tkinter import messagebox

def click():
    # messagebox.showinfo(title="Infomessage box", message="You are dumb")

    # while True:
    #     messagebox.showwarning(title="Warrning", message="You are an idiot")        # infinite warning box

    # messagebox.showerror(title="error", message="You are an error")

    # if messagebox.askokcancel(title="Ask ok cancel", message="do you want to do the thing?"):
    #     print("you did the thing")
    # else:
    #     print("you did not do the thing")

    # if messagebox.askretrycancel(title="ask ok cancel", message="do you want to retry the thing?"):
    #     print("you did the thing")
    # else:
    #     print("you did not do the thing")

    # if messagebox.askyesno(title="yes or no", message="do you like cake?"):
    #     print("good")
    # else:
    #     print("what's wrong with you")

    # answer = messagebox.askquestion(title="ask question", message="do you like pizza?")
    # if answer == "yes":
    #     print("good")
    # else:
    #     print("you need a doctor")

    answer = messagebox.askyesnocancel(title="yes no cancel", message="do you like?", icon='warning')       # icons: info, error, warning
    if answer == True:
        print("you like")
    elif answer == False:
        print("you don't like")
    else:
        print("what")


button = Button(window, command=click, text='click me')
button.pack()
"""

# colorchooser
"""
# ------- COLORCHOOSER ------- 

from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    color_hex = color[1]
    window.config(bg=color_hex)                 # change background color
    # window.config(bg=colorchooser.askcolor()[1])

window = Tk()
window.geometry("420x420")
button = Button(text="CLICK ME", command=click)
button.pack()
"""


window.mainloop()                                           # place window on a screen 