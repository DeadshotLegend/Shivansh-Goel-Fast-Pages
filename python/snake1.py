import pygame
import sys
import random

# board size
height=400
width=300

#snake size
snake_size=10
#mouse size
mouse_size=10

# this should be configured in user's profile
gamespeed=3
""" user should be able to select High | Medium | Low speeds """

# create basic colors
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
brown=(123,63,0)

def gameLost(score):
    dis.fill(black)
    font = pygame.font.SysFont(None, 25)
    score_text = font.render("Score ("+str(score)+")", True, white)
    dis.blit(score_text, [0, 0])
    game_over_text = font.render("Game Over!", True, white)
    dis.blit(game_over_text, [width//2 - 50, height//2 - 25])
    pygame.display.update()
    pygame.time.wait(3000)
    sys.exit()
    
def gameClosed(score):
    dis.fill(black)
    font = pygame.font.SysFont(None, 25)
    score_text = font.render("Score ("+str(score)+")", True, white)
    dis.blit(score_text, [0, 0])
    game_over_text = font.render("See you soon!", True, white)
    dis.blit(game_over_text, [width//2 - 50, height//2 - 25])
    pygame.display.update()
    pygame.time.wait(3000)
    sys.exit()

def showScore(score):
    font = pygame.font.SysFont(None, 25)
    score_text = font.render("Score ("+str(score)+")", True, white)
    dis.blit(score_text, [0, 0])
    pygame.display.update()
#draw the snake's shape
def drawSnake(snake_shape):
    #print(snake_shape)
    for x in snake_shape:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_size, snake_size])
#initialize pygame
pygame.init()
# game board
dis=pygame.display.set_mode((width,height))
pygame.display.set_caption('Snake game by Shivansh Goel DNHS APCSP')

#initial snake position - centered for 
snake_x = width/2
snake_y = height/2

# initial mouse position
mouse_x = round(random.randrange(0, width - mouse_size) / 10.0) * 10.0
mouse_y = round(random.randrange(0, height - mouse_size) / 10.0) * 10.0

pygame.draw.rect(dis, black, [snake_x, snake_y, snake_size, snake_size])
pygame.display.update()
dis.fill(white)


# run the game until it is over
def main():
    x1_change = 0       
    y1_change = 0
    score=0

    #the clock
    clock = pygame.time.Clock()

    snake_shape = []
    snake_len = 1
    game_quit=False
    game_lost=False
    snake_x = width / 2
    snake_y = height / 2
    mouse_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    mouse_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
    
    # check when game is over
    while not game_lost:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
                gameClosed(score)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0
 
        if snake_x >= width or snake_x < 0 or snake_y >= height or snake_y < 0:
            game_lost = True
            gameLost(score)
            
        snake_x += x1_change
        snake_y += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, brown, [mouse_x, mouse_y, snake_size, snake_size])
        
        new_snake_pos = []
        new_snake_pos.append(snake_x)
        new_snake_pos.append(snake_y)
        snake_shape.append(new_snake_pos)
        
        if len(snake_shape) > snake_len:
            # delete the tail
            del snake_shape[0]
 
        # if the snake eats its own body, then game is over
        for x in snake_shape[:-1]:
            if x == new_snake_pos:
                game_lost = True
                gameLost(score)
 
        drawSnake(snake_shape)
        showScore(score)
        pygame.display.update()
 
        if snake_x == mouse_x and snake_y == mouse_y:
            score+=1
            mouse_x = round(random.randrange(0, width - mouse_size) / 10.0) * 10.0
            mouse_y = round(random.randrange(0, height - mouse_size) / 10.0) * 10.0
            snake_len += 1
 
        clock.tick(gamespeed)
 
    pygame.quit()
    quit()

main()

