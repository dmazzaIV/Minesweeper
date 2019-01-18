import numpy as np
from gameboard import Gameboard


class view:

    def __init__(self):
        self.board = Gameboard()
        # Create board to hold the flag for whether a tile has been revealed
        self.size = np.sqrt(len(self.board))
        self.bool_board = np.zeros(self.size, self.size)
        self.game_over_flag = False

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
                surrounding_y = y + sur_y
                surroundings.append((surrounding_x, surrounding_y))
        return surroundings

    def reveal_surroundings(self, x: int, y: int):
        """Recursively reveals all tiles that are touching 0 bombs.

        Will genereate a list of all surrounding tiles.
        Iterates through the list.
        Recursively sets the reveal flag for each surrounding tile.
        Reveal all connected tiles that are labelled 0 in the gameboard.
        """
        # Hit an integer that is not a bomb so it stops the reveal process
        if self.board[x, y] != 0 and self.board[x, y] != 9:
            self.bool_board[x, y] = 1
        # Hit a bomb, reveal the bomb and set the game over flag to true
        elif self.board[x, y] == 9:
            self.bool_board[x, y] = 1
            self.game_over_flag = True
        # Hit a 0, reveal all adjacent tiles until you hit an integer >0
        else:
            surroundings = self.get_surroundings_list(x, y)
            self.bool_board[x, y] = 1
            for surrounding in surroundings:
                surrounding_x = surrounding[0]
                surrounding_y = surrounding[1]
                self.reveal_surroundings(surrounding_x, surrounding_y)

    def update_view(self, x: int, y: int) -> bool:
        self.reveal_surroundings(x, y)
        self.print_board()
        return self.game_over_flag
