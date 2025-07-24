from PIL import Image, ImageTk
import random
import tkinter as tk
import os

# Change working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def load_images():
    """Loads and resizes images for rock, paper, and scissors."""
    images = {
        1: Image.open('rock.png'),      # Replace with actual file paths
        2: Image.open('paper.png'),
        3: Image.open('scissors.png')
    }
    # Resize images to a manageable size (200x200 pixels)
    for key in images:
        images[key] = ImageTk.PhotoImage(images[key].resize((200, 200), Image.LANCZOS))
    return images

# Initialize choices to store each player's choice
Choice1 = None
Choice2 = None
player1_image_on_canvas = None  # Placeholder to store Player 1's image reference on canvas
player2_image_on_canvas = None  # Placeholder to store Player 2's image reference on canvas
text_on_canvas = []  # To store text IDs and clear them later

def clear_text():
    """Clears previous text from the canvas."""
    global text_on_canvas
    for text_id in text_on_canvas:
        canvas.delete(text_id)
    text_on_canvas = []

def player1_turn():
    """Handles Player 1's turn and updates the image based on the choice."""
    global Choice1, player1_image_on_canvas
    Choice1 = random.randint(1, 3)
    
    # Update the console with Player 1's choice
    print('Player 1 chose', game[Choice1]) 

    # Update the canvas to show Player 1's choice image
    if player1_image_on_canvas:
        canvas.delete(player1_image_on_canvas)  # Remove the previous image
    player1_image_on_canvas = canvas.create_image(400, 325, anchor='center', image=images[Choice1])  # Left side for Player 1

    # Clear previous text and update text for Player 1's choice
    clear_text()
    text_on_canvas.append(canvas.create_text(400, 550, anchor='center', text=f"Player 1 chose {game[Choice1]}", fill='black', font='Helvetica 20 bold'))

    # Switch the button to Player 2's turn
    generate_button.config(text="Player 2's Turn", command=player2_turn)

def player2_turn():
    """Handles Player 2's turn, updates the image, and determines the winner."""
    global Choice2, player2_image_on_canvas
    Choice2 = random.randint(1, 3)
    
    # Update the console with Player 2's choice
    print('Player 2 chose', game[Choice2])  

    # Update the canvas to show Player 2's choice image
    if player2_image_on_canvas:
        canvas.delete(player2_image_on_canvas)  # Remove the previous image
    player2_image_on_canvas = canvas.create_image(1200, 325, anchor='center', image=images[Choice2])  # Right side for Player 2

    # Clear previous text and update text for Player 2's choice
    clear_text()
    text_on_canvas.append(canvas.create_text(1200, 550, anchor='center', text=f"Player 2 chose {game[Choice2]}", fill='black', font='Helvetica 20 bold'))

    # Determine and display the winner
    if Choice1 == Choice2:
        result = "It's a draw!"
    elif (Choice1 == 1 and Choice2 == 3) or (Choice1 == 2 and Choice2 == 1) or (Choice1 == 3 and Choice2 == 2):
        result = 'Player 1 wins!'
    else:
        result = 'Player 2 wins!'
    
    text_on_canvas.append(canvas.create_text(800, 700, anchor='center', text=result, fill='red', font='Helvetica 40 bold'))

    # Reset the button to Player 1's turn for the next round
    generate_button.config(text="Player 1's Turn", command=player1_turn)

# Set up the main window
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("1080x1920")

# Load images after the main window has been created
images = load_images()
game = {1: 'rock', 2: 'paper', 3: 'scissors'}

# Frame for the main game screen
frame2 = tk.Frame(window, bg="light slate blue")
frame2.grid(row=0, column=0, sticky="nsew")

# Main game screen contents
canvas = tk.Canvas(frame2, bg='light slate blue', width=1920, height=1080)
canvas.pack()

# Display the main game title
canvas.create_text(850, 50, text='Rock Paper Scissors game', fill="black", font='Helvetica 50 bold')

# Place static "Player 1" and "Player 2" labels below their respective image slots
canvas.create_text(400, 600, text="Player 1", fill="black", font='Helvetica 20 bold')
canvas.create_text(1200, 600, text="Player 2", fill="black", font='Helvetica 20 bold')

# Create a 'Generate' button to start the game
generate_button = tk.Button(frame2, text="Player 1's Turn", font='Helvetica 20', command=player1_turn)
canvas.create_window(800, 725, window=generate_button)

# Show the main game screen initially
frame2.tkraise()
window.mainloop()
