import pygame
import random


class Cloud:
    def __init__(self, x: int):
        self.x = x
        self.y = random.randint(75, 100)
        self.speed = 4
        self.surf = pygame.image.load(f'assets/cloud.png')
        self.rect = self.surf.get_rect()

    def get_coordinates(self):
        return self.x, self.y

    def move(self):
        self.x -= self.speed

    def check(self):
        if self.x < -52:
            self.x = 600
            self.y = random.randint(75, 100)
