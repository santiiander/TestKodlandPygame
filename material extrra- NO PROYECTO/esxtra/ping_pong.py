import pygame
import sys
pygame.init

#Colores
black=(0, 0, 0)
white =(255, 255, 255)
size = (800,600)


#Constantes

player_width=15
player_height=90


#Coordenadas y velocidad de jugador 1
player1_x_coor=50
player1_y_coor=300 - 45
player1_y_speed=0

#Coordenadas y velocidad de jugador 2
player2_x_coor=750-player_width
player2_y_coor=300 - 45
player2_y_speed=0

#Coordenadas de la pelota
pelotax=400
pelotay=300
pelotaspeedx=3
pelotaspeedy=3


screen=pygame.display.set_mode(size)
clock= pygame.time.Clock();

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            #Jugador1
            if event.key == pygame.K_w:
                player1_y_speed = -3
            if event.key == pygame.K_s:
                player1_y_speed = 3    
            #Jugador2
            if event.key == pygame.K_UP:
                player2_y_speed = -3
            if event.key == pygame.K_DOWN:
                player2_y_speed = 3


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0   
            #Jugador2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0

    player1_y_coor+=player1_y_speed
    player2_y_coor+=player2_y_speed


    #Movimiento pelota

    if pelotay>590 or pelotay<10:
        pelotaspeedy*= -1

    #Revisamos si la pelota sale por lado derecho
    if pelotax>800:
        pelotax=400
        pelotay=300

        pelotaspeedx*=-1
        pelotaspeedy*=-1
        
    if pelotax<0:
        pelotax=400
        pelotay=300

        pelotaspeedx*=-1
        pelotaspeedy*=-1
    

        

    pelotax+=pelotaspeedx
    pelotay+=pelotaspeedy

    screen.fill(black)
    #Zona de dibujo
    Jugador1=pygame.draw.rect(screen,white,(player1_x_coor,player1_y_coor,player_width,player_height))
    Jugador2=pygame.draw.rect(screen,white,(player2_x_coor,player2_y_coor,player_width,player_height))
    Pelota=pygame.draw.circle(screen,white,(pelotax,pelotay),10)



    #Colisiones

    if Pelota.colliderect(Jugador1) or Pelota.colliderect(Jugador2):
        pelotaspeedx*=-1

    pygame.display.flip()
    clock.tick(60)


pygame.QUIT()
          