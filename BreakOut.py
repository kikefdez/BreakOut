import math
import pygame

from Ladrillo import *
from Pelota import *
from Portero import * 


def pausarJuego():
    juegoPausado = True

    # Mostramos un mensaje informando que el juego está pausado
    alertaPausa = fuenteJuego.render('JUEGO PAUSADO', True , BLANCO)
    alertaPausa_posicion = alertaPausa.get_rect(centerx=tableroJuego.get_width() / 2)
    alertaPausa_posicion.top = 300
    tablero.blit(alertaPausa, alertaPausa_posicion)

    # Generamos un buqle hasta que detectemos que se ha producido de nuevo el KeyDown del espacio para reanudar el juego
    while juegoPausado:
        for accion in pygame.event.get():
            if accion.type == pygame.QUIT:
                pygame.quit()
            if accion.type == pygame.KEYDOWN:
                if accion.key == 32:
                    juegoPausado = False
                pygame.display.update()

# Definimos las constantes de colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Inicializamos la librería pygame para comenzar a jugar
pygame.init()
# Definimos el título de la ventana
pygame.display.set_caption('Breakout')
# Ocultamos el puntero del ratón mientras esté encima del tablero de juego
pygame.mouse.set_visible(0)
# Definimos el tamaño de letra que usaremos
fuenteJuego = pygame.font.Font(None, 36)

#Definimos la resolución de pantalla a 600x600
tablero = pygame.display.set_mode([600, 600])
# Recuperamos el tablero de juego para poder operar con él
tableroJuego = pygame.Surface(tablero.get_size())

# Creamos las variables responsable de controlar la salida y fin del juego
gameOver = False
exitJuego = False

# Creamos el reloj que controlará el tiempo de juego
reloj = pygame.time.Clock()

# Cargamos los componentes visuales del juego
spTotal = pygame.sprite.Group()

spPelota = pygame.sprite.Group()
valorPelota = Pelota()
spPelota.add(valorPelota)
spTotal.add(valorPelota)

spPortero = pygame.sprite.Group()
valorPortero = Portero()
spPortero.add(valorPortero)
spTotal.add(valorPortero)

spLadrillo = pygame.sprite.Group()

# Definimos la altura inicial de los bloques
topLadrillo = 80
# Generamos todos los cuadros del panel superior
# 5 filas con 25 ladrillos cada una [600 / 24 = 25] siendo 24 = 23 del ancho del ladrillo + 1 de separación
for fila in range(5):
    for columna in range(0, 32):
        valorLadrillo = Ladrillo(columna * 24, topLadrillo)
        spLadrillo.add(valorLadrillo)
        spTotal.add(valorLadrillo)
    topLadrillo += 17

puntuacion = 0
temporizador = 0
iniciado = False
vidas = 3

while not exitJuego:
    # Definimos el jugo a 30 fps
    reloj.tick(30)

    # Definimos el color fondo del tablero de juego
    tablero.fill(NEGRO)

    # Controlamos los eventos para detectar el fin de juego
    for accion in pygame.event.get():
        # En caso de producirse el evento de salida cambiamos el estado de la variable
        if accion.type == pygame.QUIT:
            exitJuego = True
        # En caso de producirse el evento de presionar una tecla y que corresponde al espacio, pausamos el juego
        if accion.type == pygame.KEYDOWN:
            if accion.key == 32:
                pausarJuego()
        if accion.type == pygame.MOUSEBUTTONUP:
            iniciado = True

    # Comprobamos si se ha producido el Game Over
    if gameOver:
        alertaGameOver = fuenteJuego.render('Game Over', True , BLANCO)
        alertaGameOver_posicion = alertaGameOver.get_rect(centerx=tableroJuego.get_width() / 2)
        alertaGameOver_posicion.top = 300
        tablero.blit(alertaGameOver, alertaGameOver_posicion)
    else:
        valorPortero.actualizar()
        if iniciado:
            if valorPelota.actualizar():
                if vidas > 0:
                    vidas -= 1
                    valorPelota.posicionar()
                    iniciado = False
                else:
                    gameOver = True
        else:
            valorPelota.posicionar()

    # Comprobamos si la pelota choca contra el portero y produce un rebote
    if pygame.sprite.spritecollide(valorPortero, spPelota, False):
        trayectoria = (valorPortero.rect.x + valorPortero.largoPortero / 2) - (valorPelota.rect.x + valorPelota.largoPelota / 2)
        valorPelota.rebotar(trayectoria)

    # Comprobamos si la pelota choca contra algún ladrillo y produce un rebote
    bloquesRestantes = pygame.sprite.spritecollide(valorPelota, spLadrillo, True)

    # Si existen bloques es que se ha producido un rebote en los ladrillos
    if len(bloquesRestantes) > 0:
        puntuacion += len(bloquesRestantes) * 10
        valorPelota.rebotar(0)
    
    # Si ya no existen ladrillos significa que todos han sido eliminados y el juego ha terminado
    if len(spLadrillo) == 0:
        gameOver = True

    if not gameOver & iniciado:
        # Posicionamos el área de informar la puntuación alcanzada
        alertaPuntuacion = fuenteJuego.render('Puntuacion: ' + str(puntuacion), True , BLANCO)
        alertaPuntuacion_posicion = alertaPuntuacion.get_rect(centerx = tableroJuego.get_width() / 4)
        alertaPuntuacion_posicion.top = 10
        
        # Posicionamos el área para informar del tiempo consumido
        tiempo = temporizador // 30
        alertaTemporizador = fuenteJuego.render('Tiempo: {0:02}:{1:02}'.format(tiempo // 60, tiempo % 60), True , BLANCO)
        alertaTemporizador_posicion = alertaTemporizador.get_rect(centerx = tableroJuego.get_width() * 3 / 4)
        alertaTemporizador_posicion.top = 10
        temporizador += 1

    # Actualizamos los valores de puntuación y tiempo mostrados por pantalla
    tablero.blit(alertaPuntuacion, alertaPuntuacion_posicion)
    tablero.blit(alertaTemporizador, alertaTemporizador_posicion)

    # Dibujamos los elementos visuales en la pantalla
    spTotal.draw(tablero)
    #Actualizamos el tablero de juego con los nuevos elementos visuales
    pygame.display.update()
# Salimos del entorno
pygame.quit()

