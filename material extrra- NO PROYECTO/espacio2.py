import pygame
import sys
import random
BLACK= (0,0,0)
WHITE= (255,255,255)
pygame.init()
screen=pygame.display.set_mode([900,600])
clock=pygame.time.Clock()
done= False
score=0

lista_sprites=pygame.sprite.Group() 

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("laser.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y-=5

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("player.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        mouse_pos=pygame.mouse.get_pos()
        player.rect.x=mouse_pos[0]
        player.rect.y=510
        

player = Player()
lista_sprites.add(player)
lista_meteoros=pygame.sprite.Group()
lista_lasers=pygame.sprite.Group()

for i in range (50):
    meteor = Meteor()
    meteor.rect.x=random.randrange(880)
    meteor.rect.y=random.randrange(250)

    lista_meteoros.add(meteor)
    lista_sprites.add(meteor)



while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True;

        if event.type==pygame.MOUSEBUTTONDOWN:
            laser= Laser()
            laser.rect.x=player.rect.x+45
            laser.rect.y=player.rect.y-20
             
            lista_sprites.add(laser)
            lista_lasers.add(laser)


    lista_sprites.update()

    for laser in lista_lasers:
        lista_hit_meteoros=pygame.sprite.spritecollide(laser,lista_meteoros,True)
        for meteor in lista_hit_meteoros:
            lista_sprites.remove(laser)
            lista_lasers.remove(laser)
            if laser.rect.y <-10:
                lista_sprites.remove(laser)
                lista_lasers.remove(laser)

        
    
    screen.fill(WHITE)
    lista_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()    