import numpy as np
from gameboard import Gameboard


class view:

    def __init__(self):
        self.board = Gameboard()
        self.size = np.sqrt(len(self.board))
        self.bool_board = np.zeros(self.size, self.size)
