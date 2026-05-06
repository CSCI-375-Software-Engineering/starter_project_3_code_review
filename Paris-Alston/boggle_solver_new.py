"""
Paris Alston
SID: 03102195
"""


class Boggle:
    """
    Boggle word solver using DFS + prefix pruning.
    """

    MIN_WORD_LENGTH = 3

    # All 8 neighboring directions
    DIRECTIONS = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    def __init__(self, grid, dictionary):
        """
        grid: expected to be an NxN board of strings
        dictionary: list of valid words
        """
        self.grid = grid
        self.dictionary = dictionary
        self.solution = []

        # Sets allow fast O(1) lookup
        self.word_set = set()
        self.prefix_set = set()

        self.size = 0

    def setGrid(self, grid):
        self.grid = grid

    def setDictionary(self, dictionary):
        self.dictionary = dictionary

    def getSolution(self):
        """
        Returns a sorted list of valid words found in the grid.
        Returns [] if grid or dictionary is invalid.
        """
        if not self._validGrid() or not self._validDictionary():
            return []

        self.size = len(self.grid)
        self.solution = []

        self._buildDictionaries()

        found = set()

        for r in range(self.size):
            for c in range(self.size):
                visited = self._makeVisited()
                self._dfs(r, c, "", visited, found)

        result = sorted(found)

        self.solution = result

        return result

    def _validGrid(self):
        """
        Grid must be:
        - non-empty
        - NxN
        - contain non-empty strings
        """
        if not isinstance(self.grid, list) or len(self.grid) == 0:
            return False

        n = len(self.grid)

        for row in self.grid:
            if not isinstance(row, list) or len(row) != n:
                return False

            for cell in row:
                if not isinstance(cell, str) or cell.strip() == "":
                    return False

        return True

    def _validDictionary(self):
        """
        Dictionary must be a list of non-empty strings.
        """
        if not isinstance(self.dictionary, list):
            return False

        for word in self.dictionary:
            if not isinstance(word, str) or word.strip() == "":
                return False

        return True

    def _buildDictionaries(self):
        """
        Converts all words to uppercase for consistency.

        word_set:
            Fast full-word lookup

        prefix_set:
            Stores all prefixes so DFS can stop early
            when a path cannot possibly form a word.
        """
        self.word_set = set()
        self.prefix_set = set()

        for word in self.dictionary:
            w = word.upper()

            self.word_set.add(w)

            for i in range(1, len(w) + 1):
                self.prefix_set.add(w[:i])

    def _dfs(self, r, c, current, visited, found):
        """
        Depth-first search with backtracking.
        """

        if visited[r][c]:
            return

        current += self.grid[r][c].upper()

        # Performance optimization:
        # stop exploring paths that are not valid prefixes
        if current not in self.prefix_set:
            return

        visited[r][c] = True

        # Valid Boggle word check
        if (
            len(current) >= self.MIN_WORD_LENGTH
            and current in self.word_set
        ):
            found.add(current)

        # Explore all 8 neighboring directions
        for dr, dc in self.DIRECTIONS:
            nr = r + dr
            nc = c + dc

            if self._inBounds(nr, nc) and not visited[nr][nc]:
                self._dfs(nr, nc, current, visited, found)

        # Backtrack
        visited[r][c] = False

    def _inBounds(self, r, c):
        return 0 <= r < self.size and 0 <= c < self.size

    def _makeVisited(self):
        """
        Creates a visited matrix initialized to False.
        """
        return [
            [False for _ in range(self.size)]
            for _ in range(self.size)
        ]


def run_test(name, grid, dictionary, expected):
    game = Boggle(grid, dictionary)

    result = game.getSolution()

    result.sort()
    expected.sort()

    if result == expected:
        print("PASS:", name)
    else:
        print("FAIL:", name)
        print("Expected:", expected)
        print("Got     :", result)


def run_all_tests():
    # Diagonal + adjacency
    run_test(
        "Diagonal adjacency",
        [["A", "B"], ["C", "D"]],
        ["ABC", "ABD", "ACB", "DCA"],
        ["ABC", "ABD", "ACB", "DCA"]
    )

    # No tile reuse
    run_test(
        "No tile reuse",
        [["A", "A"], ["A", "A"]],
        ["AAA", "AAAA", "AAAAA"],
        ["AAA", "AAAA"]
    )

    # Qu tile
    run_test(
        "Qu tile",
        [["Qu", "A"], ["R", "T"]],
        ["QUA", "QUART", "QU"],
        ["QUA", "QUART"]
    )

    # St tile
    run_test(
        "St tile",
        [["St", "O", "P"], ["A", "R", "T"], ["X", "Y", "Z"]],
        ["STOP", "STO", "ST"],
        ["STOP", "STO"]
    )

    # IE tile
    run_test(
        "IE tile",
        [["A", "B", "C"], ["D", "H", "X"], ["Y", "IE", "Z"]],
        ["ABC", "ABDHIE"],
        ["ABC", "ABDHIE"]
    )


def main():
    run_all_tests()

    print("\nExample board solution:")

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

    boggle_game = Boggle(grid, dictionary)

    print(boggle_game.getSolution())


if __name__ == "__main__":
    main()
