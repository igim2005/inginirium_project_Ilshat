import pygame
import time
import random

pygame.init()
purple = (186, 85, 211)
green = (0, 90, 0)
red = (255, 0, 0)
light_green = (0, 255, 0)
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка Ильшата')
clock = pygame.time.Clock()
snake_block = 20
speed = 5
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("calibry", 35)

def Your_score(score):
    value = score_font.render("Яблок съедено: " + str(score), True, purple)
    dis.blit(value, [300, 0])

def our_snake(snake_block, s_list):
    for x in s_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    m = font_style.render(msg, True, color)
    dis.blit(m, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    s_List = []
    s_Length = 1
    foodx = round(random.randrange(20, dis_width - 20 - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(20, dis_height - 20 - snake_block) / 20.0) * 20.0
    while not game_over:
        while game_close == True:
            message("Вы проиграли! Нажмите ESC для выхода или R для повторной игры", red)
            Your_score(s_Length - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(light_green)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        Head = []
        Head.append(x1)
        Head.append(y1)
        s_List.append(Head)
        if len(s_List) > s_Length:
            del s_List[0]
        for x in s_List[:-1]:
            if x == Head:
                game_close = True
        our_snake(snake_block, s_List)
        Your_score(s_Length - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            s_Length += 1
        clock.tick(speed)
    pygame.quit()
    quit()

gameLoop()