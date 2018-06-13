import pygame

# Definimos las constantes de dimensiones de alto y largo que tendrá el portero
LARGO = 70
ALTO = 10

# Definimos la constante del color de relleno del portero
BLANCO = (255, 255, 255)

class Portero(pygame.sprite.Sprite):
    # Esta clase es la definición del objeto Portero
    # Será necesario ir moviendo el portero para que la pelota rebote y así evitar
    # que esta supere la zona de TouchDown ya que se considerará que ha perdido una vida

    def __init__(self):
        # Invocamos al constructor de la clase padre para la inicialización [Sprite]
        super().__init__()
        # Definimos el objeto Portero como una superficie de 70x10
        self.image = pygame.Surface([LARGO, ALTO])
        # Definimos el color de fondo del objeto Ladrillo
        self.image.fill(BLANCO)
        # Obtenemos el rectangulo correspondiente al objeto con la configuración anterior
        self.rect = self.image.get_rect()
        
        # Obtenemos las dimensiones del tablero de juego
        self.altoTablero = pygame.display.get_surface().get_height()
        self.largoTablero = pygame.display.get_surface().get_width()

        # Definimos las dimensiones del portero
        self.altoPortero = ALTO
        self.largoPortero = LARGO

        # Definimos la posicion inicial del portero
        self.rect.x = 0
        self.rect.y = self.altoTablero - self.altoPortero
    def actualizar(self):
        posicionMouse = pygame.mouse.get_pos();
        self.rect.x = posicionMouse[0]
        limite = self.largoTablero - self.largoPortero
        if self.rect.x > limite:
            self.rect.x = limite