import pygame
class Tanque:
    def __init__(self, screen, tank_config, image_path="media/tanque_verde.png"):
        self.screen = screen
        self.tank_config = tank_config
        self.image = pygame.image.load(image_path)
        self.image_original = self.image
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.image_rect_centerx = float(self.image_rect.centerx)
        self.image_rect_centery = float(self.image_rect.centery)
        self.tank_speed = self.tank_config.tank_speed
        self.is_moving_right = False
        self.is_moving_left = False
        self.is_moving_up = False
        self.is_moving_down = False
        self.direction = 'up'
        self.balas_disparadas = 0
        self.max_balas = 10
        self.vida = 100
        self.tiempo_ultima_bala = 0
        self.retraso_disparo = 750
        self.eliminado = False
        self.imagen_destruccion = pygame.image.load("media/bander.png")
        self.puede_disparar = True

    def recibir_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            self.eliminado = True
            self.cambiar_a_imagen_destruccion()

    def cambiar_a_imagen_destruccion(self):
        self.image = pygame.transform.scale(self.imagen_destruccion, self.image.get_size())
        old_center = self.image_rect.center
        self.image_rect = self.image.get_rect()
        self.image_rect.center = old_center

    def update_direction(self):
        if self.is_moving_up:
            self.direction = 'up'
        elif self.is_moving_down:
            self.direction = 'down'
        elif self.is_moving_left:
            self.direction = 'left'
        elif self.is_moving_right:
            self.direction = 'right'

        self.rotate_image()

    def rotate_image(self):
        if self.eliminado:
            return

        if self.direction == 'up':
            self.image = pygame.transform.rotate(self.image_original, 0)
        elif self.direction == 'down':
            self.image = pygame.transform.rotate(self.image_original, 180)
        elif self.direction == 'left':
            self.image = pygame.transform.rotate(self.image_original, 90)
        elif self.direction == 'right':
            self.image = pygame.transform.rotate(self.image_original, -90)

        self.image_rect = self.image.get_rect(center=self.image_rect.center)

    def update_pos(self, otro_tanque, paredes):
        if self.eliminado:
            return

        nueva_posicion = self.image_rect.copy()

        if self.is_moving_right and not (self.is_moving_up or self.is_moving_down or self.is_moving_left):
            nueva_posicion.centerx += self.tank_speed
            self.direction = 'right'
        elif self.is_moving_left and not (self.is_moving_up or self.is_moving_down or self.is_moving_right):
            nueva_posicion.centerx -= self.tank_speed
            self.direction = 'left'
        elif self.is_moving_up and not (self.is_moving_left or self.is_moving_right or self.is_moving_down):
            nueva_posicion.centery -= self.tank_speed
            self.direction = 'up'
        elif self.is_moving_down and not (self.is_moving_left or self.is_moving_right or self.is_moving_up):
            nueva_posicion.centery += self.tank_speed
            self.direction = 'down'

        puede_moverse = True
        if (nueva_posicion.left >= 0 and
                nueva_posicion.right <= self.tank_config.screen_width and
                nueva_posicion.top >= 0 and
                nueva_posicion.bottom <= self.tank_config.screen_height):

            if nueva_posicion.colliderect(otro_tanque.image_rect):
                puede_moverse = False

            for pared in paredes:
                if nueva_posicion.colliderect(pared.rect):
                    puede_moverse = False
                    break

            if puede_moverse:
                self.image_rect = nueva_posicion
                self.image_rect_centerx = float(self.image_rect.centerx)
                self.image_rect_centery = float(self.image_rect.centery)
                self.rotate_image()

    def blitme(self):
        self.screen.blit(self.image, self.image_rect)

    def disparar(self):
        self.tiempo_ultima_bala = pygame.time.get_ticks()

    def can_shoot(self, current_time):
        return (self.balas_disparadas < self.max_balas and
                current_time - self.tiempo_ultima_bala > self.retraso_disparo)