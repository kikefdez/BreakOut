import pygame
from SpriteSheet import *

# Definimos las constantes de dimensiones de alto y largo que tendrá cada bloque
LARGO = 30
ALTO = 30

# Definimos la constante del color de relleno de cada bloque
AZUL = (0, 0, 255)


class Ladrillo(pygame.sprite.Sprite):
    # Esta clase es la definición del objeto Ladrillo
    # Se situará en la parte superior de la pantalla
    # El objetivo será destruirlos sin que la pelota llegue a la zona de gol

    def getLargo():
        return LARGO
    def getAlto():
        return ALTO

    def __init__(self, fila, posicionX, posicionY):
        # Invocamos al constructor de la clase padre para la inicialización [Sprite]
        super().__init__()
        # Definimos el objeto Ladrillo como una superficie de 23x15
        self.image = pygame.Surface([LARGO, ALTO])
        # Definimos el color de fondo del objeto Ladrillo
        # self.image.fill(AZUL)
        sprites = SpriteSheet("breakout_sprites.png")
        self.image = sprites.cargarImagen(40 * fila, 0, 30, 30)

        # Obtenemos el rectangulo correspondiente al objeto con la configuración anterior
        self.rect = self.image.get_rect()
        # Posicionamos en el espacio el rectangulo en las coordenadas correspondientes
        self.rect.x = posicionX
        self.rect.y = posicionY

    def quitarDureza(self):
        if(self.fila > 1):
            self.fila -= 1
            sprites = SpriteSheet("breakout_sprites.png")
            self.image = sprites.cargarImagen(40 * fila, 0, 30, 30)
            return False
        else:
            return True