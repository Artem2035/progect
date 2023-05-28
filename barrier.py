import pygame
import random


class Barrier:
    ''' Класс препятствия: кактуса или камня '''

    def __init__(self, x: int):
        '''Создание обьекта, где X - начальное положение обьекта по X координате '''
        self.x = x
        self.y = 208
        self.speed = 3
        image = random.randint(1, 3)
        self.surf = pygame.image.load(f'assets/barrier_{image}.png')
        self.rect = self.surf.get_rect()
        self.rect.move(x, self.y)

    def move(self):
        '''  изменение положения препятствия по x на значение скорости  '''
        self.x -= self.speed
        self.rect = self.surf.get_rect()
        self.rect = self.rect.move(self.x, self.y)
