import tkinter as tk
from tkinter import messagebox

def Close_window(event=None):
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
Main_Window.minsize(width=250, height=200)
Main_Window.maxsize(width=900, height=600)
Main_Window.geometry("800x600")

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

#menus

def about_app():
    messagebox.showinfo("app", "the app that\ndoes nothing")

def open_file():
    messagebox.showinfo("Open Doc", 'we will open a file here')

main_menu = tk.Menu(Main_Window)
Main_Window.config(menu=main_menu)

sub_menu_file = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='File', menu=sub_menu_file, underline=0)
sub_menu_file.add_cascade(label='Open...', underline=0, command=open_file)
sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
sub_menu_file.add_cascade(label='Open recent...', underline=5, menu=sub_sub_menu_file)

for i in range(8):
    number =  str(i+1)
    sub_sub_menu_file.add_cascade(label=f'{number}. file.txt', underline=0)

def on_off3():
    global accessible
    if accessible == tk.DISABLED:
        accessible = tk.ACTIVE
    else:
        accessible = tk.DISABLED
    sub_menu_file.entryconfigure(3, state = accessible)

accessible = tk.DISABLED
sub_menu_file.add_cascade(label="On/Off", command=on_off3)
sub_menu_file.add_cascade(label='Switch', state=tk.DISABLED)

sub_menu_file.add_separator()
sub_menu_file.add_command(label='Quit', underline=0, command=Close_window, accelerator="Ctrl+Q")

sub_menu_about = tk.Menu(main_menu)
main_menu.add_cascade(label='About...', command=about_app, underline=1)

#global bind ctrl+q to Close
Main_Window.bind_all("<Control-q>", Close_window)

#close app popup when 'X' is clicked
Main_Window.protocol("WM_DELETE_WINDOW", Close_window)

# pre-defined modal Window
def question():
    # answer = messagebox.askyesno("?","to be or not to be") #returns 1 or 0
    # answer = messagebox.askokcancel("?","to be or not to be") #returns 1 or 0
    # answer = messagebox.askretrycancel("?","to be or not to be") #returns 1 or 0
    answer = messagebox.askquestion("?","to be or not to be") #returns 'yes' or 'no'
    # messagebox.showinfo('answer', 'yes' if answer==1 else 'no')
    messagebox.showinfo('answer', answer)

button_6 = tk.Button(Main_Window, text="ask yes or no", command=question)
button_6.grid(row=0, column=1, ipadx=50)

# canvas
canvas = tk.Canvas(Main_Window, width=400, height=400, bg='yellow')
# canvas.create_line(10, 180, 100, 10, 190, 180, 10, 180,
# arrow=tk.BOTH, fill='red', smooth=True, width=3) # draw triangle
canvas.create_arc(10,100, 380, 300, outline='red', width=5)
canvas.create_arc(10, 100, 380, 300, outline='blue', fill='white',
start=90, style=tk.CHORD, width=5)
canvas.create_arc(10, 100, 380, 300, outline='green', width=5,
style=tk.ARC, start=180, extent=180)
canvas.grid(row=1, column=1)

Main_Window.mainloop()
