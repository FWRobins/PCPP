# You need a calculator. A very simple and very specific calculator.
# Look at the picture - it contains two fields that the user can use
# to enter arguments, a radio button to select the operation to perform,
# and a button initiating the evaluation
import tkinter as tk
from tkinter import messagebox

calc_string = ""
evals = ['+', '-', '*', '/']

def Close_window(event=None):
    reply = messagebox.askquestion("Quit?", "Are you sure?")
    if reply == 'yes':
        Main_Window.destroy()

def update_calc_label(string):
    global label_calc_2
    label_calc_2["text"] = string
    global label_ans_2
    label_ans_2["text"] = ""


def add_value(event):
    global calc_string
    calc_string += event.widget.cget("text")
    print(calc_string)
    update_calc_label(calc_string)

def clear():
    global calc_string
    calc_string = ""
    update_calc_label(calc_string)

def evaluate():
    global calc_string
    if len(calc_string) == 0:
        calc_string = "0"
    if calc_string[0] in evals:
        calc_string = calc_string[1:]
    if calc_string[-1] in evals:
        calc_string = calc_string[:-1]
    global label_ans_2
    try:
        label_ans_2["text"]=eval(calc_string)
    except ZeroDivisionError:
        messagebox.showinfo("Cannot Calculate", "Cannot divide by Zero")
        clear()



Main_Window = tk.Tk()
Main_Window.title("Calculator")
Main_Window.protocol("WM_DELETE_WINDOW", Close_window)

label_calc_1 = tk.Label(Main_Window, text="Calculate:")
label_calc_1.grid(row=0, column=0, columnspan=2)

label_calc_2 = tk.Label(Main_Window, text="")
label_calc_2.grid(row=0, column=2, columnspan=2)

label_ans_1 = tk.Label(Main_Window, text="Answer: ")
label_ans_1.grid(row=1, column=0, columnspan=2)

label_ans_2 = tk.Label(Main_Window, text="")
label_ans_2.grid(row=1, column=2, columnspan=2)

button_1 = tk.Button(Main_Window, text="1", width=5)
button_1.bind("<Button-1>", add_value)
button_1.grid(row=2, column=0)

button_2 = tk.Button(Main_Window, text="2", width=5)
button_2.bind("<Button-1>", add_value)
button_2.grid(row=2, column=1)

button_3 = tk.Button(Main_Window, text="3", width=5)
button_3.bind("<Button-1>", add_value)
button_3.grid(row=2, column=2)

button_add = tk.Button(Main_Window, text="+", width=5)
button_add.bind("<Button-1>", add_value)
button_add.grid(row=2, column=3)

button_4 = tk.Button(Main_Window, text="4", width=5)
button_4.bind("<Button-1>", add_value)
button_4.grid(row=3, column=0)

button_5 = tk.Button(Main_Window, text="5", width=5)
button_5.bind("<Button-1>", add_value)
button_5.grid(row=3, column=1)

button_6 = tk.Button(Main_Window, text="6", width=5)
button_6.bind("<Button-1>", add_value)
button_6.grid(row=3, column=2)

button_sub = tk.Button(Main_Window, text="-", width=5)
button_sub.bind("<Button-1>", add_value)
button_sub.grid(row=3, column=3)

button_7 = tk.Button(Main_Window, text="7", width=5)
button_7.bind("<Button-1>", add_value)
button_7.grid(row=4, column=0)

button_8 = tk.Button(Main_Window, text="8", width=5)
button_8.bind("<Button-1>", add_value)
button_8.grid(row=4, column=1)

button_9 = tk.Button(Main_Window, text="9", width=5)
button_9.bind("<Button-1>", add_value)
button_9.grid(row=4, column=2)

button_mul = tk.Button(Main_Window, text="*", width=5)
button_mul.bind("<Button-1>", add_value)
button_mul.grid(row=4, column=3)

button_clr = tk.Button(Main_Window, text="clr", command=clear, width=5)
button_clr.grid(row=5, column=0)

button_0 = tk.Button(Main_Window, text="0", width=5)
button_0.bind("<Button-1>", add_value)
button_0.grid(row=5, column=1)

button_equ = tk.Button(Main_Window, text="=", command=evaluate, width=5)
button_equ.grid(row=5, column=2)

button_div = tk.Button(Main_Window, text="/", width=5)
button_div.bind("<Button-1>", add_value)
button_div.grid(row=5, column=3)

Main_Window.mainloop()
