import random
import tkinter as tk
import os

# Change working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def Roll1():
    input('Player 1, press the enter key to roll for either rock, paper, or scissors: ')

def Roll2():
    input('Player 2, press the enter key to roll for either rock, paper, or scissors: ')

def GUI():
    window = tk.Tk()  # Initialize the main Tk window
    canvas = tk.Canvas(window, bg='light slate blue', width=1920, height=1080)
    canvas.pack()

    # Create an image placeholder
    window.photo = tk.PhotoImage(file='question.png')  # Keep a reference to the image
    canvas.create_image(900, 325, anchor=tk.CENTER, image=window.photo)

    # Add main game title
    canvas.create_text(850, 50, text='Rock Paper Scissors game', fill="black", font='Helvetica 50 bold')

    # Add Player 1's turn text
    canvas.create_text(900, 600, text="Player 1's turn", fill='black', font='Helvetica 35 bold')

    # Create a 'Generate' button
    generate_button = tk.Button(window, text='Generate', font='Helvetica 20', command=rps)
    canvas.create_window(900, 700, window=generate_button)

    window.mainloop()

def rps():
    game = {1: 'rock', 2: 'paper', 3: 'scissors'}
    Roll1()
    Choice1 = random.randint(1, 3)
    Roll2()
    Choice2 = random.randint(1, 3)

    print('Player 1 chose', game[Choice1])
    print('Player 2 chose', game[Choice2])

    # Determine the winner
    if Choice1 == Choice2:
        print("It's a draw!")
    elif (Choice1 == 1 and Choice2 == 3) or (Choice1 == 2 and Choice2 == 1) or (Choice1 == 3 and Choice2 == 2):
        print('Player 1 wins!')
    else:
        print('Player 2 wins!')


GUI()
