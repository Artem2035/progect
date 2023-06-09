import random
import pygame
from dino import Dino
from terrain import Terrain
from cloud import Cloud


class Game:
    '''
    Класс Game совмещает необходимые оъекты и параметры для игры
    '''

    def __init__(self):
        self.back_color = (255, 255, 255)
        self.best_score_color = (255, 126, 83)
        self.score_color = (127, 127, 127)
        self.size = (600, 300)
        self.FPS = 30
        self.player = Dino()
        self.game_terrain = Terrain()
        self.sky = [Cloud(600), Cloud(600 + random.randint(100, 300)), Cloud(600 + random.randint(350, 450))]
        self.score = 0
        self.running = True

        # retry_button
        self.surf = pygame.image.load('assets/retry_button.png')
        self.surf.set_colorkey((255, 255, 255))
        self.button_rect = self.surf.get_rect()
        self.button_rect = self.button_rect.move(264,118)