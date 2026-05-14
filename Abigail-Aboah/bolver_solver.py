"""
Name: Abigail Aboah
SID: XXXXXXXX
"""


class Boggle:
    """
    A class to solve a Boggle board given a specific grid and dictionary.
    """

    def __init__(self, grid=None, dictionary=None):
        """
        Initializes the Boggle game.
        """
        self.grid = []
        self.dictionary = []
        
        if grid:
            self.set_grid(grid)
        if dictionary:
            self.set_dictionary(dictionary)

    def set_grid(self, grid):
        """
        Validates and normalizes the grid. Converts 'Q' to 'QU' 
        and 'S' to 'ST' per standard Boggle rules.
        """
        if not grid or not any(grid):
            self.grid = []
            return

        # Use a mapping for special Boggle rules to improve readability
        special_rules = {"Q": "QU", "S": "ST"}

        self.grid = [
            [special_rules.get(cell.upper(), cell.upper()) for cell in row]
            for row in grid
        ]

    def set_dictionary(self, dictionary):
        """
        Normalizes the dictionary to uppercase for consistent matching.
        """
        if not dictionary:
            self.dictionary = []
        else:
            self.dictionary = [word.upper() for word in dictionary]

    def get_solution(self):
        """
        Returns a list of valid words found in the grid.
        """
        if not self.grid or not self.dictionary:
            return []

        rows = len(self.grid)
        cols = len(self.grid[0])
        found_words = []

        for word in self.dictionary:
            # Only process words that meet the minimum length requirement
            if len(word) >= 3 and self._exists(word, rows, cols):
                found_words.append(word)

        return found_words

    def _exists(self, word, rows, cols):
        """
        Iterates through the grid to find a starting point for the word.
        """
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if self._dfs(r, c, word, 0, visited):
                    return True
        return False

    def _dfs(self, r, c, word, index, visited):
        """
        Recursive search to match the word characters against the grid.
        """
        if index == len(word):
            return True

        # Check bounds and if cell is already used in current path
        if (r < 0 or r >= len(self.grid) or 
                c < 0 or c >= len(self.grid[0]) or 
                visited[r][c]):
            return False

        current_cell = self.grid[r][c]

        # Early exit if the current cell doesn't match the word segment
        if not word.startswith(current_cell, index):
            return False

        visited[r][c] = True
        next_index = index + len(current_cell)

        # Explore all 8 neighbors (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                
                if self._dfs(r + dr, c + dc, word, next_index, visited):
                    visited[r][c] = False  # Backtrack
                    return True

        visited[r][c] = False  # Backtrack
        return False


def main():
    """
    Entry point for the Boggle solver script.
    """
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
    print(f"Found words: {game.get_solution()}")


if __name__ == "__main__":
    main()
