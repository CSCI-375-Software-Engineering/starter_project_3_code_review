
class Boggle:
    """
    Boggle game solver class.
    """

    def __init__(self, grid, dictionary):
        """
        Constructor for the Boggle class.

        grid: 2D list of strings
        dictionary: list of words
        """
        self.grid = grid
        self.dictionary = dictionary
        self.solution = []

        # making dictionary uppercase sensitive and putting it in a hash table
        self.dict_set = set(word.upper() for word in dictionary)

        # store all prefix's of words in, helps place and discontinue invalid search paths
        self.prefix_set = set()
        for word in self.dict_set:
            for i in range(1, len(word) + 1):
                self.prefix_set.add(word[:i])

        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def setGrid(self, grid):
        """
        Setter for the grid.
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def setDictionary(self, dictionary):
        """
        Setter for the dictionary.
        """
        self.dictionary = dictionary
        self.dict_set = set(word.upper() for word in dictionary)

    def getSolution(self):
        """
        Finds and returns all valid words in the grid.
        """
        if not self.grid or not self.dictionary:
            return []

        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        found_words = set()

        for r in range(self.rows):
            for c in range(self.cols):
                self._dfs(r, c, "", visited, found_words)

        self.solution = sorted(found_words)
        return self.solution   # turn set of found words into a sorted list then return it

    def _dfs(self, row, col, current_word, visited, found_words):
        # functions moves through the board to make words

        # checks to see if tile is inside the bound and to see if tile has been used already
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return
        if visited[row][col]:
            return

        # add current tile to letter (handles Qu, St, Ie automatically)
        current_word += self.grid[row][col].upper()

        # stops checking if not a valid prefix
        if current_word not in self.prefix_set:
            return

        visited[row][col] = True     #marks the tile or piece on the board as visited' 

        # checks if valid dictionary word (at least 3 letters and is in dict)
        if len(current_word) >= 3 and current_word in self.dict_set:
            found_words.add(current_word)

        # explores the different directions words can e formed and goes thru it
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    self._dfs(row + dr, col + dc, current_word, visited, found_words)

        # unmarking the tile so it can potentially be used in another word
        visited[row][col] = False


def main():
    grid = [
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["IE", "J", "K", "L"],
        ["A", "B", "C", "D"]
    ]

    dictionary = ["ABEF", "AFJIEEB", "DGKD", "DGKA"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
