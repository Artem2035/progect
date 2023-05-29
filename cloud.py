import pygame
import random


class Cloud:
    ''' Класс облака'''

    def __init__(self, x: int):
        '''Создание обьекта, где X - начальное положение обьекта по X координате '''
        self.x = x
        self.y = random.randint(75, 100)
        self.speed = 4
        self.surf = pygame.image.load(f'assets/cloud.png')
        self.rect = self.surf.get_rect()
        self.rect = self.rect.move(self.x, self.y)


    def move(self):
        ''' Перемещение облака с право налево по X координате'''
        self.x -= self.speed
        self.rect = self.surf.get_rect()
        self.rect = self.rect.move(self.x, self.y)

    def check(self):
        '''
        Проверка выхода облака за правую границу окна приложния
        Перемещение облака за левую границу окна приложния
        '''
        if self.x < -52:
            self.x = 600
            self.y = random.randint(75, 100)
