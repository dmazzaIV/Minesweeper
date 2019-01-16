import numpy as np
import random


class Gameboard():
    """Class to create and populate gameboard."""

    def __init__(self):
        self.board = self._generate_board()
        self.mine_coords = self._generate_bombs()
        self._populate_board()

    def _set_difficulty(self) -> dict:
        """Saves board size and number of bombs into a dictionary.

        The settings dictionary will have 3 keys: 'easy', 'medium', and 'hard'.
        Each difficulty key holds a dictionary that stores the board size
        and bomb count for that difficulty.
        i.e. settings[easy] holds dictionary {'board size' : 9, 'mines' : 10}.
        """
        easy = {'board size': 9, 'mines': 10}
        medium = {'board size': 16, 'mines': 40}
        hard = {'board size': 21, 'mines': 90}
        settings = {'easy': easy, 'medium': medium, 'hard': hard}

        difficulty = input('Enter a difficulty(easy, medium, or hard): ')
        while difficulty not in settings:
            print(f'{difficulty} is not a difficulty')
            difficulty = input('Enter a difficulty(easy, medium, or hard): ')

        return settings[difficulty]

    def _generate_board(self) -> np.array:
        """Generates a gameboard of 0's that will be NxN indicies.

        Where N is the value of the board size key in the settings dict.
        """
        self.settings = self._set_difficulty()
        board_size = self.settings['board size']
        board = np.zeros([board_size, board_size])
        return board

    def _generate_bombs(self) -> list:
        """Randomly selects coordinates in the grid to place bombs.

        Returns a list of tuples
        Each tuple being a coordinate to a mine on the gameboard.
        i.e. [(1,2), (6,1), (4,3)]
        """
        mine_coords = []
        boundry = self.settings['board size'] - 1
        total_mines = self.settings['mines']
        placed_mines = 0

        while placed_mines < total_mines:
            mine_x = random.randint(0, boundry)
            mine_y = random.randint(0, boundry)
            coords = (mine_x, mine_y)

            # Check if there is already a mine at that location
            # If not save it as a valid mine coordinate
            if coords not in mine_coords:
                mine_coords.append(coords)
                placed_mines += 1
        return mine_coords

    def _populate_board(self):
        """Places mines on the gameboard.

        After placing a mine,
        updates tiles to display the number of mines each tile is touching.
        """
        boundry = self.settings['board size']
        for mine in self.mine_coords:
            mine_x = mine[0]
            mine_y = mine[1]
            self.board[mine_x, mine_y] = 9
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if (0 <= mine_x + x < boundry and 0 <= mine_y + y < boundry
                            and self.board[mine_x + x, mine_y + y] != 9):
                        self.board[mine_x + x, mine_y + y] += 1

    def __getitem__(self, point):
        """Overrides the __getitem__ magic method.

        Allows access to indicies through keys instead of a getter.
        i.e. board[0, 0] -> value at index (0, 0) on the gameboard
        """
        x, y = point
        return self.board[x, y]

    def __len__(self):
        """Overrides the __len__ magic method.

        Prints out the total number of indicies in our gameboard.
        """
        n, m = self.board.shape
        return n * m

    def __str__(self):
        """Overrides the __str__ magic method.

        Allows printing of the gameboard with as a 2D array.
        """
        return print(self.board)
