import pygame, random
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

#Tambien podemos hacer esto con screen=([800,600]) y usamos la posicion del vector 
WHITE = (255,255,255)
BLACK = (0,0,0)
class Meteor(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("meteor.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
	def update(self):
		self.rect.y += 1
		if self.rect.y > 600:
			self.rect.y = -10
			self.rect.x = random.randrange(900)
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("player.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
	def update(self):
		mouse_pos = pygame.mouse.get_pos()
		self.rect.x = mouse_pos[0]
		self.rect.y = mouse_pos[1]
class Game(object):
	def __init__(self):
		self.game_over = False
		self.score = 0
		self.meteor_list = pygame.sprite.Group()
		self.all_sprites_list = pygame.sprite.Group()
		for i in range(50):
			meteor = Meteor()
			meteor.rect.x = random.randrange(SCREEN_WIDTH)
			meteor.rect.y = random.randrange(SCREEN_HEIGHT)
			self.meteor_list.add(meteor)
			self.all_sprites_list.add(meteor)
		self.player = Player()
		self.all_sprites_list.add(self.player)
	def process_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
			if event.type == pygame.MOUSEBUTTONDOWN:
				if self.game_over:
					self.__init__()
		return False
	def run_logic(self):
		if not self.game_over:
			self.all_sprites_list.update()
			meteor_hit_list = pygame.sprite.spritecollide(self.player, self.meteor_list, True)
			for meteor in meteor_hit_list:
				self.score += 1
				print(self.score)
			if len(self.meteor_list) == 0:
				self.game_over = True
	def display_frame(self, screen):
		screen.fill(WHITE)
		if self.game_over:
			font = pygame.font.SysFont("serif", 25)
			text = font.render("Fin del juego!, Click para continuar.", True, BLACK)
			center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
			center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
			screen.blit(text, [center_x, center_y])
		if not self.game_over:
			self.all_sprites_list.draw(screen)
		self.all_sprites_list.draw(screen)
		pygame.display.flip()
def main():
	pygame.init()
	screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
	done = False
	clock = pygame.time.Clock()
	game = Game()
	while not done:
		done = game.process_events()
		game.run_logic()
		game.display_frame(screen)
		clock.tick(60)
	pygame.quit()
if __name__ == "__main__":
	main()