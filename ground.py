import pygame
import random


class Ground:
    def __init__(self, x: int):
        self.x = x
        self.y = 330
        self.speed = 3
        image = random.randint(1,8)
        self.surf = pygame.image.load(f'assets/ground_{image}.png')
        self.rect = self.surf.get_rect()

    def get_coordinates(self):
        return self.x, self.y

    def move(self):
        self.x -= self.speed