import pygame
from Tanque import Tanque
from config import Config
import game_functionalities
from pygame.sprite import Group
from Pared import Pared

def run_game():
    pygame.init()
    tank_config = Config()
    screen_size = (tank_config.screen_width, tank_config.screen_height)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption(tank_config.game_title)


    # Crear paredes
    paredes = []
    for pared_info in tank_config.paredes:
        pared = Pared(screen, *pared_info)
        paredes.append(pared)

    tanque1 = Tanque(screen, tank_config)
    tanque1.image_rect.topleft = (100, 100)

    tanque2 = Tanque(screen, tank_config, image_path="media/tanque_arena.png")
    tanque2.image_rect.topleft = (800, 500)

    balas_group = Group()

    while True:
        game_functionalities.game_events(tank_config, screen, tanque1, tanque2, balas_group, paredes)
        game_functionalities.screen_refresh(tank_config, screen, tanque1, tanque2, balas_group, paredes)


run_game()

