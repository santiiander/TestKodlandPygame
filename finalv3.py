import pygame
import sys
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()
pygame.mouse.set_visible(False)


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 50)
        self.option = 0

    def draw(self):
        text1 = self.font.render("Jugar", True, RED if self.option == 0 else WHITE)
        text2 = self.font.render("Salir", True, RED if self.option == 1 else WHITE)
        self.screen.blit(text1, (400, 200))
        self.screen.blit(text2, (400, 250))

    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if self.option == 0:
                    return "start"
                elif self.option == 1:
                    return "exit"
            elif event.key == pygame.K_UP:
                self.option = (self.option - 1) % 2
            elif event.key == pygame.K_DOWN:
                self.option = (self.option + 1) % 2
        return "menu"


class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("laser.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 5


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rotation_speed = random.uniform(-2, 2)  # Velocidad de rotación
        self.angle = 0  # Ángulo de rotación inicial

    def reset_position(self):
        self.rect.x = random.randrange(880)
        self.rect.y = random.randrange(250)

    def update(self):
        self.rotate()

    def rotate(self):
        self.angle = (self.angle + self.rotation_speed) % 360
        original_center = self.rect.center
        self.image = pygame.transform.rotate(pygame.image.load("meteor.png").convert_alpha(), self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = original_center


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0]
        self.rect.y = 510


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 0.6


class Game:
    def __init__(self):
        self.score = 0
        self.done = False
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([900, 600])
        self.background = pygame.image.load("background.png").convert()
        self.all_sprites = pygame.sprite.Group()
        self.meteor_list = pygame.sprite.Group()
        self.laser_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.menu = Menu(self.screen)
        self.font = pygame.font.Font(None, 50)

        self.player = Player()
        self.all_sprites.add(self.player)

        self.meteor_count = 25  # Inicializa con la cantidad de meteoritos
        self.initialize_meteors()

    def initialize_meteors(self):
        for _ in range(25):
            meteor = Meteor()
            meteor.reset_position()
            self.meteor_list.add(meteor)
            self.all_sprites.add(meteor)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True

            if event.type == pygame.MOUSEBUTTONDOWN:
                laser = Laser()
                laser.rect.x = self.player.rect.x + 45
                laser.rect.y = self.player.rect.y - 20

                self.all_sprites.add(laser)
                self.laser_list.add(laser)

        return False

    def run_logic(self):
        self.all_sprites.update()

        # Colisiones entre lasers y meteoritos
        for laser in self.laser_list:
            hit_meteors = pygame.sprite.spritecollide(laser, self.meteor_list, True)
            for meteor in hit_meteors:
                self.all_sprites.remove(laser)
                self.laser_list.remove(laser)
                if laser.rect.y < -10:
                    self.all_sprites.remove(laser)
                    self.laser_list.remove(laser)
                # Decrementa el contador de meteoritos
                self.meteor_count -= 1

        # Colisiones entre lasers y enemigos
        hit_enemies = pygame.sprite.groupcollide(self.enemy_list, self.laser_list, True, True)
        for enemy in hit_enemies:
            # Puedes realizar alguna acción aquí si es necesario
            pass

        # Generar nuevos enemigos
        if random.randrange(100) < 1:
            enemy = Enemy()
            enemy.rect.x = random.randrange(880)
            enemy.rect.y = -10
            self.enemy_list.add(enemy)
            self.all_sprites.add(enemy)

        # Colisiones entre jugador y enemigos
        hit_enemies = pygame.sprite.spritecollide(self.player, self.enemy_list, True)
        if hit_enemies:
            self.done = True

        # Verifica si todos los meteoritos han sido eliminados
        if self.meteor_count == 0:
            self.done = True

    def display_frame(self):
        self.screen.blit(self.background, [0, 0])
        self.all_sprites.draw(self.screen)

        if self.done:
            text = self.font.render("Fin del Juego", True, RED)
            self.screen.blit(text, (350, 250))

        pygame.display.flip()

    def main_loop(self):
        state = "menu"
        while not self.done:
            if state == "menu":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.done = True
                    state = self.menu.event_handler(event)
                self.menu.draw()
            elif state == "start":
                self.done = self.process_events()
                self.run_logic()
                self.display_frame()
                if self.done:
                    pygame.time.delay(3000)
                    pygame.quit()
                    return
            elif state == "exit":
                self.done = True
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        while True:
            self.display_frame()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    return


if __name__ == "__main__":
    game = Game()
    game.main_loop()