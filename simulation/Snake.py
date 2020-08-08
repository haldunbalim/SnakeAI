from utils import Singleton
from .Grid import Grid

class Snake(metaclass=Singleton):
    def __init__(self, canvas, body):
        self.canvas = canvas
        snake_init_size = 3  # square
        init_pos = Grid()._offset // 2
        self.rects = body
        self.rect_visuals = []
        self.head_visual = None
        self.visualize()

    def visualize(self):
        if len(self.rect_visuals) != 0:
            for rect in self.rect_visuals:
                self.canvas.delete(rect)

        if self.head_visual is not None:
            self.canvas.delete(self.head_visual)

        for rect in self.rects:
            rect_visual = self.canvas.create_rectangle(*Grid().calculate_square_coords(*rect), fill="green")
            self.rect_visuals.append(rect_visual)

        head = self.rects[0]
        x1, y1, x2, y2 = Grid().calculate_square_coords(*head)
        x1 += Grid()._square_edge_len // 4
        y1 += Grid()._square_edge_len // 4
        x2 -= Grid()._square_edge_len // 4
        y2 -= Grid()._square_edge_len // 4
        self.head_visual = self.canvas.create_oval(x1, y1, x2, y2, fill="red")