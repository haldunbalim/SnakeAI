from utils import Singleton
from collections import deque
from .Direction import Direction

class SnakeModel(metaclass=Singleton):
    def __init__(self):
        self.body = deque([(5, 5), (5, 6), (5, 7)])
        self.direction = Direction.NORTH

    def move(self):
        old_head = self.body[0]

        if self.direction is Direction.NORTH:
            new_head = (old_head[0], old_head[1] - 1)
        elif self.direction is Direction.SOUTH:
            new_head = (old_head[0], old_head[1] + 1)
        elif self.direction is Direction.EAST:
            new_head = (old_head[0] + 1, old_head[1])
        elif self.direction is Direction.WEST:
            new_head = (old_head[0] - 1, old_head[1])

        return new_head