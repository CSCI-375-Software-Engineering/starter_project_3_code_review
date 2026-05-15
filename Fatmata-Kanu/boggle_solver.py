#Fatmata Kanu
#004001377


class Boggle:
    """Boggle solver which takes in a grid and dictionary
    and generates possible solutions."""

    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []

    def setDictionary(self, dictionary):
        self.dictionary = dictionary
        # updating dictionary and grid

    def setGrid(self, grid):
        self.grid = grid

    def getSolution(self):  # defining function to find solutions
        if not isinstance(self.dictionary, list) or not self.dictionary:
            # making sure dict is non-empty list
            return []
        for w in self.dictionary:
            if not isinstance(w, str) or not w:
                # checker for if a word is a string
                return []

        if not isinstance(self.grid, list) or not self.grid:
            # grid exists
            return []

        num = len(self.grid)  # size of the board

        for row in self.grid:
            if len(row) == 0:
                return []

        board = []  # making letters on the board lowercase
        for i in range(num):
            row = []
            for j in range(num):
                row.append(self.grid[i][j].lower())  # adding lowercase tile
            board.append(row)

        wordSet = set()
        for w in self.dictionary:
            w = w.lower()
            if len(w) >= 3:
                wordSet.add(w)

        if not wordSet:
            return []

        preSet = set()  # prefix set to eliminate bad searches head on
        for w in wordSet:
            for x in range(1, len(w) + 1):
                preSet.add(w[:x])

        found = set()

        already_visited = []  # tracking already visited tiles
        for _ in range(num):
            already_visited.append([False] * num)

        drs = [(-1, -1), (0, -1), (1, -1),
               (-1, 0),           (1, 0),
               (-1, 1),  (0, 1),  (1, 1)]  # all possible 8 directions

        def search(i, j, word):
            # moving through each tile that is not already used,
            # word is built and then reset to be used again
            if word not in preSet:
                return

            if word in wordSet:
                found.add(word)

            for row_change, column_change in drs:
                new_row_index = i + row_change
                new_column = j + column_change

                if (0 <= new_row_index < num
                        and 0 <= new_column < num
                        and not already_visited[new_row_index][new_column]):
                    already_visited[new_row_index][new_column] = True
                    search(new_row_index, new_column,
                           word + board[new_row_index][new_column])
                    already_visited[new_row_index][new_column] = False

        # search for every tile on the board
        for i in range(num):
            for j in range(num):
                already_visited[i][j] = True
                search(i, j, board[i][j])
                already_visited[i][j] = False

        self.solutions = sorted(list(found))
        return self.solutions


def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],
            ["G", "Z", "Qu", "R"], ["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt",
                  "prat", "pry", "qua", "quart", "quartz", "rat", "tar",
                  "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
