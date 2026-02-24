"""
ALANA MARCIAL - original code for solver
004001996
"""

class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = [[cell.lower() for cell in row] for row in grid]
        self.dictionary = [word.lower() for word in dictionary]
        self.solution = []

    def setGrid(self, grid):
        self.grid = [[cell.lower() for cell in row] for row in grid]

    def setDictionary(self, dictionary):
        self.dictionary = [word.lower() for word in dictionary]

    def getSolution(self):
        if not self.grid or not self.dictionary:
          return []

        found = set()

        for word in self.dictionary:
          if len(word) < 3:
            continue
          if self._exist(word):
              found.add(word)

        self.solution = sorted(found)
        return self.solution

    def _exist(self, word):
        rows = len(self.grid)
        cols = len(self.grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if self._dfs(r, c, word, 0, visited):
                    return True
        return False

    def _dfs(self, r, c, word, index, visited):
        if index == len(word):
            return True

        if (
            r < 0 or c < 0 or
            r >= len(self.grid) or
            c >= len(self.grid[0]) or
            visited[r][c]

        ):
            return False

        tile = self.grid[r][c]
        tile_len = len(tile)

        if word[index:index + tile_len]  != tile:
            return False

        visited[r][c] = True

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    if self._dfs(r + dr, c + dc, word, index + tile_len, visited):
                        visited[r][c] = False
                        return True

        visited[r][c] = False
        return False


def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()