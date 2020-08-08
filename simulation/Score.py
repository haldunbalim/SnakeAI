from utils import Singleton

class Score(metaclass=Singleton):
    def __init__(self, canvas, score):
        self.canvas = canvas
        self.visual = None
        self.score = score

    def visualize(self, width):
        if self.visual is not None:
            self.canvas.delete(self.visual)
        self.visual = self.canvas.create_text(width - 50, 10, text="Score: {}".format(self.score))