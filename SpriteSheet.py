import pygame

class SpriteSheet(object):
    # Esta es la clase que se encargará de la gestión de los sprites
    # Nos proporcionará para un objeto el componente gráfico que le corresponde

    def __init__(self, archivoSprites):
        # Invocamos al constructor de la clase padre para la inicialización
        self.sprite_sheet = pygame.image.load(archivoSprites).convert()
    def cargarImagen(self, posX, posY, ancho, alto):
        # Creamos una nueva imagen con las dimensiones correctas
        imageRespuesta = pygame.Surface([ancho, alto]).convert()

        # Cargamos el correspondiente componente gráfico
        imageRespuesta.blit(self.sprite_sheet, (0, 0), (posX, posY, ancho, alto))

        return imageRespuesta


