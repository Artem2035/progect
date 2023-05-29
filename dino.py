import pygame, time
from barrier import Barrier
from bird import Bird


class Dino:
    ''' Класс динозаврика(игрока) для игры в  DinoRex '''

    def __init__(self):
        self.x = 0
        self.y = 200
        self.speed = 0
        self.cadr = 0
        self.state = "run"
        self.dino_surf_stay = pygame.image.load('assets/dino-menu.png')
        self.dino_surf_crash = pygame.image.load('assets/dino-crash.png')
        self.dino_surf_run_1 = pygame.image.load('assets/dino-run1.png')
        self.dino_surf_run_2 = pygame.image.load('assets/dino-run2.png')
        self.dino_surf_tilt_1 = pygame.image.load('assets/dino-tilt-1.png')
        self.dino_surf_tilt_2 = pygame.image.load('assets/dino-tilt-2.png')
        self.dino_surf = self.dino_surf_stay
        self.dino_surf.set_colorkey((255, 255, 255))

        self.dino_rect = pygame.Rect(self.dino_surf.get_rect().x, self.dino_surf.get_rect().y,
                                     self.dino_surf.get_rect().width - 13, self.dino_surf.get_rect().height - 7)
        self.dino_rect.x = self.x
        self.dino_rect.y = self.y
        self.start_anim_jump = 0

    def move(self):
        '''
        Перемещение динозаврика по X или Y, обработка состоянии "бег", "прыжок" и  "наклон"
        Обработка анимации бега, прыжка и наклона
        '''
        if self.state == "run":
            self.y = 200
            if self.cadr <= 10:
                self.dino_surf = self.dino_surf_run_1
            elif self.cadr <= 20:
                self.dino_surf = self.dino_surf_run_2
            else:
                self.cadr = 0
            self.cadr += 1
        elif self.state == "jump":
            self.dino_surf = self.dino_surf_stay
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
                self.dino_surf = self.dino_surf_tilt_1
            elif self.cadr <= 20:
                self.dino_surf = self.dino_surf_tilt_2
            else:
                self.cadr = 0
            self.cadr += 1
        self.dino_surf.set_colorkey((255, 255, 255))
        self.dino_rect = pygame.Rect(self.dino_surf.get_rect().x, self.dino_surf.get_rect().y,
                                     self.dino_surf.get_rect().width - 13, self.dino_surf.get_rect().height - 7)
        if self.x + self.speed >= 0 and self.x + self.speed <= 500:
            self.x += self.speed
        self.dino_rect = self.dino_rect.move(self.x, self.y)

    def jump(self, speed_y: int):
        ''' Перемещение динозаврика по Y  '''
        self.y += speed_y

    def change_speed(self, v: int):
        '''
        Определение скорости динозаврика, где V - скорость,
        на которую изменяется скорость динозаврика
        '''
        self.speed += v

    def change_state(self, state: str):
        '''
        изменение текущего состояния(бег, прыжок, наклон) на указанное
        :param state: состояние, на которое нужно изменить текущее состояние динозаврика
        '''
        if state == "run" or state == "tilt" or state == "jump":
            self.state = state
        else:
            self.state = "run"

    def set_start_anim_time(self):
        '''
        Фиксироваие начало  времени анимации прыжка
        Необходимо для корректной работы анимации прыжка
        '''
        self.start_anim_jump = time.time()

    def collision(self, sprites):
        '''
        Проверка столкновения динозаврика и списка обьектов(препятствии, птицы)
        :param sprites: Список обьектов, для проверки на столкновение
        :return: Возвращает True, если не было столкновения
        '''
        not_collide = True
        for index in range(len(sprites)):
            if isinstance(sprites[index], Barrier) and self.dino_rect.colliderect(sprites[index].rect):
                self.dino_surf = self.dino_surf_crash
                not_collide = False
                break
            if isinstance(sprites[index], Bird) and self.dino_rect.colliderect(sprites[index].bird_rect):
                self.dino_surf = self.dino_surf_crash
                not_collide = False
                break
        if self.state == "tilt" and not not_collide:
            self.y = 200
            self.x += 10
            self.dino_rect = self.dino_rect.move(10, -17)
        self.dino_surf.set_colorkey((255, 255, 255))
        return not_collide
