import pygame
import sys
import random

pygame.init

size=(800,600)

#Definir colores

RED=(255, 0, 0)
WHITE=(255, 255, 255)

screen=pygame.display.set_mode(size)
clock=pygame.time.Clock()
pygame.mouse.set_visible(0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    mouse_pos=pygame.mouse.get_pos()
    print(mouse_pos)
    x= mouse_pos[0]
    y= mouse_pos[1]
    screen.fill(WHITE)

    pygame.draw.rect(screen,RED,(x,y,100,100))         


    pygame.display.flip()        