import pygame
import sys
pygame.init();

size = (800,500)

#Definir colores
BLACK					=			(  0,   0,   0)
DARK_BLUE				=			(  0,   0, 100)
BLUE					=			(  0,   0, 255)
DARK_GREEN			=			(  0, 100,   0)
GREENISH_BLUE			=			(  0, 100, 100)
LIGHT_TURQUOISE		=			(  0, 100, 255)
GREEN					=			(  0, 255,   0)
WATERY_GREEN			=			(  0, 255, 100)
CYAN					=			(  0, 255, 255)


#Crear ventana

screen=pygame.display.set_mode(size)
coord_x=400
coord_y=200

#Velodidad cuadrado movimiento
speed_x=3
speed_y=3

clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit();
    
    coord_x+=speed_x
    coord_y+=speed_y

    if coord_x>720 or coord_x<0:
        speed_x*=-1

    if coord_y>420 or coord_y<0:
        speed_y*=-1


    
    #Ponemos color de fondo
    screen.fill(LIGHT_TURQUOISE)

    #ZONA DE DIBUJO

    pygame.draw.rect(screen,BLUE,(coord_x,coord_y,80,80))

    #Con este metodo actualizamos pantalla
    #Todos los cambios deben estar realizados por encima
    #de esta linea
    pygame.display.flip()
    clock.tick(60)
