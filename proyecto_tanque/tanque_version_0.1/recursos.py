import pygame
import random
from pygame.sprite import Sprite

class Recurso(Sprite):
    def __init__(self, screen, tipo, image_path, position):
        super().__init__()
        self.screen = screen
        self.tipo = tipo
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (30, 30))  # Ajusta el tamaño
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def blitme(self):
        self.screen.blit(self.image, self.rect)

def crear_recurso(screen, tipo, image_path):
    x = random.randint(50, screen.get_width() - 50)
    y = random.randint(50, screen.get_height() - 50)
    recurso = Recurso(screen, tipo, image_path, (x, y))
    return recurso

def generar_recursos(screen, botiquines, municiones):
    tipo_recurso = random.choice(['botiquin', 'municion'])
    if tipo_recurso == 'botiquin':
        nuevo_botiquin = crear_recurso(screen, 'botiquin', 'media/botiquin.png')
        botiquines.add(nuevo_botiquin)
    else:
        nueva_municion = crear_recurso(screen, 'municion', 'media/municion.png')
        municiones.add(nueva_municion)