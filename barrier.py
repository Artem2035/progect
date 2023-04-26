import pygame
import random


class Barrier:
    def __init__(self, x: int):
        self.x = x
        self.y = 308
        self.speed = 3
        image = random.randint(1,3)
        self.surf = pygame.image.load(f'assets/barrier_{image}.png')
        self.rect = self.surf.get_rect()

    def get_coordinates(self):
        return self.x, self.y

    def move(self):
        self.x -= self.speed