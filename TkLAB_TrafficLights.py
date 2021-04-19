"""LAB: Traffic lights

It's a set of rules describing the behavior of British-style traffic lights.
Assume that the very first element of all inner tuples is assigned to the
red light, the second - to the yellow, and the third - to the green one.
True means that the light is on, False - off.

As you see, there are four different phases:

the red light is lit,
the red and yellow lights are lit together,
the green light is lit,
the yellow light is lit.
Your task is to implement a model which will show how such a traffic signal works.

the model is built of three widgets:

the canvas being a background for all the three lights,
the button named "Next" - clicking it switches the signal to the next phase,
the button named "Quit" - clicking it immediately exits the program.
Note: use the phases tuple as a "knowledge base" for your whole code.
The code has to adopt to any change done to the tuple, e.g.,
there can be more or less than four phases and the lights'
combinations can be different also.

If traffic lights in your home country work in a different way,
you can implement your native scheme, but the only change you're allowed
to make is to modify the phases tuple - the code itself must remain the same.

"""
import tkinter as tk
from tkinter import Button, Canvas


PHASES = ((True,  False, False),
          (True,  True,  False),
          (False, False, True),
          (False, True,  False))

# class traffic_light():

    # def __init__(self, PHASES):
    #     PHASES = self.PHASES

def colour(state, light_id):
    """Return color of light or off"""
    colours = ('red', 'yellow', 'green', 'grey40')
    return colours[light_id] if state else colours[3]

# CURRENTPHASE=0
def loop_currnet_phase():
    """loop though currnet phase"""
    current_phase=0
    while True:
        print(current_phase)
        yield current_phase%4
        current_phase += 1
    # else:
    #     CURRENTPHASE=0

def change_colour():
    """Loop through light phases"""
    current_phase = next(gen)
    for index, light in enumerate(CANVAS.find_all()):
        CANVAS.itemconfig(CANVAS.find_all()[index],
        fill=colour(PHASES[current_phase][index], index))


gen = loop_currnet_phase()

Main_Window = tk.Tk()

CANVAS = Canvas(Main_Window, width=40, height=100, bg='grey20')
LIGHT1 = CANVAS.create_oval(5,5,35,35, outline='black', fill='grey40')
LIGHT2 = CANVAS.create_oval(5,35,35,65, outline='black', fill='grey40')
LIGHT2 = CANVAS.create_oval(5,65,35,95, outline='black', fill='grey40')
CANVAS.grid()

BUTTON = Button(Main_Window, text='Next',
command= change_colour)
# BUTTON.bind("<Button-1>", change_colour(CURRENTPHASE, PHASES, CANVAS))
BUTTON.grid(row=1)



Main_Window.mainloop()


# mylight = traffic_light(PHASES)
