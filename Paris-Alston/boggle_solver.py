
"""
Paris Alston
SID: 03102195
"""

class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solution = []

        self.word_dict = {}
        self.prefix_dict = {}
        self.size = 0

    def setGrid(self, grid):
        self.grid = grid

    def setDictionary(self, dictionary):
        self.dictionary = dictionary

    def getSolution(self):
        """
        Returns a list of valid words found in the grid.
        Returns [] if grid or dictionary is invalid.
        """
        if (not self._validGrid()) or (not self._validDictionary()):
            return []

        self.size = len(self.grid)
        self.solution = []

        self._buildDictionaries()

        found = {}

        for r in range(self.size):
            for c in range(self.size):
                visited = self._makeVisited()
                self._dfs(r, c, "", visited, found)

        result = list(found.keys())
        result.sort()
        self.solution = result
        return result

    

    def _validGrid(self):
        # must be a non-empty NxN list of strings
        if type(self.grid) is not list or len(self.grid) == 0:
            return False

        n = len(self.grid)

        for row in self.grid:
            if type(row) is not list or len(row) != n:
                return False

            for cell in row:
                if type(cell) is not str or cell.strip() == "":
                    return False

        return True  

    def _validDictionary(self):
        if type(self.dictionary) is not list:
            return False

        for word in self.dictionary:
            if type(word) is not str or word.strip() == "":
                return False

        return True

    def _buildDictionaries(self):
        self.word_dict = {}
        self.prefix_dict = {}

        for word in self.dictionary:
            w = word.upper()
            self.word_dict[w] = True

            for i in range(1, len(w) + 1):
                self.prefix_dict[w[:i]] = True

    def _dfs(self, r, c, current, visited, found):
        if visited[r][c]:
            return

        current = current + self.grid[r][c].upper()

        # prefix pruning
        if current not in self.prefix_dict:
            return

        visited[r][c] = True

        # full word check (>= 3 letters)
        if len(current) >= 3 and current in self.word_dict:
            found[current] = True

        # explore neighbors (8 directions)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    nr = r + dr
                    nc = c + dc
                    if self._inBounds(nr, nc) and not visited[nr][nc]:
                        self._dfs(nr, nc, current, visited, found)

        visited[r][c] = False  

    def _inBounds(self, r, c):
        return 0 <= r < self.size and 0 <= c < self.size

    def _makeVisited(self):
        visited = []
        for _ in range(self.size):
            visited.append([False] * self.size)
        return visited



def run_test(name, grid, dictionary, expected):
    game = Boggle(grid, dictionary)
    result = game.getSolution()
    result.sort()
    expected.sort()

    if result == expected:
        print("PASS:", name)
    else:
        print("FAIL:", name)
        print(" Expected:", expected)
        print(" Got     :", result)


def main():
    # Diagonal + adjacency
    run_test(
        "Diagonal adjacency",
        [["A","B"],["C","D"]],
        ["ABC", "ABD", "ACB", "DCA"],
        ["ABC", "ABD", "ACB", "DCA"]
    )

    # No tile reuse
    run_test(
        "No tile reuse",
        [["A","A"],["A","A"]],
        ["AAA", "AAAA", "AAAAA"],
        ["AAA", "AAAA"]
    )

    # Qu tile
    run_test(
        "Qu tile",
        [["Qu","A"],["R","T"]],
        ["QUA", "QUART", "QU"],
        ["QUA", "QUART"]
    )

    # St tile
    run_test(
        "St tile",
        [["St","O","P"],["A","R","T"],["X","Y","Z"]],
        ["STOP", "STO", "ST"],
        ["STOP", "STO"]
    )

    # IE tile
    run_test(
        "IE tile",
        [["A","B","C"],["D","H","X"],["Y","IE","Z"]],
        ["ABC", "ABDHIE"],
        ["ABC", "ABDHIE"]
    )












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
        "tar", "tarp", "ten", "went", "wet", "arty", "not"
    ]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()    main()