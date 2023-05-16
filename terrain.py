from ground import Ground
from barrier import Barrier
import random


class Terrain:

    def __init__(self):
        self.terrain = []
        for i in range(31):
            self.terrain.append(Ground(20 * i))

    def ckeck_ground(self):
        if self.terrain[0].x < -20:
            self.terrain.pop(0)
            self.generate_terrain()

    def generate_terrain(self):
        length = len(self.terrain) - random.randint(8, 16)

        if any(isinstance(block, Barrier) for block in self.terrain[length:]):
            self.terrain.append(Ground(self.terrain[len(self.terrain) - 1].x + 20))
        else:
            self.terrain.append(Barrier(self.terrain[len(self.terrain) - 1].x + 20))
