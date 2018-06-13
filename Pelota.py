import pygame
import math

# Definimos constante de la velocidad en número de píxeles que avanza por cada ciclo
VELOCIDAD = 10

# Definimos las constantes de dimensiones de alto y largo que tendrá la pelota
LARGO = 10
ALTO = 10

# Definimos la constante del color de relleno de la pelota
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

class Pelota(pygame.sprite.Sprite):
    # Esta clase es la definición del objeto Pelota
    # Irá rebotando entre los ladrillos y el portero
    # Si la pelota supera la zona de TouchDown se considerará que ha perdido una vida

    # Definimos las coordenadas con la posición inicial de la pelota
    coordX = 0.0
    coordY = 180.0
     
    # Definimos la dirección (en grados) de la trayectoria de la pelota
    direccion = 200

    def __init__(self):
        # Invocamos al constructor de la clase padre para la inicialización [Sprite]
        super().__init__()
        # Definimos el objeto Pelota como una superficie de 10x10
        self.image = pygame.Surface([LARGO, ALTO])
        # Definimos el color de fondo del objeto Ladrillo
        self.image.fill(BLANCO)
        # Obtenemos el rectangulo correspondiente al objeto con la configuración anterior
        self.rect = self.image.get_rect()

        # Almacenamos las dimensiones de la pelota
        self.altoPelota = ALTO
        self.largoPelota = LARGO

        # Almacenamos la velocidad de la pelota
        self.velocidadPelota = VELOCIDAD

        # Obtenemos las dimensiones del tablero de juego
        self.altoTablero = pygame.display.get_surface().get_height()
        self.largoTablero = pygame.display.get_surface().get_width()


    def rebotar(self, diferencia):
        # Definimos el comportamiento que tendrá la pelota cuando se produzca un rebote bien en un ladrillo o bien en el portero
        self.direccion = (180 - self.direccion) % 360
        self.direccion -= diferencia
    def actualizar(self):
        # Definimos el comportamiento que tendrá la pelota - seguir con la trayectoria definida tras un rebote
        direccionRadianes = math.radians(self.direccion)

        # Calculamos la posición de la pelota en función de la trayectoria y la velocidad
        self.coordX += self.velocidadPelota * math.sin(direccionRadianes)
        self.coordY -= self.velocidadPelota * math.cos(direccionRadianes)

        #pygame.draw.lines(pygame.display.get_surface(), ROJO, False, [(self.coordX + 5, self.coordY + 5), ((self.coordX + 5 + (100 * math.sin(direccionRadianes))), (self.coordY + 5 - (100 * math.cos(direccionRadianes))))], 1)

        #print('[' + str(self.coordX) + ',' + str(self.coordY) + ']')

        # Actualizamos la posición de la pelota
        self.rect.x = self.coordX
        self.rect.y = self.coordY

        # Comprobamos si la trayectoria supera en borde superior de la pantalla
        if self.coordY <= 0:
            self.rebotar(0)
            self.coordY = 1
        # Comprobamos si la trayectoria supera el borde izquierdo de la pantalla
        if self.coordX <= 0:
            self.direccion = (360 - self.direccion) % 360
            self.coordX = 1
        # Comprobamos si la trayectoria supera el borde derecho de la pantalla
        if self.coordX > self.largoTablero - LARGO:
            self.direccion = (360 - self.direccion) % 360
            self.x = self.largoTablero - LARGO - 1
        # Comprobamos si la trayectoria supera el borde inferior de la pantalla - TouchDown
        if self.coordY > 600:
            return True
        else:
            return False
    def posicionar(self):
        posicionMouse = pygame.mouse.get_pos();
        self.rect.x = posicionMouse[0] + 35
        self.rect.y = self.altoTablero - 20
        limite = self.largoTablero - 35
        if self.rect.x > limite:
            self.rect.x = limite
        self.coordX = self.rect.x
        self.coordY = self.rect.y