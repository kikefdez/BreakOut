import pygame

# Definimos las constantes de dimensiones de alto y largo que tendrá cada bloque
LARGO = 23
ALTO = 15

# Definimos la constante del color de relleno de cada bloque
AZUL = (0, 0, 255)

class Ladrillo(pygame.sprite.Sprite):
    # Esta clase es la definición del objeto Ladrillo
    # Se situará en la parte superior de la pantalla
    # El objetivo será destruirlos sin que la pelota llegue a la zona de gol

    def __init__(self, posicionX, posicionY):
        # Invocamos al constructor de la clase padre para la inicialización [Sprite]
        super().__init__()
        # Definimos el objeto Ladrillo como una superficie de 23x15
        self.image = pygame.Surface([LARGO, ALTO])
        # Definimos el color de fondo del objeto Ladrillo
        self.image.fill(AZUL)
        # Obtenemos el rectangulo correspondiente al objeto con la configuración anterior
        self.rect = self.image.get_rect()
        # Posicionamos en el espacio el rectangulo en las coordenadas correspondientes
        self.rect.x = posicionX
        self.rect.y = posicionY

