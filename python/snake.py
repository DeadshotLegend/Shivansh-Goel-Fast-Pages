import pygame
import sys
import random
import os

# Initialize game engine
pygame.init()

# Set screen width and height
width = 500
height = 500

# Set screen size
screen = pygame.display.set_mode((width, height))
pygame.display.update()

# Set title
pygame.display.set_caption("Snake Game")

# Set clock
clock = pygame.time.Clock()

# Define snake color
snake_color = (255, 0, 0)

# Define food color
food_color = (0, 255, 0)

# Set block size
block_size = 10

# Set font
font = pygame.font.SysFont(None, 25)

def display_score(score):
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, [0,0])

def draw_food(food_x, food_y):
    pygame.draw.rect(screen, food_color, [food_x, food_y, block_size, block_size])

def game_over():
    game_over_text = font.render("Game Over!", True, (255, 255, 255))
    screen.blit(game_over_text, [width//2 - 50, height//2 - 25])
    pygame.display.update()
    pygame.time.wait(3000)
    sys.exit()

def check_collision(snake_head, food_x, food_y):
    if snake_head[0] == food_x and snake_head[1] == food_y:
        return True
    return False

def check_boundary_collision(snake_head):
    if snake_head[0] >= width or snake_head[0] < 0 or snake_head[1] >= height or snake_head[1] < 0:
        return True
    return False

def check_self_collision(snake_head, snake_list):
    if snake_head in snake_list[1:]:
        return True
    return False

# Set initial position of snake and food
snake_x = 150
snake_y = 150
food_x = random.randint(0, width-block_size)
food_y = random.randint(0, height-block_size)

# Set initial velocity
velocity_x = 0
velocity_y = 0

# Set initial snake length
snake_length = 1

# Initialize snake list
snake_list = []

# Set initial score
score = 0

# Start game loop
gameover=False
while not gameover:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameover = True
            game_over()

        
        # Get key events
        #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_LEFT and velocity_x != block_size:
                #velocity_x = -block_size
                #velocity_y = 0
                #if event.key == pygame.K_RIGHT and velocity_x != -