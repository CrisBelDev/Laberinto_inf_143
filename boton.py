import pygame

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

# Configurar la ventana
ancho_ventana = 800
alto_ventana = 600
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Ejemplo de botones")

# Clase para el botón
class Boton:
    def __init__(self, x, y, ancho, alto, color_normal, color_destacado, texto, fuente):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color_normal = color_normal
        self.color_destacado = color_destacado
        self.texto = texto
        self.fuente = fuente
        self.destacado = False

    def dibujar(self):
        color = self.color_destacado if self.destacado else self.color_normal
        pygame.draw.rect(ventana, color, self.rect)
        texto_renderizado = self.fuente.render(self.texto, True, BLANCO)
        texto_rect = texto_renderizado.get_rect(center=self.rect.center)
        ventana.blit(texto_renderizado, texto_rect)

    def actualizar(self):
        self.destacado = self.rect.collidepoint(pygame.mouse.get_pos())

# Fuente




# Bucle principal del juego
"""while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if boton.rect.collidepoint(event.pos):
                print("Haz clic en el botón")

    # Actualizar
    boton.actualizar()

    # Dibujar
    ventana.fill(NEGRO)
    boton.dibujar()
    pygame.display.flip()"""
