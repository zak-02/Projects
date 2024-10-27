import random
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import os

# Change working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def Roll1():
    input('Player 1, press the enter key to roll for either rock, paper or scissors: ')

def Roll2():
    input('Player 2, press the enter key to roll for either rock, paper or scissors: ')

def GUI():
    window = tk.Tk()  # Initialize the main Tk window
    canvas= tk.Canvas(window, width= 750, height= 540)
    canvas.pack()
    photo = tk.PhotoImage(file='rock.png')
    canvas.create_image(150,250,anchor=NW,image=photo,width=150, height=200)
    canvas.create_text(300, 50, text='Rock Paper Scissors game', fill="black", font=('Helvetica 15 bold'))

    
    
    window.mainloop()

def rps():
    GUI()
    game = {1: 'rock', 2: 'paper', 3: 'scissors'}
    Roll1()
    Choice1 = random.randint(1, 3)
    Roll2()
    Choice2 = random.randint(1, 3)

    print('Player 1 chose', game[Choice1])
    print('Player 2 chose', game[Choice2])

    if (Choice1 == game[1] and Choice2 == game[3]):
        print('Player 1 wins!')
    elif (Choice1 == game[3] and Choice2 == game[1]):
        print('Player 2 wins!')
    elif (Choice1 == game[2] and Choice2 == game[3]):
        print('Player 1 wins!')
    elif (Choice1 == game[3] and Choice2 == game[2]):
        print('Player 2 wins!')
    elif (Choice1 == Choice2):
        print("It's a draw!")
    elif (Choice1 > Choice2):
        print('Player 1 wins!')
    else:
        print('Player 2 wins!')

rps()
