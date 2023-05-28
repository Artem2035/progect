from ground import Ground
from barrier import Barrier
from bird import Bird
import random


class Terrain:
    '''
    Класс игрового поля, содержит объекты земли, барьеров, включая препятствие - птицу
    Размер игрового поля 30 блоков
    '''

    def __init__(self):
        '''
        Создание игрового поля размером 30 блоков
        1 блок - 20 пикселей
        '''
        self.terrain = []
        for i in range(31):
            self.terrain.append(Ground(20 * i))

    def ckeck_ground(self):
        '''
        Проверка выходит ли крайнии левый блок за правую границу окна приложения
        При выходе, происходит удаление 1го блока и добавляется блок - земли,барьера или птицы - в конец поля
        '''
        if self.terrain[0].x < -20:
            self.terrain.pop(0)
            self.generate_terrain(0)

    def generate_terrain(self, score: int):
        '''процесс генерации последенго(30) блока игрового поля  '''
        length = len(self.terrain) - random.randint(8, 16)

        if (any(isinstance(block, Barrier) for block in self.terrain[length:]) or
                any(isinstance(block, Bird) for block in self.terrain[length:])):
            self.terrain.append(Ground(self.terrain[len(self.terrain) - 1].x + 20))
        else:
            if random.randint(0, 50) > 27:
                self.terrain.append(Bird(self.terrain[len(self.terrain) - 1].x + 20))
            else:
                self.terrain.append(Barrier(self.terrain[len(self.terrain) - 1].x + 20))
