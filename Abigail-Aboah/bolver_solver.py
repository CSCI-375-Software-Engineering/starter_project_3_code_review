"""
Name: Abigail Aboah
SID: XXXXXXXX
"""

class Boggle:
    def __init__(self, grid=None, dictionary=None):
        """
        Initializes the Boggle game with a grid and a dictionary.
        """
        self.setGrid(grid)
        self.setDictionary(dictionary)

    def setGrid(self, grid):
        """
        Sets the grid and performs validation.
        Converts 'Q' to 'QU' and 'S' to 'ST' per Boggle rules.
        """
        # Check if the grid is empty or None
        if not grid or not any(grid):
            self.grid = []
            return

        # Normalize the grid: ensure 'Q' -> 'QU' and 'S' -> 'ST'
        # and convert all to uppercase for consistency.
        normalized_grid = []
        for row in grid:
            new_row = []
            for cell in row:
                cell_upper = cell.upper()
                if cell_upper == "Q":
                    new_row.append("QU")
                elif cell_upper == "S":
                    new_row.append("ST")
                else:
                    new_row.append(cell_upper)
            normalized_grid.append(new_row)
        
        self.grid = normalized_grid

    def setDictionary(self, dictionary):
        """
        Sets the dictionary and checks if it is empty.
        """
        if not dictionary:
            self.dictionary = []
        else:
            # Store dictionary in uppercase for easier comparison
            self.dictionary = [word.upper() for word in dictionary]

    def getSolution(self):
        """
        Finds all valid words from the dictionary present in the grid.
        """
        if not self.grid or not self.dictionary:
            return []

        rows = len(self.grid)
        cols = len(self.grid[0])
        found_words = []

        # Iterate through the dictionary to check each word's existence in the grid
        for word in self.dictionary:
            # Words must be at least 3 characters long per standard rules
            if len(word) >= 3 and self._exists(word, rows, cols):
                found_words.append(word)

        # Removed redundant self.solution assignment as per reviewer suggestion
        return found_words

    def _exists(self, word, rows, cols):
        """
        Starts a DFS search for a word from every cell in the grid.
        """
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if self._dfs(r, c, word, 0, visited):
                    return True
        return False

    def _dfs(self, r, c, word, index, visited):
        """
        Recursive Depth First Search to find the word path in the grid.
        Handles multi-character cells (like QU or ST).
        """
        # Base Case: Entire word has been found
        if index == len(word):
            return True

        # Boundary and visited checks
        if r < 0 or c < 0 or r >= len(self.grid) or c >= len(self.grid[0]) or visited[r][c]:
            return False

        cell = self.grid[r][c]

        # Check if the current cell matches the current part of the word
        if not word.startswith(cell, index):
            return False

        # Mark cell as visited
        visited[r][c] = True
        
        # Advance index by the length of the cell (handles 1 or 2 character cells)
        next_index = index + len(cell)

        # Explore all 8 adjacent directions
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    if self._dfs(r + dr, c + dc, word, next_index, visited):
                        # Backtrack before returning True
                        visited[r][c] = False
                        return True

        # Backtrack: unmark cell for other search paths
        visited[r][c] = False
        return False


def main():
    # Example grid with mixed cases and special rules
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "St", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]

    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt",
        "prat", "pry", "qua", "quart", "rat", "tar",
        "tarp", "ten", "went", "wet", "arty", "not"
    ]

    game = Boggle(grid, dictionary)
    print("Found words:", game.getSolution())


if __name__ == "__main__":
    main()
