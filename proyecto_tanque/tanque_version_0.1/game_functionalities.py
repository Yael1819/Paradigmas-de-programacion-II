import pygame
import sys
from Bala import Bala
from Explosion import Explosion
explosiones = []
def game_events(tank_config, screen, tanque1, tanque2, balas_group, paredes):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            game_events_keydown(event, tank_config, screen, tanque1, tanque2, balas_group)
        elif event.type == pygame.KEYUP:
            game_events_keyup(event, tanque1, tanque2)
def game_events_keydown(event, tank_config, screen, tanque1, tanque2, balas_group):
    current_time = pygame.time.get_ticks()

    # Tanque 1 - solo procesar si no está eliminado
    if not tanque1.eliminado:
        if event.key == pygame.K_RETURN:
            if tanque1.can_shoot(current_time):
                bala = Bala(tank_config, screen, tanque1)
                balas_group.add(bala)
                tanque1.disparar()
                tanque1.balas_disparadas += 1

        if event.key == pygame.K_RIGHT:
            tanque1.is_moving_right = True
            tanque1.update_direction()
        elif event.key == pygame.K_LEFT:
            tanque1.is_moving_left = True
            tanque1.update_direction()
        elif event.key == pygame.K_UP:
            tanque1.is_moving_up = True
            tanque1.update_direction()
        elif event.key == pygame.K_DOWN:
            tanque1.is_moving_down = True
            tanque1.update_direction()

    # Tanque 2 - solo procesar si no está eliminado
    if not tanque2.eliminado:
        if event.key == pygame.K_SPACE:
            if tanque2.can_shoot(current_time):
                bala = Bala(tank_config, screen, tanque2)
                balas_group.add(bala)
                tanque2.disparar()
                tanque2.balas_disparadas += 1

        if event.key == pygame.K_d:
            tanque2.is_moving_right = True
            tanque2.update_direction()
        elif event.key == pygame.K_a:
            tanque2.is_moving_left = True
            tanque2.update_direction()
        elif event.key == pygame.K_w:
            tanque2.is_moving_up = True
            tanque2.update_direction()
        elif event.key == pygame.K_s:
            tanque2.is_moving_down = True
            tanque2.update_direction()

def game_events_keyup(event, tanque1, tanque2):
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

def screen_refresh(tank_config, screen, tanque1, tanque2, balas_group, paredes):
    # Dibujar fondo
    background = pygame.image.load(tank_config.background_image_path)
    background = pygame.transform.scale(background, (tank_config.screen_width, tank_config.screen_height))
    screen.blit(background, (0, 0))

    # Dibujar paredes
    for pared in paredes:
        pared.blitme()

    # Verificar colisión de balas con tanques y paredes
    for bala in balas_group.copy():
        # Eliminar balas fuera de la pantalla
        if not screen.get_rect().colliderect(bala.bala_rect):
            balas_group.remove(bala)
            if bala.tanque == tanque1:
                tanque1.balas_disparadas -= 1
            elif bala.tanque == tanque2:
                tanque2.balas_disparadas -= 1
            continue

        # Verificar colisión con paredes
        for pared in paredes:
            if bala.bala_rect.colliderect(pared.rect):
                explosiones.append(Explosion(screen, bala.bala_rect.centerx, bala.bala_rect.centery))
                balas_group.remove(bala)
                if bala.tanque == tanque1:
                    tanque1.balas_disparadas -= 1
                elif bala.tanque == tanque2:
                    tanque2.balas_disparadas -= 1
                break

        # Colisión con tanque 1
        if bala.tanque != tanque1 and bala.bala_rect.colliderect(tanque1.image_rect):
            explosiones.append(Explosion(screen, bala.bala_rect.centerx, bala.bala_rect.centery))
            balas_group.remove(bala)
            if bala.tanque == tanque2:
                tanque2.balas_disparadas -= 1
            tanque1.recibir_dano(20)
            continue

        # Colisión con tanque 2
        if bala.tanque != tanque2 and bala.bala_rect.colliderect(tanque2.image_rect):
            explosiones.append(Explosion(screen, bala.bala_rect.centerx, bala.bala_rect.centery))
            balas_group.remove(bala)
            if bala.tanque == tanque1:
                tanque1.balas_disparadas -= 1
            tanque2.recibir_dano(20)
            continue

    # Actualizar y dibujar explosiones
    for explosion in explosiones[:]:
        explosion.update()
        if not explosion.activa:
            explosiones.remove(explosion)
        else:
            explosion.blitme()

    # Actualizar y dibujar tanques
    if tanque1.eliminado:
        tanque1.blitme()
    else:
        tanque1.update_pos(tanque2, paredes)
        tanque1.blitme()

    if tanque2.eliminado:
        tanque2.blitme()
    else:
        tanque2.update_pos(tanque1, paredes)
        tanque2.blitme()

    # Actualizar posición y dibujar balas
    for bala in balas_group.sprites():
        bala.update_pos()
        bala.blitme()

    pygame.display.flip()