"""
Chris Pozo Hernandez
SID: 004003215
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
        """Return all valid words found in the Boggle grid."""
        if not self.grid or not self.dictionary:
            return []

        rows = len(self.grid)
        cols = len(self.grid[0])

        words = [w.upper() for w in self.dictionary]

        found = set()

        for r in range(rows):
            for c in range(cols):
                self._dfs(r, c, "", set(), found, words)

        self.solution = [w for w in found if len(w) >= 3]
        return self.solution

    def _dfs(self, row, col, current, visited, found, words):
        rows = len(self.grid)
        cols = len(self.grid[0])

        if (row, col) in visited:
            return

        tile = self.grid[row][col].upper()
        if tile == "Q":
            tile = "QU"

        new_word = current + tile

        if not any(w.startswith(new_word) for w in words):
            return

        if new_word in words:
            found.add(new_word)

        visited.add((row, col))

        # Explore neighbors (in all 8 directions)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    new_r = row + dr
                    new_c = col + dc
                    # split bounds to avoid long line
                    row_ok = 0 <= new_r < rows
                    col_ok = 0 <= new_c < cols
                    if row_ok and col_ok:
                        self._dfs(
                            new_r,
                            new_c,
                            new_word,
                            visited,
                            found,
                            words
                        )

        visited.remove((row, col))


def main():
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]

    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt",
        "prat", "pry", "qua", "quart", "quartz", "rat",
        "tar", "tarp", "ten", "went", "wet", "arty",
        "rhr", "not", "quar"
    ]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
