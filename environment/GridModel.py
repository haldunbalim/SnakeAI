from utils import Singleton
import numpy as np

class GridModel(metaclass=Singleton):
    _num_squares_in_row = 10
    _num_squares_in_col = 10

    def __init__(self):
        self.__set_vars()
        self.grid = np.zeros((self._num_squares_in_col, self._num_squares_in_row))

    def __set_vars(self):
        self._num_squares_in_row = 10
        self._num_squares_in_col = 10