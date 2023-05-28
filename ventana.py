import pygame

import sys

class Ventana:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.ancho = len(laberinto[0])
        self.alto = len(laberinto)
        self.tamano_bloque = 40
        self.ancho_ventana = self.ancho * self.tamano_bloque
        self.alto_ventana = self.alto * self.tamano_bloque+100
        self.posicion_jugador_x = 0
        self.posicion_jugador_y = 0
        # reloj fps
        self.clock = pygame.time.Clock()
        self.speed_x = 0
        self.speed_y = 0
        self.pasos = 0
        pygame.init()
        self.pantalla = pygame.display.set_mode((self.ancho_ventana, self.alto_ventana))


    def dibujar_laberinto(self):
        image = pygame.image.load("media/pared.jpg")
        imagen_redimensionada = pygame.transform.scale(image, (self.tamano_bloque, self.tamano_bloque))

        for y in range(self.alto):
            for x in range(self.ancho):
                if self.laberinto[y][x] == 1:
                    self.pantalla.blit(imagen_redimensionada, (x * self.tamano_bloque, y * self.tamano_bloque))

                    #pygame.draw.rect(self.pantalla, (0, 0, 0), (x * self.tamano_bloque , y * self.tamano_bloque, self.tamano_bloque, self.tamano_bloque))
                else:
                    
                    pygame.draw.rect(self.pantalla, (0, 0, 0), (x * self.tamano_bloque, y * self.tamano_bloque, self.tamano_bloque, self.tamano_bloque))
        self.colorear_meta()
    # funcion para colorear la meta
    def colorear_meta(self):
        for y in range(self.alto):
            for x in range(self.ancho):
                if self.laberinto[y][x] == 2:
                    pygame.draw.rect(self.pantalla, (0, 255, 0), (x * self.tamano_bloque, y * self.tamano_bloque, self.tamano_bloque, self.tamano_bloque))

    def dibujar_jugador(self):
        image = pygame.image.load("media/1.png")
        imagen_redimensionada = pygame.transform.scale(image, (self.tamano_bloque, self.tamano_bloque))
        self.pantalla.blit(imagen_redimensionada, ( self.posicion_jugador_x*self.tamano_bloque,  self.posicion_jugador_y*self.tamano_bloque))
        #pygame.draw.rect(self.pantalla, (255, 0, 0), (self.posicion_jugador_x * self.tamano_bloque, self.posicion_jugador_y * self.tamano_bloque, self.tamano_bloque, self.tamano_bloque))

    def mover_jugador(self, dx, dy):
        
        nueva_posicion_x = self.posicion_jugador_x + dx
        nueva_posicion_y = self.posicion_jugador_y + dy
        if 0 <= nueva_posicion_x < self.ancho and 0 <= nueva_posicion_y < self.alto and self.laberinto[nueva_posicion_y][nueva_posicion_x] in [0,2]:
            self.posicion_jugador_x = nueva_posicion_x
            self.posicion_jugador_y = nueva_posicion_y
            if not dy == 0:
                self.pasos += 1
            elif not dx == 0:
                self.pasos += 1
        print(self.pasos)
            

    def ejecutar_juego(self):
        reposo = False
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN: # al presionar
                    
                    
                    if evento.key == pygame.K_UP:
                        self.speed_y = -1 
                        #self.mover_jugador(0, -1)
                    elif evento.key == pygame.K_DOWN:
                        self.speed_y = 1 
                        #self.mover_jugador(0, 1)
                    elif evento.key == pygame.K_LEFT:
                        self.speed_x = -1
                        #self.mover_jugador(-1, 0)
                    elif evento.key == pygame.K_RIGHT:
                        self.speed_x = 1
                    
                        #self.mover_jugador(1, 0)
                if evento.type == pygame.KEYUP:      # dejo de presionar tecla
                    if evento.key == pygame.K_LEFT:
                        self.speed_x = 0
                    if evento.key == pygame.K_RIGHT:
                        self.speed_x = 0
                    # eje Y ----------------------
                    if evento.key == pygame.K_UP:
                        self.speed_y = 0
                    if evento.key == pygame.K_DOWN:
                        self.speed_y = 0
            
            self.mover_jugador(self.speed_x,self.speed_y)
            
            self.dibujar_laberinto()
            self.dibujar_jugador()
            # barra de informacion
            pygame.draw.rect(self.pantalla, (67, 92, 98, 1), (0 , self.alto * self.tamano_bloque, self.ancho_ventana, 100))

            fuente = pygame.font.Font(None, 50)
            texto_superficie = fuente.render(f"pasos : {self.pasos}", True, (255,255,255))
            rect_texto = texto_superficie.get_rect()
            rect_texto.center = (100, self.alto * self.tamano_bloque+20)
            self.pantalla.blit(texto_superficie, rect_texto)

            pygame.display.flip()
            self.clock.tick(10)
    # marcar soluciones
    def marcar_soluciones(self):
        return True


# Ejemplo de uso
"""laberinto = [
    [0, 1, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 2]
]

juego = Ventana(laberinto)
juego.ejecutar_juego()"""