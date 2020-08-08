from utils import Singleton
import numpy as np
from utils import get_num_squares_in_row_col

class GridModel(metaclass=Singleton):
    _num_squares_in_row = None
    _num_squares_in_col = None

    def __init__(self):
        self.__set_vars()
        self.grid = np.zeros((self._num_squares_in_col, self._num_squares_in_row))

    def __set_vars(self):
        self._num_squares_in_row,self._num_squares_in_col = get_num_squares_in_row_col()