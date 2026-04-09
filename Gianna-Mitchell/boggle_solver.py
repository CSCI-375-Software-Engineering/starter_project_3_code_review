class Boggle:
    def __init__(self, grid, dictionary):
        self.solutions = set()
        self.set_grid(grid)
        self.set_dictionary(dictionary)

    def set_grid(self, grid):
        self.grid = []
        for row in grid:
            clean_row = [tile.upper() for tile in row]
            self.grid.append(clean_row)

    def set_dictionary(self, dictionary):
        self.dictionary = set()
        for word in dictionary:
            word = word.upper()
            if len(word) >= 3 and word.isalpha():
                self.dictionary.add(word)

    def find_words(self, word, row, col, index, visited):
        if row < 0 or row >= len(self.grid) or \
           col < 0 or col >= len(self.grid[0]):
            return

        if (row, col) in visited:
            return

        tile = self.grid[row][col]

        if word[index: index + len(tile)] == tile:
            new_index = index + len(tile)
            if new_index == len(word):
                self.solutions.add(word)
                return

            visited.add((row, col))
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    self.find_words(word, row + dr, col + dc,
                                    new_index, visited)
            visited.remove((row, col))

    def getSolution(self):
        if not self.grid or not self.dictionary:
            return []
        self.solutions = set()
        for word in self.dictionary:
            for r in range(len(self.grid)):
                for c in range(len(self.grid[0])):
                    self.find_words(word, r, c, 0, set())
        return sorted(list(self.solutions))


def main():
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]
    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt", "prat",
        "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten",
        "went", "wet", "arty", "rhr", "not", "quar"
    ]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
# Final submission update - April 9
