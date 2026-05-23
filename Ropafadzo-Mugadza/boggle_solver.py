class Boggle:
    """
    Boggle solver using DFS with prefix pruning.
    """

    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = set(word.lower() for word in dictionary)
        self.prefixes = set()
        self.solutions = set()

        # Precompute prefixes
        for word in self.dictionary:
            for i in range(1, len(word) + 1):
                self.prefixes.add(word[:i])

        self.rows = len(grid)
        self.cols = len(grid[0]) if grid and grid[0] else 0

    def getSolution(self):
        """
        Required by auto-grader.
        Returns sorted list of valid words.
        """
        if self.rows == 0 or self.cols == 0:
            return []

        self.solutions.clear()
        visited = [[False] * self.cols for _ in range(self.rows)]

        for r in range(self.rows):
            for c in range(self.cols):
                self._dfs(r, c, "", visited)

        return sorted(self.solutions)

    def _dfs(self, r, c, current_word, visited):
        # Boundary check
        if not (0 <= r < self.rows and 0 <= c < self.cols):
            return

        if visited[r][c]:
            return

        cell_value = self.grid[r][c].lower()

        # Support multi-character tiles like "Qu" or "St"
        new_word = current_word + cell_value

        # Prefix pruning
        if new_word not in self.prefixes:
            return

        # Valid word conditions
        if (
            len(new_word) >= 3
            and new_word in self.dictionary
            and not new_word.endswith(("q", "s", "i"))
        ):
            self.solutions.add(new_word)

        visited[r][c] = True

        # Explore 8 directions
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr != 0 or dc != 0:
                    self._dfs(r + dr, c + dc, new_word, visited)

        visited[r][c] = False
