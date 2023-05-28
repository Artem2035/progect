import pygame
import random


class Ground:
    ''' Класс блока земли'''

    def __init__(self, x: int):
        '''Конструктор класса, где X - начальное положени обьекта по X координате '''
        self.x = x
        self.y = 230
        self.speed = 3
        image = random.randint(1, 8)
        self.surf = pygame.image.load(f'assets/ground_{image}.png')
        self.rect = self.surf.get_rect()
        self.rect.move(self.x, self.y)

    def move(self):
        ''' Перемещение объекта по  X координате справо налево, Y не меняется  '''
        self.x -= self.speed
        self.rect = self.surf.get_rect()
        self.rect = self.rect.move(self.x, self.y)
