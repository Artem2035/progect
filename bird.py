import pygame
import random

class Bird:
    def __init__(self, x: int):
        #генерация блока под птицей
        self.block_x = x
        self.block_y = 230
        self.block_speed = 3
        self.surf = pygame.image.load(f'assets/ground_1.png')
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.move(self.block_x, self.block_y)
        #генерация птицы
        self.x = x
        self.y = 180
        self.speed = 3
        self.cadr = 0
        self.bird_surf = pygame.image.load('assets/bird_1.png')
        self.bird_run_1 = self.bird_surf
        self.bird_run_2 = pygame.image.load('assets/bird_2.png')
        self.bird_surf.set_colorkey((255, 255, 255))
        self.bird_rect = self.bird_surf.get_rect()

    def move(self):
        #движение препятствия - птицы
        if self.cadr <= 10:
            self.bird_surf = self.bird_run_1
        elif self.cadr <= 20:
            self.bird_surf = self.bird_run_2
        else:
            self.cadr = 0
        self.cadr += 1
        self.x -= self.speed
        self.bird_surf.set_colorkey((255, 255, 255))
        self.bird_rect = self.bird_surf.get_rect()
        self.bird_rect = self.bird_rect.move(self.x, self.y)
        #передвижение блока под птицей
        self.block_x -= self.block_speed
        self.rect = self.surf.get_rect()
        self.rect = self.rect.move(self.block_x, self.block_y)