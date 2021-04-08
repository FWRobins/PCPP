# We want you to write a simple but challenging game,
# which can help many people to improve their perception skills and visual memory.
# We'll call the game The Clicker as clicking is what we expect from the player.
# The Clicker's board consists of 25 buttons and each of the buttons contains
# a random number from range 1..999. Note: each number is different!
# Below the board there is a timer which initially shows 0. The timer starts
# when the user clicks the board for the first time.
#
# We expect the player to click all the buttons in the order imposed
# by the numbers - from the lowest to the highest one. Additional rules say that:
# the properly clicked button changes the button's state to DISABLED
# (it greys the button out)
# the improperly clicked button shows no activity,
# the timer increases its value every second,
# when all the buttons are greyed out (i.e., the player has completed his/her task)
# the timer stops immediately.


import tkinter as tk
from tkinter import messagebox
import random

Main_Window = tk.Tk()
Main_Window.title("Numbers Game")

messagebox.showinfo("Goal", "Select all number in numerical order")

# get list of 25 unique numbers
list = random.sample(range(1000), 25)

# check if started, else start timer
started = False
def start():
    global started
    if not started:
        started = True
        Main_Window.after(1000, label_time)

# update timer label every second
time_count = 0
def label_time():
    global time_count
    global label
    global list
    time_count +=1
    label['text'] = time_count
    if list:
        Main_Window.after(1000, label_time)

# check button clicked, disable and remove from list
def click(event=None):
    start()
    if event.widget.cget("text") == list[0]:
        event.widget.config(state=tk.DISABLED)
        list[:] = list[1:]


# buttons = []
for i in range(len(list)):
    button = tk.Button(Main_Window, text = list[i], width=5)
    button.grid(row=i//5, column=i%5)
    button.bind("<Button-1>", click)
    # buttons.append(button)

# sort list numerically
list.sort()

label = tk.Label(Main_Window, text="0")
label.grid(row=5, columnspan=5)


Main_Window.mainloop()
