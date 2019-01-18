import numpy as np
from gameboard import Gameboard


class view:

    def __init__(self):
        self.board = Gameboard()
        # Create board to hold the flag for whether a tile has been revealed
        self.size = np.sqrt(len(self.board))
        self.bool_board = np.zeros(self.size, self.size)

    def print_board(self):
        """Prints the current state of the game view.

        If a tile has not been revealed (the value of bool_board
        at that position is 0) then it will display as a '-'
        If a tile has been revealed it will display the value
        of the gameboard at that position.bool_board.
        """
        for x in range(0, self.size):
            for y in range(0, self.size):
                if self.bool_board[x, y] == 0:
                    print('-')
                else:
                    print(self.board[x, y])
            print('\n')

    def get_surroundings_list(self, x: int, y: int) -> list:
        """Generates the list coordiantes surrounding a given tile.

        Returns a list of tuples.
        Each tuple is an x, y coordinate pair.
        Each coordinate pair corresponds to a surrounding tile.
        """
        surroundings = []
        for sur_x in [-1, 0, 1]:
            for sur_y in [-1, 0, 1]:
                surrounding_x = x + sur_x
                surrouding_y = y + sur_y
                surroundings.append((sur_x, sur_y))
        return surroundings

    def reveal_surroundings(self, x: int, y: int):
        """Recursively reveals all tiles that are touching 0 bombs.

        Will genereate a list of all surrounding tiles.
        Iterates through the list.
        Recursively sets the reveal flag for each surrounding tile.
        Revealing all tiles that are labelled 0 in the gameboard.
        """
        surroundings = self.get_surroundings_list(x, y)


    def update_view(self, x: int, y: int):
        self.bool_board[x, y] = 1
        self.print_board()

