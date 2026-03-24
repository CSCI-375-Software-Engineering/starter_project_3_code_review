class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary

    def getSolution(self):
        if not self._valid():
            return []

        rows = len(self.grid)
        cols = len(self.grid[0])
        prefixes = self._prefixes()
        found = set()

        for r in range(rows):
            for c in range(cols):
                self._dfs(r, c, "", set(), found, prefixes)

        return [w for w in self.dictionary if w.lower() in found]

    def _valid(self):
        if not isinstance(self.grid, list) or not self.grid:
            return False
        if not isinstance(self.dictionary, list):
            return False
        return True

    def _prefixes(self):
        p = set()
        for w in self.dictionary:
            w = w.lower()
            if len(w) >= 3:
                for i in range(1, len(w)+1):
                    p.add(w[:i])
        return p

    def _dfs(self, r, c, word, visited, found, prefixes):
        rows = len(self.grid)
        cols = len(self.grid[0])

        if (r, c) in visited:
            return

        tile = self.grid[r][c].lower()
        new_word = word + tile

        if new_word not in prefixes:
            return

        visited.add((r, c))

        if len(new_word) >= 3 and new_word in [w.lower() for w in self.dictionary]:
            found.add(new_word)

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    self._dfs(nr, nc, new_word, visited.copy(), found, prefixes)

