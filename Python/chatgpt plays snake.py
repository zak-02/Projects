# Importing libraries
import pygame
import time
import random
import openai
import os

# Snake speed
snake_speed = 10  # Reduced speed to handle API latency

# Window size
window_x = 720
window_y = 480

# Defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Initializing pygame
pygame.init()

# Game window
pygame.display.set_caption('ChatGPT Snakes')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS controller
fps = pygame.time.Clock()

# Snake's starting position
snake_position = [100, 50]

# First 4 blocks of the snake's body
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# Default snake direction
direction = 'RIGHT'
change_to = direction

# Initial score
score = 0

# ChatGPT API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to call ChatGPT for the next move with updated context after each fruit
def get_chatgpt_move(snake_position, snake_body, fruit_position, direction):
    grid_info = f"The snake body is at these positions: {snake_body}. The fruit is at position {fruit_position}. The snake is moving {direction}."
    prompt = f"""
    You are controlling a snake in a 2D game grid. You need to avoid obstacles like walls and the snake's body, and move towards the fruit to grow. The game grid is 720x480 pixels.
    {grid_info}
    Your job is to provide the next move direction for the snake to move towards the fruit without crashing into walls or itself.
    Possible directions are 'UP', 'DOWN', 'LEFT', 'RIGHT'. Provide only the direction, no additional explanation.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a snake controller in a 2D grid game."},
            {"role": "user", "content": prompt}
        ]
    )
    
    # Extract direction from response
    return response['choices'][0]['message']['content'].strip().upper()

# Function to check if a move is valid
def is_valid_move(new_position, snake_body, window_x, window_y):
    x, y = new_position
    # Check if the move is within the window bounds
    if x < 0 or x >= window_x or y < 0 or y >= window_y:
        return False
    # Check if the move collides with the snake's body
    if new_position in snake_body:
        return False
    return True

# Function to calculate the next position based on the direction
def get_next_position(snake_position, direction):
    if direction == 'UP':
        return [snake_position[0], snake_position[1] - 10]
    elif direction == 'DOWN':
        return [snake_position[0], snake_position[1] + 10]
    elif direction == 'LEFT':
        return [snake_position[0] - 10, snake_position[1]]
    elif direction == 'RIGHT':
        return [snake_position[0] + 10, snake_position[1]]
    return snake_position

# Function to display the score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

# Function for game over
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main game loop
while True:
    # Get ChatGPT's decision with the current context (including snake's position and fruit's position)
    suggested_direction = get_chatgpt_move(snake_position, snake_body, fruit_position, direction)

    # Calculate the next position based on the suggested direction
    next_position = get_next_position(snake_position, suggested_direction)

    # Validate the suggested direction (check for walls or body collision)
    if is_valid_move(next_position, snake_body, window_x, window_y):
        direction = suggested_direction  # Accept the move if valid
    else:
        # If the suggested direction is invalid, use the current direction
        next_position = get_next_position(snake_position, direction)
        if not is_valid_move(next_position, snake_body, window_x, window_y):
            # If the current direction is also invalid (snake trapped), game over
            game_over()

    # Move the snake
    snake_position = next_position

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False  # The fruit is eaten, so we need to spawn a new one
    else:
        snake_body.pop()

    if not fruit_spawn:
        # Spawn a new fruit in a random location
        fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
        fruit_spawn = True

    # Fill the game window with black background
    game_window.fill(black)

    # Draw the snake's body
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    
    # Draw the fruit
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Game over conditions: hit walls
    if snake_position[0] < 0 or snake_position[0] > window_x-10 or snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    # Game over conditions: snake bites itself
    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    # Display score
    show_score(1, white, 'times new roman', 20)

    # Refresh the game screen
    pygame.display.update()

    # Frame Per Second / Refresh Rate
    fps.tick(snake_speed)
