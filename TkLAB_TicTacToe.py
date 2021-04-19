"""
Write a simple GUI program which pretends to play tic-tac-toe with the user.

Here are our assumptions:.

the computer (i.e., your program) plays 'X', and Xes are always red,
the user (e.g., you) plays 'O', and Os are always green,
the board consists of 9 tiles, and the tile role is played by a button,
the first move belongs to the computer - it always puts its first 'X' in the
middle of the board,
the user enters her/his move by clicking the chosen tile (clicking the tiles
which are not free is ineffective)
the program checks if the game over conditions are met, and if the game is over,
a message box is displayed announcing the winner,
otherwise the computer responds with its move and the check is repeated,
use random to generate the computer's moves.

"""
PLAYING = True

import tkinter as tk
from tkinter import messagebox
from random import randrange

PLAYCOUNT = 0

def click(event=None):
    global PLAYCOUNT
    if event.widget.cget('text') == '':
        event.widget.config(text="O", fg='green')
        print(event.widget.id)
        PLAYCOUNT +=1
        check_victory('O')
        if PLAYCOUNT >= 9:
            messagebox.showinfo("Done", 'tie')
            stop_playing()
        comp_play()
    else:
        messagebox.showinfo("warning", "block already chosen")

def comp_play():
    global PLAYCOUNT
    move = randrange(0,9)
    print(buttons[f'button{move}'].cget('text'))
    if buttons[f'button{move}'].cget('text') == '':
        buttons[f'button{move}'].config(text='X')
        PLAYCOUNT +=1
        check_victory('X')
        if PLAYCOUNT >= 9:
            messagebox.showinfo("Done", 'tie')
            stop_playing()
    else:
        comp_play()

def stop_playing():
    global PLAYCOUNT
    print(buttons)
    for button in buttons:
        print(button)
        buttons[button].config(text="")
        PLAYCOUNT = 0

def check_victory(player):
    if buttons[f"button{0}"].cget("text")== buttons[f"button{1}"].cget("text")== buttons[f"button{2}"].cget("text") == player:
        messagebox.showinfo("Done", player + 'wins')
        stop_playing()
    if buttons[f"button{3}"].cget("text")== buttons[f"button{4}"].cget("text")== buttons[f"button{5}"].cget("text") == player:
        messagebox.showinfo("Done", player + 'wins')
        stop_playing()
    if buttons[f"button{6}"].cget("text")== buttons[f"button{7}"].cget("text")== buttons[f"button{8}"].cget("text") == player:
        messagebox.showinfo("Done", player + 'wins')
        stop_playing()
    if buttons[f"button{0}"].cget("text")== buttons[f"button{3}"].cget("text")== buttons[f"button{6}"].cget("text") == player:
        messagebox.showinfo("Done", player + 'wins')
        stop_playing()
    if buttons[f"button{1}"].cget("text")== buttons[f"button{4}"].cget("text")== buttons[f"button{7}"].cget("text") == player:
        messagebox.showinfo("Done", player + 'wins')
        stop_playing()
    if buttons[f"button{2}"].cget("text")== buttons[f"button{5}"].cget("text")== buttons[f"button{8}"].cget("text") == player:
        messagebox.showinfo("Done", player + 'wins')
        stop_playing()
    if buttons[f"button{0}"].cget("text")== buttons[f"button{4}"].cget("text")== buttons[f"button{8}"].cget("text") == player:
        messagebox.showinfo("Done", player + 'wins')
        stop_playing()
    if buttons[f"button{2}"].cget("text")== buttons[f"button{4}"].cget("text")== buttons[f"button{6}"].cget("text") == player:
        messagebox.showinfo("Done", player + 'wins')
        stop_playing()


Main_Window = tk.Tk()

Main_Window.title("Tic-Tac-Toe")

buttons ={}
for block in range(9):
    if block == 4:
        button = tk.Button(Main_Window, text = 'X',
        width=10, height=5, font=("Arial", "16", "bold"),
        relief='ridge')
        button.id = block
        button.grid(row=block//3, column=block%3)
        button.bind("<Button-1>", click)
        print(button.id)
        buttons[f'button{block}'] = button
        PLAYCOUNT += 1
    else:
        button = tk.Button(Main_Window, text = '',
        width=10, height=5, font=("Arial", "16", "bold"),
        relief='ridge')
        button.id = block
        button.grid(row=block//3, column=block%3)
        button.bind("<Button-1>", click)
        buttons[f'button{block}'] = button


Main_Window.mainloop()
