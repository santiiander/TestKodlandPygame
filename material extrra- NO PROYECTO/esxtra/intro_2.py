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

coor_list=[]

for i in range (60):
        x= random.randint(0,800)
        y =random.randint(0,600)
        coor_list.append([x,y])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(WHITE) 
    for coord in coor_list:
         pygame.draw.circle(screen,RED,(coord),2)
         coord[1]+=1
         if coord[1]>600:
              coord[1]=0
    
    pygame.display.flip()
    clock.tick(30)
