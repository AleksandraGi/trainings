# https://www.youtube.com/watch?v=lyoyTlltFVU&list=PLZPZq0r_RZOOeQBaP5SeMjl2nwDcJaV0T

from tkinter import *

BACKGROUND_COLOUR = "#484848"
# BACKGROUND_COLOUR = '#FFFFFF'

window = Tk()
window.geometry("400x300")
window.title("GUI")

icon = PhotoImage(file='tkinter_training\images\cat.png')
window.iconphoto(True, icon)

window.config(background=BACKGROUND_COLOUR)

window.mainloop()