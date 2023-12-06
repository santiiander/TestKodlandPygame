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
background= pygame.image.load("background.png").convert()


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
        self.rect.x=mouse_pos[0]
        self.rect.y=510


class Game(object):
    def __init__(self):
        self.score=0

        self.lista_sprites=pygame.sprite.Group() 
        self.lista_meteoros=pygame.sprite.Group()
        self.lista_lasers=pygame.sprite.Group()

        for i in range (50):
            meteor = Meteor()
            meteor.rect.x=random.randrange(880)
            meteor.rect.y=random.randrange(250)

        lista_meteoros.add(meteor)
        lista_sprites.add(meteor)


    def process_events(self):
        pass
    def run_logic():
        pass
    def display_frame(self):
        pass

def main():
    pass

if __name__=="finalv2":
    pass


