# Write a simple game - an infinite game which humans cannot win. Here are the rules:
#
# the game goes on between TkInter and the user (probably you)
# TkInter opens a 500x500 pixel window and places a button saying "Catch me!" in the top-left corner of the window;
# if the user moves the mouse cursor over the button, the button immediately jumps to another location inside the window; you have to assure that the new location is distant enough to prevent the user from making an instant click,
# the button must not cross the window's boundaries during the jump!

import tkinter as tk
import random

Main_Window = tk.Tk()


def move(event=None):
    global width, height
    global button
    bwidth, bheight = button.winfo_width(),button.winfo_height()
    xpos = random.randint(1, width-bwidth)
    while abs(xpos-button.winfo_x()) <bwidth:
        xpos = random.randint(1, width-bwidth)
    ypos = random.randint(1, height-bheight)
    button.place(x=xpos, y=ypos)
    # print(f"{button.winfo_x()}, {button.winfo_y()}, {button.winfo_width()}")

width, height = 500, 500
Main_Window.title("Catch Me!")
Main_Window.minsize(width=width, height=height)
Main_Window.maxsize(width=width, height=height)
Main_Window.geometry(f"{width}x{height}")


button = tk.Button(Main_Window, text="Catch Me!")
button.bind("<Enter>", move)
button.place(x=15, y=15)

Main_Window.mainloop()
