# Nigel Tendo
# 004002779

"""
Boggle Solver Module

This module solves Boggle puzzles using depth-first search (DFS) with
backtracking and prefix pruning optimization.
"""

# Minimum word length required in Boggle (extracted as constant per review)
MIN_WORD_LENGTH = 3

# 8-directional neighbor offsets (excluding center (0,0))
NEIGHBOR_DELTAS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]


class Boggle:
    """
    Solves Boggle puzzles using depth-first search with prefix pruning.

    The solver finds all valid words in a grid by exploring all possible
    paths and checking against a dictionary. It uses prefix pruning to
    optimize the search by stopping early when no dictionary word starts
    with the current path.
    """

    def __init__(self, grid, dictionary):
        """
        Initialize the Boggle solver with a grid and dictionary.

        Args:
            grid: 2D list of strings representing the game board
            dictionary: List of valid words to search for
        """
        # Store grid (will be validated in setGrid)
        self._grid = grid

        # Normalize dictionary: uppercase and strip whitespace
        self._dictionary = {
            word.strip().upper() for word in dictionary
            if isinstance(word, str) and word.strip().isalpha()
        }

        # Build prefix set for optimization
        self._prefixes = set()
        for word in self._dictionary:
            for i in range(1, len(word) + 1):
                self._prefixes.add(word[:i])

    def set_grid(self, grid):
        """
        Update the game grid.

        Args:
            grid: 2D list of strings representing the new game board

        Note:
            This method validates that the grid is rectangular (NxN).
            If validation fails, the grid remains unchanged.
        """
        # Validate grid is rectangular
        if not grid or not self._is_rectangular_grid(grid):
            return

        self._grid = grid

    def set_dictionary(self, dictionary):
        """
        Update the dictionary of valid words.

        Args:
            dictionary: List of valid words to search for

        Note:
            Words are automatically normalized to uppercase and filtered
            to contain only alphabetic characters.
        """
        # Filter and normalize: only alpha characters, strip whitespace
        self._dictionary = {
            word.strip().upper() for word in dictionary
            if isinstance(word, str) and word.strip().isalpha()
        }

        # Rebuild prefix set when dictionary changes
        self._prefixes = set()
        for word in self._dictionary:
            for i in range(1, len(word) + 1):
                self._prefixes.add(word[:i])

    def get_solution(self):
        """
        Find all valid words in the current grid.

        Returns:
            Sorted list of all valid words found in the grid

        Note:
            Returns empty list if grid is invalid or empty.
        """
        # Handle empty or invalid grid
        if not self._grid or not self._is_rectangular_grid(self._grid):
            return []

        found_words = set()
        rows = len(self._grid)
        cols = len(self._grid[0])

        # Start DFS from each position in the grid
        for row in range(rows):
            for col in range(cols):
                visited = [[False] * cols for _ in range(rows)]
                self._dfs(row, col, "", visited, found_words)

        return sorted(list(found_words))

    def _expand_tile(self, tile):
        """
        Convert tile to uppercase for uniform comparison.

        Args:
            tile: String representing a grid tile (e.g., "A", "Qu")

        Returns:
            Uppercase version of the tile

        Note:
            Handles special multi-letter tiles like "Qu" → "QU"
        """
        return tile.upper()

    def _dfs(self, row, col, current_word, visited, found_words):
        """
        Perform depth-first search to find valid words.

        This method explores all possible paths from the current position,
        using backtracking to try different combinations. It employs prefix
        pruning to optimize the search by stopping early when the current
        path cannot lead to a valid word.

        Args:
            row: Current row position
            col: Current column position
            current_word: Word built so far along the current path
            visited: 2D boolean array tracking visited cells in current path
            found_words: Set to accumulate discovered valid words
        """
        # Mark current cell as visited
        visited[row][col] = True

        # Expand the current tile and append to word
        current_letter = self._expand_tile(self._grid[row][col])
        current_word = current_word + current_letter

        # Early termination: stop if no dictionary word starts with this
        # This prefix pruning significantly reduces the search space
        if current_word not in self._prefixes:
            visited[row][col] = False
            return

        # Check if current word is valid (length >= 3 and in dictionary)
        if (len(current_word) >= MIN_WORD_LENGTH and
                current_word in self._dictionary):
            found_words.add(current_word)

        # Get grid dimensions
        rows = len(self._grid)
        cols = len(self._grid[0])

        # Explore all 8 neighboring cells
        for dr, dc in NEIGHBOR_DELTAS:
            new_row = row + dr
            new_col = col + dc

            # Check if neighbor is valid and unvisited
            if (self._in_bounds(new_row, new_col, rows, cols) and
                    not visited[new_row][new_col]):
                self._dfs(new_row, new_col, current_word, visited, found_words)

        # Backtrack: unmark current cell as visited
        visited[row][col] = False

    def _in_bounds(self, row, col, rows, cols):
        """
        Check if a position is within grid boundaries.

        Args:
            row: Row position to check
            col: Column position to check
            rows: Total number of rows in grid
            cols: Total number of columns in grid

        Returns:
            True if position is valid, False otherwise
        """
        return 0 <= row < rows and 0 <= col < cols

    def _is_rectangular_grid(self, grid):
        """
        Validate that grid is rectangular (all rows have same length).

        Args:
            grid: 2D list to validate

        Returns:
            True if grid is rectangular, False otherwise
        """
        if not grid:
            return False

        expected_length = len(grid[0])
        return all(len(row) == expected_length for row in grid)


def main():
    """
    Test the Boggle solver with sample data.
    """
    # Sample 4x4 grid with standard and special tiles
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]

    # Sample dictionary of valid words
    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt",
        "prat", "pry", "qua", "quart", "quartz", "rat", "tar",
        "tarp", "ten", "went", "wet", "arty", "not"
    ]

    # Create solver instance and find all valid words
    mygame = Boggle(grid, dictionary)
    print(mygame.get_solution())


if __name__ == "__main__":
    main()