class Config:
    def __init__(self):
        self.game_title = "Tank Battle"
        self.screen_width = 1080
        self.screen_height = 720
        self.background_image_path = "media/fondo.jpg"
        self.tank_speed = 6
        self.bala_speed = 8

        # Definir la posición de las paredes [x, y, ancho, alto]
        self.paredes = [
            [300, 100, 50, 200],  # Pared vertical izquierda
            [700, 100, 50, 200],  # Pared vertical derecha
            [300, 500, 50, 200],  # Pared vertical inferior izquierda
            [700, 500, 50, 200],  # Pared vertical inferior derecha
            [400, 380, 200, 50],  # Pared horizontal central
        ]