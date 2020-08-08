from tkinter import *
from .Grid import Grid
from .Snake import Snake
from .Apple import Apple
from .Score import Score
from .State import State

class Simulator(object):
    _idx = 0
    _canvas_grid_space_width = 550
    _canvas_grid_space_height = 550
    _state_description_space = 250
    _canvas_width = _canvas_grid_space_width + _state_description_space
    _canvas_height = _canvas_grid_space_height

    def __init__(self, snake_history, apple_history, score_history, state_history, manual=False, **kwargs):
        self.root = Tk()
        self.frame = Frame(self.root, width=self._canvas_width, height=self._canvas_height)
        self.canvas = Canvas(self.frame, width=self._canvas_width, height=self._canvas_height)
        self.grid = Grid(self.canvas)
        self.snake_history = snake_history
        self.apple_history = apple_history
        self.score_history = score_history
        self.state_history = state_history
        self.snake = Snake(self.canvas, snake_history[self._idx])
        self.apple = Apple(self.canvas, apple_history[self._idx])
        self.score = Score(self.canvas, score_history[self._idx])
        self.state = State(self.canvas, state_history[self._idx])
        self.manual = manual
        if self.manual:
            self.frame.focus_set()
            self.frame.bind("<Key>", self.key)
        else:
            self.root.after(0, self.animation)

        self.canvas.pack()
        self.frame.pack()

    def animation(self):
        if self._idx < len(self.snake_history):
            self.root.after(500, self.animation)
            self.__animate()

    def __animate(self):
        self.snake.rects = self.snake_history[self._idx]
        self.snake.visualize()
        self.apple.pos = self.apple_history[self._idx]
        self.apple.visualize()
        self.score.score = self.score_history[self._idx]
        self.score.visualize(self._canvas_grid_space_width)
        self.state.data = self.state_history[self._idx]
        self.state.visualize(self._canvas_grid_space_width)
        self._idx += 1

    def key(self, event):
        if self._idx < len(self.snake_history) and event.char == " ":
            self.__animate()

    def start(self):
        self.root.mainloop()