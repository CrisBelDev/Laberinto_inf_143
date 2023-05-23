import pygame
import sys

class Laberinto:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.ancho = len(laberinto[0])
        self.alto = len(laberinto)
        self.tamano_bloque = 50
        self.ancho_ventana = self.ancho * self.tamano_bloque
        self.alto_ventana = self.alto * self.tamano_bloque
        self.posicion_jugador_x = 0
        self.posicion_jugador_y = 0

        pygame.init()
        self.pantalla = pygame.display.set_mode((self.ancho_ventana, self.alto_ventana))

    def dibujar_laberinto(self):
        for y in range(self.alto):
            for x in range(self.ancho):
                if self.laberinto[y][x] == 1:
                    pygame.draw.rect(self.pantalla, (0, 0, 0), (x * self.tamano_bloque, y * self.tamano_bloque, self.tamano_bloque, self.tamano_bloque))
                else:
                    pygame.draw.rect(self.pantalla, (255, 255, 255), (x * self.tamano_bloque, y * self.tamano_bloque, self.tamano_bloque, self.tamano_bloque))

    def dibujar_jugador(self):
        pygame.draw.rect(self.pantalla, (255, 0, 0), (self.posicion_jugador_x * self.tamano_bloque, self.posicion_jugador_y * self.tamano_bloque, self.tamano_bloque, self.tamano_bloque))

    def mover_jugador(self, dx, dy):
        nueva_posicion_x = self.posicion_jugador_x + dx
        nueva_posicion_y = self.posicion_jugador_y + dy
        if 0 <= nueva_posicion_x < self.ancho and 0 <= nueva_posicion_y < self.alto and self.laberinto[nueva_posicion_y][nueva_posicion_x] == 0:
            self.posicion_jugador_x = nueva_posicion_x
            self.posicion_jugador_y = nueva_posicion_y

    def ejecutar_juego(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        self.mover_jugador(0, -1)
                    elif evento.key == pygame.K_DOWN:
                        self.mover_jugador(0, 1)
                    elif evento.key == pygame.K_LEFT:
                        self.mover_jugador(-1, 0)
                    elif evento.key == pygame.K_RIGHT:
                        self.mover_jugador(1, 0)

            self.pantalla.fill((0, 0, 0))
            self.dibujar_laberinto()
            self.dibujar_jugador()
            pygame.display.update()


# Ejemplo de uso
laberinto = [
    [0, 1, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

juego = Laberinto(laberinto)
juego.ejecutar_juego()
