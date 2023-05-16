import random
import pygame
from dino import Dino
from terrain import Terrain
from cloud import Cloud


class Game:

    def __init__(self):
        self.back_color = (255, 255, 255)
        self.score_color = (255, 126, 83)
        self.size = (600, 300)
        self.FPS = 30
        self.player = Dino()
        self.game_terrain = Terrain()
        self.sky = [Cloud(600), Cloud(600 + random.randint(100, 300)), Cloud(600 + random.randint(350, 450))]
        self.score = 0
        self.running = True

        self.surf_retry_button = pygame.image.load('assets/retry_button.png')
        self.surf_retry_button.set_colorkey((255, 255, 255))
        self.retry_button_rect = self.surf_retry_button.get_rect()
        self.retry_button_rect.x = 264
        self.retry_button_rect.y = 118