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

    # Inicializar sonidos
    sonido_disparo = pygame.mixer.Sound("media/disparo.mp3")
    sonido_vacio = pygame.mixer.Sound("media/vacio.mp3")
    sonido_botiquin = pygame.mixer.Sound("media/recoger_botiquin.mp3")
    sonido_municion = pygame.mixer.Sound("media/recoger_municion.mp3")

    # Ajustar volumen
    for sonido in [sonido_disparo, sonido_vacio, sonido_botiquin, sonido_municion]:
        sonido.set_volume(0.5)



    # Crear grupos de sprites
    botiquines = Group()
    municiones = Group()

    # Configurar temporizador para generar recursos
    pygame.time.set_timer(pygame.USEREVENT, 10000)  # Cada 10 segundos

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
        game_functionalities.game_events(tank_config, screen, tanque1, tanque2, balas_group, paredes, botiquines, municiones, sonido_disparo, sonido_vacio)
        game_functionalities.screen_refresh(tank_config, screen, tanque1, tanque2, balas_group, paredes, botiquines, municiones)

run_game()

