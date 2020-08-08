from utils import Singleton
from utils import get_num_squares_in_row_col


# TODO: Make dynamic edge length and move canvas specs to config
class Grid(metaclass=Singleton):
    _square_edge_len = 50
    _offset = 50
    _num_squares_in_row = None
    _num_squares_in_col = None

    def __init__(self, canvas):
        # create grid
        self.__set_vars()
        self.canvas = canvas
        for i in range(self._num_squares_in_col):
            for j in range(self._num_squares_in_row):
                self.canvas.create_rectangle(*self.calculate_square_coords(i, j))

    def __set_vars(self):
        self._num_squares_in_row, self._num_squares_in_col = get_num_squares_in_row_col()
        #self._square_edge_len = (Simulator._canvas_grid_space_width - self._offset) / self._num_squares_in_col

    def calculate_square_coords(self, i, j):
        return (i * self._square_edge_len + self._offset // 2, j * self._square_edge_len + self._offset // 2,
                (i + 1) * self._square_edge_len + self._offset // 2,
                (j + 1) * self._square_edge_len + self._offset // 2)

    # redundant
    def get_square_index_by_coords(self, x, y):
        return (x - self._offset) // self._square_edge_len + 1, (y - self._offset) // self._square_edge_len + 1


