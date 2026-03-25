"""
Name: Abigail Aboah
SID: XXXXXXXX
"""

class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solution = []

    def setGrid(self, grid):
        self.grid = grid

    def setDictionary(self, dictionary):
        self.dictionary = dictionary

    def getSolution(self):
        if not self.grid or not self.dictionary:
            return []

        rows = len(self.grid)
        cols = len(self.grid[0])

        found_words = []

        for word in self.dictionary:
            word = word.upper()
            if len(word) >= 3 and self._exists(word, rows, cols):
                found_words.append(word)

        self.solution = found_words
        return found_words

    def _exists(self, word, rows, cols):
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if self._dfs(r, c, word, 0, visited):
                    return True
        return False

    def _dfs(self, r, c, word, index, visited):
        if index == len(word):
            return True

        if r < 0 or c < 0 or r >= len(self.grid) or c >= len(self.grid[0]):
            return False

        if visited[r][c]:
            return False

        cell = self.grid[r][c].upper()

        if not word.startswith(cell, index):
            return False

        visited[r][c] = True
        next_index = index + len(cell)

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    if self._dfs(r + dr, c + dc, word, next_index, visited):
                        visited[r][c] = False
                        return True

        visited[r][c] = False
        return False


def main():
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
    print(game.getSolution())


if __name__ == "__main__":
    main()
git checkout -b Abigail-Aboah-review
mkdir Abigail-LA
