"""
Name: Miles James
SID: 003100448

Boggle Solver
-------------
Implements a solver for the Boggle word game.
"""


class Boggle:
    """
    Boggle game solver class.
    """

    def __init__(self, grid=None, dictionary=None):
        self.grid = []
        self.dictionary = []
        self.solution = []

        if grid is not None:
            self.setGrid(grid)
        if dictionary is not None:
            self.setDictionary(dictionary)

    def setGrid(self, grid):
        """
        Sets the game grid.
        Grid must be a 2D list of strings.
        """
        if not grid or not isinstance(grid, list):
            self.grid = []
            return

        size = len(grid)
        new_grid = []

        for row in grid:
            if not isinstance(row, list) or len(row) != size:
                self.grid = []
                return

            new_row = []
            for tile in row:
                new_row.append(tile.upper())
            new_grid.append(new_row)

        self.grid = new_grid

    def setDictionary(self, dictionary):
        """
        Sets the dictionary of valid words.
        """
        if not dictionary or not isinstance(dictionary, list):
            self.dictionary = []
            return

        self.dictionary = [word.upper() for word in dictionary]

    def getSolution(self):
        """
        Returns a list of valid words found in the grid.
        """
        if not self.grid or not self.dictionary:
            return []

        self.solution = []
        rows = len(self.grid)
        cols = len(self.grid[0])

        for word in self.dictionary:
            if len(word) < 3:
                continue

            if self._existsInGrid(word, rows, cols):
                self.solution.append(word)

        return self.solution

    def _existsInGrid(self, word, rows, cols):
        """
        Checks if a word exists in the grid.
        """
        for r in range(rows):
            for c in range(cols):
                visited = [[False for _ in range(cols)] for _ in range(rows)]
                if self._dfs(r, c, word, 0, visited):
                    return True
        return False

    def _dfs(self, r, c, word, index, visited):
        """
        Depth-first search helper.
        """
        if index == len(word):
            return True

        if (
            r < 0 or r >= len(self.grid) or
            c < 0 or c >= len(self.grid[0]) or
            visited[r][c]
        ):
            return False

        tile = self.grid[r][c]
        tile_len = len(tile)

        if word[index:index + tile_len] != tile:
            return False

        visited[r][c] = True

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    if self._dfs(r + dr, c + dc, word, index + tile_len, visited):
                        return True

        visited[r][c] = False
        return False


def main():
    """
    Main test driver.
    """
    grid = [
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["IE", "J", "K", "L"],
        ["A", "B", "C", "D"]
    ]

    dictionary = ["ABEF", "AFJIEEB", "DGKD", "DGKA"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
