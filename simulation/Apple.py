from utils import Singleton
from .Grid import Grid

class Apple(metaclass=Singleton):
    def __init__(self, canvas, pos):
        self.canvas = canvas
        self.pos = pos
        self.visual = None

    def visualize(self):
        if self.visual is not None:
            self.canvas.delete(self.visual)
        self.visual = self.canvas.create_rectangle(*Grid().calculate_square_coords(*self.pos), fill="yellow")