import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Esquiva Obstáculos")

# Definir el jugador
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
player_speed = 10

# Definir los obstáculos
obstacle_size = 50
obstacle_speed = 5
obstacle_frequency = 25
obstacles = []

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Función para dibujar al jugador en la pantalla
def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, player_size, player_size])

# Función para dibujar obstáculos en la pantalla
def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, WHITE, obstacle)

# Función principal del juego
def game():
    global player_x, player_y, obstacles

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player_x -= (keys[pygame.K_LEFT] - keys[pygame.K_RIGHT]) * player_speed
        player_x = max(0, min(WIDTH - player_size, player_x))

        screen.fill(BLACK)

        # Generar obstáculos aleatorios
        if random.randint(1, obstacle_frequency) == 1:
            obstacle_x = random.randint(0, WIDTH - obstacle_size)
            obstacle_y = 0
            obstacles.append([obstacle_x, obstacle_y, obstacle_size, obstacle_size])

        # Mover y dibujar obstáculos
        for obstacle in obstacles:
            obstacle[1] += obstacle_speed
            if obstacle[1] > HEIGHT:
                obstacles.remove(obstacle)

        # Verificar colisiones
        for obstacle in obstacles:
            if (
                player_x < obstacle[0] < player_x + player_size
                or player_x < obstacle[0] + obstacle[2] < player_x + player_size
            ) and (
                player_y < obstacle[1] + obstacle[3] < player_y + player_size
            ):
                print("¡Has perdido!")
                pygame.quit()
                sys.exit()

        draw_player(player_x, player_y)
        draw_obstacles(obstacles)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    game()