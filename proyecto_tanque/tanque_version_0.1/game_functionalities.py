import sys
import pygame
from Bala import Bala

def game_events(tank_config, screen, tanque1, tanque2, balas_group):
    """Función que administra los eventos del juego."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            game_events_keydown(event, tank_config, screen, tanque1, tanque2, balas_group)

        elif event.type == pygame.KEYUP:
            game_events_keyup(event, tanque1, tanque2)

def game_events_keydown(event, tank_config, screen, tanque1, tanque2, balas_group):
    """Función que administra el evento cuando se presiona una tecla."""
    # Tanque 1 (movimiento con las teclas de flecha)
    if event.key == pygame.K_RIGHT:
        tanque1.is_moving_right = True
    elif event.key == pygame.K_LEFT:
        tanque1.is_moving_left = True
    elif event.key == pygame.K_UP:
        tanque1.is_moving_up = True
    elif event.key == pygame.K_DOWN:
        tanque1.is_moving_down = True

    # Tanque 2 (movimiento con las teclas W, A, S, D)
    if event.key == pygame.K_d:
        tanque2.is_moving_right = True
    elif event.key == pygame.K_a:
        tanque2.is_moving_left = True
    elif event.key == pygame.K_w:
        tanque2.is_moving_up = True
    elif event.key == pygame.K_s:
        tanque2.is_moving_down = True

    # Crear una bala cuando se presiona la tecla Enter (Tanque 1)
    elif event.key == pygame.K_RETURN:
        if len(balas_group) < 3:  # Verifica si hay menos de 3 balas activas
            new_bala = Bala(tank_config, screen, tanque1)
            balas_group.add(new_bala)

    # Crear una bala cuando se presiona la tecla espacio (Tanque 2)
    elif event.key == pygame.K_SPACE:
        if len(balas_group) < 3:  # Verifica si hay menos de 3 balas activas
            new_bala = Bala(tank_config, screen, tanque2)
            balas_group.add(new_bala)

def game_events_keyup(event, tanque1, tanque2):
    """Función que maneja el evento cuando se suelta una tecla."""
    if event.key == pygame.K_RIGHT:
        tanque1.is_moving_right = False
    elif event.key == pygame.K_LEFT:
        tanque1.is_moving_left = False
    elif event.key == pygame.K_UP:
        tanque1.is_moving_up = False
    elif event.key == pygame.K_DOWN:
        tanque1.is_moving_down = False

    if event.key == pygame.K_d:
        tanque2.is_moving_right = False
    elif event.key == pygame.K_a:
        tanque2.is_moving_left = False
    elif event.key == pygame.K_w:
        tanque2.is_moving_up = False
    elif event.key == pygame.K_s:
        tanque2.is_moving_down = False

def screen_refresh(tank_config, screen, tanque1, tanque2, balas_group):
    """Función que refresca la pantalla y dibuja los objetos."""
    background = pygame.image.load(tank_config.background_image_path)
    background = pygame.transform.scale(background, (
        tank_config.screen_width, tank_config.screen_height))

    screen.blit(background, (0, 0))

    tanque1.update_pos()
    tanque2.update_pos()

    tanque1.blitme()
    tanque2.blitme()

    for bala in balas_group.copy():  # Itera sobre las balas y elimina las que están fuera de la pantalla
        bala.update_pos()
        if (bala.bala_rect.bottom < 0 or
            bala.bala_rect.top > tank_config.screen_height or
            bala.bala_rect.right < 0 or
            bala.bala_rect.left > tank_config.screen_width):
            balas_group.remove(bala)  # Elimina la bala del grupo si está fuera de los límites.
        else:
            bala.blitme()

    pygame.display.flip()  # Actualiza la pantalla
