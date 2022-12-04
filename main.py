import pygame
from random import randint
from copy import deepcopy

res = weight, height = 1600, 900
pers = 50
w, h = weight // pers, height // pers
fps = 10
pygame.init()
pygame.display.set_caption("life")
screen = pygame.display.set_mode(res)
black = (0, 0, 0)
clock = pygame.time.Clock()

next_mas = [[0 for i in range(w)] for j in range(h)]
current_mas = [[randint(0, 1) for i in range(w)] for j in range(h)]


def check(current_mas, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_mas[j][i]:
                count += 1
    if current_mas[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0


while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    [pygame.draw.line(screen, pygame.Color("dimgray"), (x, 0), (x, height)) for x in range(0, weight, pers)]
    [pygame.draw.line(screen, pygame.Color("dimgray"), (0, y), (weight, y)) for y in range(0, height, pers)]
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            if current_mas[y][x]:
                pygame.draw.rect(screen, pygame.Color("green"), (x * pers + 2, y * h + 2, pers - 2, pers - 2))
            next_mas[y][x] = check(current_mas, x, y)
    current_mas = deepcopy(next_mas)


    pygame.display.flip()
    clock.tick(fps)
