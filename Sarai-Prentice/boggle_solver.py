"""
NAME: Sarai Prentice
SID: @03136144
"""


class Boggle:
    """
    Solve a Boggle board using depth-first search and prefix pruning.

    The solver starts from every tile on the board, builds words by moving
    to adjacent tiles in any of the 8 directions, and stops exploring paths
    that are not valid prefixes of dictionary words.
    """

    MIN_WORD_LENGTH = 3

    def __init__(self, grid, dictionary):
        """Initialize the Boggle game with a grid and dictionary."""
        self.grid = []              # 2D list of letter tiles
        self.dictionary = []        # Original dictionary as a list
        self.found_words = []       # Final sorted list of discovered words

        # words is a set for fast membership checks during the search.
        self.words = set()

        # prefixes stores every valid word prefix to prune DFS early.
        self.prefixes = set()

        self.setGrid(grid)
        self.setDictionary(dictionary)

    def setGrid(self, grid):
        """Validate the grid and store it as lowercase strings."""
        # Grid must be a non-empty 2D list.
        if (
    not isinstance(grid, list)
    or not grid
    or not isinstance(grid[0], list)
):
            # Invalid grid input is stored as an empty list.
            self.grid = []
            return

        cols = len(grid[0])

        for row in grid:
            # All rows must be lists of the same length so the board
            # forms a proper rectangle.
            if not isinstance(row, list) or len(row) != cols:
                # If the grid is invalid, reset it to an empty list.
                self.grid = []
                return

        # Convert all tiles to lowercase strings so grid values match
        # lowercase dictionary words consistently.
        self.grid = [[str(tile).lower() for tile in row] for row in grid]

    def setDictionary(self, dictionary):
        """Validate the dictionary and build the prefix set."""
        if not isinstance(dictionary, list):
            self.dictionary = []
            return

        # Store dictionary words as lowercase strings for consistency.
        self.dictionary = [str(word).lower() for word in dictionary]
        self.words = set(self.dictionary)

        # Build a prefix set so DFS can stop exploring invalid paths early.
        self.prefixes = set()
        for word in self.words:
            for i in range(1, len(word) + 1):
                self.prefixes.add(word[:i])

    def in_bounds(self, row, col, rows, cols):
        """Return True if the position is inside the board."""
        return 0 <= row < rows and 0 <= col < cols

    def getSolution(self):
        """Find and return all valid words in the grid."""
        # If the grid or dictionary is invalid/empty, return no solution.
        if not self.grid or not self.dictionary:
            self.found_words = []
            return []

        rows = len(self.grid)
        cols = len(self.grid[0])

        # used tracks which tiles are already in the current search path,
        # which prevents reusing the same tile in one word.
        used = [[False] * cols for _ in range(rows)]
        found = set()

        def dfs(row, col, current):
            """Explore all valid words starting from one board position."""
            if used[row][col]:
                return

            # Add the current tile to the growing word.
            # Special tiles such as "qu", "st", and "ie" count as 2 letters.
            current += self.grid[row][col]

            # Prefix pruning: stop immediately if no dictionary word begins
            # with the current string.
            if current not in self.prefixes:
                return

            # Save the word if it is in the dictionary and long enough.
            if len(current) >= self.MIN_WORD_LENGTH and current in self.words:
                found.add(current)

            used[row][col] = True

            # Explore all 8 neighboring tiles (horizontal, vertical,
            # and diagonal), which matches Boggle rules.
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr != 0 or dc != 0:
                        next_row = row + dr
                        next_col = col + dc

                        if self.in_bounds(next_row, next_col, rows, cols):
                            dfs(next_row, next_col, current)

            # Backtrack so this tile can be used in a different search path.
            used[row][col] = False

        # Start a DFS from every tile so all possible words are considered.
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, "")

        # Sort results for consistent output order.
        self.found_words = sorted(found)
        return self.found_words


def main():
    """Run a few example test cases."""
    grid1 = [
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["IE", "J", "K", "L"],
        ["A", "B", "C", "D"]
    ]
    dictionary1 = ["ABEF", "AFJIEEB", "DGKD", "DGKA"]

    game1 = Boggle(grid1, dictionary1)
    print("Example 1:", game1.getSolution())

    grid2 = [
        ["Qu", "A"],
        ["T", "S"]
    ]
    dictionary2 = ["QUA", "QUAT", "SAT"]

    game2 = Boggle(grid2, dictionary2)
    print("Example 2:", game2.getSolution())

    grid3 = []
    dictionary3 = ["CAT", "DOG"]

    game3 = Boggle(grid3, dictionary3)
    print("Example 3:", game3.getSolution())


if __name__ == "__main__":
    main()
