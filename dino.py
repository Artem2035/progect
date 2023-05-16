import pygame, time
from barrier import Barrier


class Dino:
    def __init__(self):
        self.x = 0
        self.y = 200
        self.speed = 0
        self.cadr = 0
        self.state = "run"
        self.dino_surf = pygame.image.load('assets/dino-menu.png')
        self.dino_surf.set_colorkey((255, 255, 255))
        self.dino_rect = self.dino_surf.get_rect()
        self.start_anim_jump = 0

    def move(self):
        if self.state == "run":
            self.y = 200
            if self.cadr <= 10:
                self.dino_surf = pygame.image.load('assets/dino-run2.png')
            elif self.cadr <= 20:
                self.dino_surf = pygame.image.load('assets/dino-run1.png')
            else:
                self.cadr = 0
            self.cadr += 1
        elif self.state == "jump":
            self.dino_surf = pygame.image.load('assets/dino-menu.png')
            if time.time() - self.start_anim_jump <= 0.75:
                self.jump(-3)
            elif time.time() - self.start_anim_jump <= 1.5:
                self.jump(3)
            else:
                self.change_state("run")
                self.y = 200
                self.start_anim_jump = 0
        elif self.state == "tilt":
            self.y = 217
            if self.cadr <= 10:
                self.dino_surf = pygame.image.load('assets/dino-tilt-1.png')
            elif self.cadr <= 20:
                self.dino_surf = pygame.image.load('assets/dino-tilt-2.png')
            else:
                self.cadr = 0
            self.cadr += 1
        self.dino_surf.set_colorkey((255, 255, 255))
        self.dino_rect = self.dino_surf.get_rect()
        self.dino_rect = self.dino_rect.move(self.x, self.y)
        self.x += self.speed

    def jump(self, speed_y: int):
        self.y += speed_y

    def change_speed(self, v: int):
        self.speed += v

    def coordinates(self):
        return self.x, self.y

    def change_state(self, state):
        self.state = state

    def set_start_anim_time(self):
        self.start_anim_jump = time.time()

    def collision(self, sprites):
        not_collide = True
        for index in range(len(sprites)):
            if isinstance(sprites[index], Barrier) and self.dino_rect.colliderect(sprites[index].rect):
                not_collide = False
                break
            else:
                not_collide = True
        return not_collide
