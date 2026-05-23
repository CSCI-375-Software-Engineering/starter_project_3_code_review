class TrieNode:
    """Node in a Trie structure."""
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    """Trie (Prefix Tree) to efficiently store dictionary words."""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True


class Boggle:
    """Boggle game solver using Trie and DFS with backtracking."""

    def __init__(self, grid, dictionary, min_word_length=3):
        """
        Initialize the Boggle solver.

        grid: 2D list of strings representing tiles
        dictionary: list of words
        min_word_length: minimum valid word length (default 3)
        """
        self.min_word_length = min_word_length
        self.solution = []

        self.setGrid(grid)
        self.setDictionary(dictionary)

    # ----------------------------
    # Grid Handling
    # ----------------------------

    def setGrid(self, grid):
        """Set a new grid and validate it is rectangular."""
        if not grid or not all(isinstance(row, list) for row in grid):
            raise ValueError("Grid must be a non-empty 2D list.")

        row_length = len(grid[0])
        for row in grid:
            if len(row) != row_length:
                raise ValueError("Grid must be rectangular (all rows same length).")

        self.grid = grid
        self.rows = len(grid)
        self.cols = row_length

    # ----------------------------
    # Dictionary Handling
    # ----------------------------

    def _build_trie(self):
        """Build a Trie from the current dictionary."""
        self.trie = Trie()
        for word in self.dict_set:
            self.trie.insert(word)

    def setDictionary(self, dictionary):
        """Set a new dictionary and rebuild the Trie."""
        self.dictionary = dictionary
        self.dict_set = set(word.upper() for word in dictionary)
        self._build_trie()

    # ----------------------------
    # Solver
    # ----------------------------

    def getSolution(self):
        """Find all valid words in the grid and return them sorted."""
        if not self.grid or not self.dictionary:
            return []

        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        found_words = set()

        for r in range(self.rows):
            for c in range(self.cols):
                self._dfs(r, c, self.trie.root, "", visited, found_words)

        self.solution = sorted(found_words)
        return self.solution

    def _dfs(self, row, col, trie_node, current_word, visited, found_words):
        """Depth-First Search to explore all valid word paths."""

        # 1. Check bounds and visited
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return
        if visited[row][col]:
            return

        # 2. Get tile letters and handle special "Q" rule
        tile_letters = self._get_tile_letters(self.grid[row][col])

        # 3. Walk the Trie with tile letters
        current_node = trie_node
        for char in tile_letters:
            if char not in current_node.children:
                return
            current_node = current_node.children[char]

        # 4. Update current word and mark visited
        new_word = current_word + tile_letters
        visited[row][col] = True

        # 5. Add valid word
        if current_node.is_word and len(new_word) >= self.min_word_length:
            found_words.add(new_word)

        # 6. Explore all neighbors
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    self._dfs(row + dr, col + dc, current_node, new_word, visited, found_words)

        # 7. Backtrack
        visited[row][col] = False

    @staticmethod
    def _get_tile_letters(tile):
        """
        Convert a tile to uppercase letters.
        Handles the Boggle "Q" rule automatically.
        """
        tile = tile.upper()
        return "QU" if tile == "Q" else tile


# ----------------------------
# Example Usage
# ----------------------------

def main():
    grid = [
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["IE", "J", "K", "L"],
        ["A", "B", "C", "D"]
    ]

    dictionary = ["ABEF", "AFJIEEB", "DGKD", "DGKA"]

    solver = Boggle(grid, dictionary, min_word_length=3)
    solution = solver.getSolution()
    print(solution)


if __name__ == "__main__":
    main()