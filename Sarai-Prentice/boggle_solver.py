"""
NAME: Sarai Prentice
SID: YOUR_SID_HERE
"""

class Boggle:
    # Initialize the Boggle game with a grid and a dictionary
    def __init__(self, grid, dictionary):
        self.grid = []          # 2D list of letter tiles
        self.dictionary = []    # list of dictionary words
        self.solution = []      # list of found words

        self.words = set()      # dictionary words for fast lookup
        self.prefixes = set()   # prefixes for pruning DFS

        self.setGrid(grid)
        self.setDictionary(dictionary)

    # Set and validate the grid
    def setGrid(self, grid):
        # Grid must be a non-empty 2D list
        if type(grid) is not list or not grid or type(grid[0]) is not list:
            self.grid = []
            return

        cols = len(grid[0])
        for row in grid:
            # All rows must have same length
            if type(row) is not list or len(row) != cols:
                self.grid = []
                return

        # Store grid as lowercase strings
        self.grid = [[str(tile).lower() for tile in row] for row in grid]

    # Set the dictionary and build prefix set
    def setDictionary(self, dictionary):
        # Dictionary must be a list
        if type(dictionary) is not list:
            self.dictionary = []
            return

        # Store dictionary as lowercase words
        self.dictionary = [str(word).lower() for word in dictionary]
        self.words = set(self.dictionary)

        # Build prefix set for pruning
        self.prefixes = set()
        for word in self.words:
            for i in range(1, len(word) + 1):
                self.prefixes.add(word[:i])

    # Find and return all valid words in the grid
    def getSolution(self):
        # Return empty list if grid or dictionary is invalid
        if not self.grid or not self.dictionary:
            self.solution = []
            return []

        rows = len(self.grid)
        cols = len(self.grid[0])

        used = [[False] * cols for _ in range(rows)]  # track used tiles
        found = set()                                 # found words

        # Depth-first search from position (r, c)
        def dfs(r, c, current):
            if used[r][c]:
                return

            # Append current tile ("qu", "st", "ie" count as 2 letters)
            current += self.grid[r][c]

            # Stop if current string is not a valid prefix
            if current not in self.prefixes:
                return

            # Save word if valid and long enough
            if len(current) >= 3 and current in self.words:
                found.add(current)

            used[r][c] = True

            # Explore all 8 neighboring tiles
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr != 0 or dc != 0:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            dfs(nr, nc, current)

            used[r][c] = False  # backtrack

        # Start DFS from every tile
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, "")

        # Store and return sorted solution
        self.solution = sorted(found)
        return self.solution


# Main function required by assignment
def main():
    grid = [["A", "B", "C", "D"],
            ["E", "F", "G", "H"],
            ["IE", "J", "K", "L"],
            ["A", "B", "C", "D"]]

    dictionary = ["ABEF", "AFJIEEB", "DGKD", "DGKA"]

    game = Boggle(grid, dictionary)
    print(game.getSolution())


# Run main when executed from terminal
if __name__ == "__main__":
    main()
