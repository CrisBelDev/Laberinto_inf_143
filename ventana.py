import pygame
import sys

# Inicializar pygame
pygame.init()

# Tamaño de la ventana del juego
WIDTH = 640
HEIGHT = 480

# Definir colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Definir el tamaño de los bloques y el laberinto
BLOCK_SIZE = 40
MAZE_WIDTH =10# WIDTH // BLOCK_SIZE
MAZE_HEIGHT = 10#HEIGHT // BLOCK_SIZE

# Definir el laberinto
maze = [
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Inicializar la posición del jugador
player_pos = [1, 1]

# Crear la ventana del juego
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Laberinto")

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Movimiento del jugador
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and maze[player_pos[1] - 1][player_pos[0]] == 0:
                player_pos[1] -= 1
            elif event.key == pygame.K_DOWN and maze[player_pos[1] + 1][player_pos[0]] == 0:
                player_pos[1] += 1
            elif event.key == pygame.K_LEFT and maze[player_pos[1]][player_pos[0] - 1] == 0:
                player_pos[0] -= 1
            elif event.key == pygame.K_RIGHT and maze[player_pos[1]][player_pos[0] + 1] == 0:
                player_pos[0] += 1

    # Dibujar el laberinto en la ventana
    screen.fill(WHITE)
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, BLUE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # Dibujar al jugador en la ventana
    pygame.draw.rect(screen, (255, 0, 0), (player_pos[0] * BLOCK_SIZE, player_pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # Actualizar la ventana
    pygame.display.flip()
