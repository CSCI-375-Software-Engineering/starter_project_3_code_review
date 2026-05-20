#Tahmauri Bobo @03134060

class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = [w.lower() for w in dictionary]
        self.solutions = []

    def getSolution(self):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                self._dfs(r, c, "", [])
        return sorted(self.solutions)

    def _dfs(self, r, c, word, path):
        if (r, c) in path:
            return

        word += self.grid[r][c].lower()

        if not self.isPrefix(word):
            return

        if len(word) >= 3 and word in self.dictionary and word not in self.solutions:
            self.solutions.append(word)

        path.append((r, c))

        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[0]):
                    self._dfs(nr, nc, word, path)

        path.pop()

    def isPrefix(self, word):
        for w in self.dictionary:
            if w.startswith(word):
                return True
        return False


def main():
    grid = [
        ["T", "W", "Y", "R"], 
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]

    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"
    ]

    game = Boggle(grid, dictionary)
    print(game.getSolution())


if __name__ == "__main__":
    main()
