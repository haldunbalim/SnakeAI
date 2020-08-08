import random
from utils import Singleton
from .GridModel import GridModel
from .SnakeModel import SnakeModel


class AppleModel(metaclass=Singleton):
    def __init__(self):
        self.pos = None
        self.find_place()

    def find_place(self):
        while True:
            i, j = random.randint(0, GridModel()._num_squares_in_col - 1), random.randint(0, GridModel()._num_squares_in_row - 1)
            flag = True
            for ri1, rj1 in SnakeModel().body:
                if i == ri1 and j == rj1:
                    flag = False
                    break
            if flag:
                break
        self.pos = (i, j)