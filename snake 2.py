import pygame
import random
import time

#initializing pygame
pygame.init()

#defining the colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
orange=(255,165,0)

#display
width , height = 600, 400

game_display=pygame.display.set_mode((width,height))
pygame.display.set_caption("SNAKE GAME")

clock=pygame.time.Clock()

#snake
snakesize=10
snakespeed=15

messagefont=pygame.font.SysFont('ActionIsShaded', 30)
scorefont=pygame.font.SysFont('ActionIsShaded', 25)
#main function
def print_score(score):
    text=scorefont.render("score: "+ str(score), True, orange)
    game_display.blit(text,[0,0])
def draw_snake(snake_size,snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display , white, [pixel[0] , pixel[1] , snake_size , snake_size])
def gameover(snake_length):
    game_display.fill(black)
    gameover_message = messagefont.render("GAME OVER !! ", True, red)
    game_display.blit(gameover_message, [width / 3, height / 3])
    print_score(snake_length - 1)
def run_game():
    gameover=False
    gameclose=False

    x=width/2
    y=height/2

    x_speed= 0
    y_speed= 0

    snake_pixels=[(x,y)]
    snake_length=1

    target_x=round(random.randrange(0,width-snakesize)/10.0)*10
    target_y = round(random.randrange(0, height-snakesize) / 10.0) * 10

    #game loop
    while not gameclose:
        game_display.fill(black)
        gameover_message=messagefont.render("GAME OVER !! ", True , red)
        game_display.blit(gameover_message,[width/ 3 , height/ 3])
        print_score(snake_length -1)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.k_1:
                    gameover=True
                    gameclose= False
                if event.key==pygame.k_2:
                    run_game()
            if event.type==pygame.QUIT:
                gameover = True
                gameclose = False


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameover=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_speed= -snakesize
                y_speed= 0
            if event.key==pygame.K_RIGHT:
                x_speed= snakesize
                y_speed= 0
            if event.key==pygame.K_UP:
                x_speed= -snakesize
                y_speed= 0
            if event.key==pygame.K_DOWN:
                x_speed= 0
                y_speed= snakesize
    if x>=width or x<0 or y>-height or y<0:
            gameclose=True
    x+=x_speed
    y+=y_speed

    game_display.fill(black)
    pygame.draw.rect(game_display, orange, [target_x,target_y,snakesize,snakesize])

    snake_pixels.append((x,y))

    if len(snake_pixels)>snake_length:
        del snake_pixels[0]
    for pixel in snake_pixels[:-1]:
         if pixel ==[x,y]:
             gameclose= True
    draw_snake(snakesize,snake_pixels)
    print_score(snake_length -1)
    pygame.display.update()

    if x==target_x and y==target_y:
        target_x = round(random.randrange(0, width - snakesize) / 10.0) * 10
        target_y = round(random.randrange(0, height - snakesize) / 10.0) * 10
        snake_length+=1
    clock.tick(snakespeed)
    pygame.quit()
    quit()
run_game()