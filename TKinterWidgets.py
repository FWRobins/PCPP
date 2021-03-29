import tkinter as tk
from tkinter import messagebox

def Close_window():
    reply = messagebox.askquestion("Quit?", "Are you sure?")
    if reply == 'yes':
        Main_Window.destroy()

def Click_Button(event=None):
    if event is None:
        messagebox.showinfo('info', 'button 1 disabled\nlabel disabled')
        button.config(command=lambda:None, text="(disabled!)")
        label.unbind('<Button-1>')
        label.config(text="disabled")
    else:
        string = f"x={event.x}, y={event.y},\n"+\
        f"num={event.num}, type={event.type},\n"+\
        f"button 1 enabled\nlabel enabled"
        messagebox.showinfo("Click!", string)
        button.config(command=Click_Button, text="Button 1")
        label.bind('<Button-1>', Click_Button)
        label.config(text="Little label")


Main_Window = tk.Tk()

Main_Window.title("Main Window")

label = tk.Label(Main_Window, text="Little label", font=("Times", "12"), cursor="heart")
label.bind('<Button-1>', Click_Button)
label.grid(ipadx=50)

frame = tk.Frame(Main_Window, height=30, width=100, bg='#000099')
frame.bind('<Button-1>', Click_Button)
frame.grid(row=1)

button = tk.Button(Main_Window, text="Button 1", command=Click_Button, font=("Arial", "16", "bold"))
button.grid(row=2, ipadx=50)

#all widgets set to the same variable switch will be affected
switch = tk.IntVar()
switch.set(1)

checkbutton = tk.Checkbutton(Main_Window, text="Check Button", variable=switch)
checkbutton.grid(row=3)

entry = tk.Entry(Main_Window, width=30)
entry.grid(row=4)

#radio buttons linked via 'variable'
radiobutton_1 = tk.Radiobutton(Main_Window, text='Salad', variable=switch, value=0)
radiobutton_1.grid(row=5)
radiobutton_2 = tk.Radiobutton(Main_Window, text='Steak', variable=switch, value=1)
radiobutton_2.grid(row=6)

def on_off():
    global button_2
    state = button_2["text"]
    state = "OFF" if state == "ON" else "ON"
    button_2["text"] = state

button_2 = tk.Button(Main_Window, text="OFF", command=on_off)
button_2.grid(row=7)

def on_off2():
    global button_3
    state = button_3.cget("text")
    state = "OFF" if state == "ON" else "ON"
    button_3.config(text=state)

button_3 = tk.Button(Main_Window, text="OFF", command=on_off2)
button_3.grid(row=8)

def blink(event=None):
    global is_white
    color = "black" if is_white else "white"
    is_white = not is_white
    frame_2.config(bg=color)
    frame_2.after(500, blink)

is_white = True
frame_2 = tk.Frame(Main_Window, width=200, height=100, bg="white")
frame_2.bind("<Button-1>", blink)
# frame_2.after(500, blink)
frame_2.grid(row=9)

def suicide():
    frame_3.destroy()

frame_3 = tk.Frame(Main_Window, width=200, height=100, bg='green')
buttonf = tk.Button(frame_3, text='child of the frame')
buttonf.place(x=10, y=10)
frame_3.after(5000, suicide)
frame_3.grid(row=10)

def flip_focus():
    button_5.focus_set() if Main_Window.focus_get()  is button_4 else button_4.focus_set()
    Main_Window.after(1000, flip_focus)

button_4 = tk.Button(Main_Window, text='first')
button_4.grid(row=11)
button_5 = tk.Button(Main_Window, text='second')
button_5.grid(row=12)
Main_Window.after(1000, flip_focus)

# observers
def r_observer(*args):
    print('reading')

def w_observer(*args):
    print('writing')

variable = tk.StringVar()
variable.set('abc')
r_obsid = variable.trace('r', r_observer)
w_obsid = variable.trace('w', w_observer)
variable.set(variable.get()+'d')
variable.trace_vdelete('r', r_obsid)
variable.set(variable.get()+'e')
variable.trace_vdelete('w', w_obsid)
variable.set(variable.get()+'f')
print(variable.get())

Main_Window.mainloop()
