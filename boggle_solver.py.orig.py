"""
NAME: [Your Name Here]
SID: [Your Student ID Here]

Boggle Solver Implementation
This module implements a solver for the Boggle word-finding game.
"""


class Boggle:
    """
    A class to solve Boggle puzzles.
    
    The Boggle game involves finding words in an NxN grid of letters where:
    - Words must use adjacent tiles (including diagonals)
    - Each tile can only be used once per word
    - Words must be at least 3 letters long
    - Special tiles: "Qu", "St", "Ie" count as 2 letters each
    """
    
    def __init__(self, grid, dictionary):
        """
        Initialize the Boggle solver with a grid and dictionary.
        
        Args:
            grid: 2D array of strings representing the letter grid
            dictionary: List of valid words to search for
        """
        self.grid = None
        self.dictionary = None
        self.solution_set = set()
        
        self.setGrid(grid)
        self.setDictionary(dictionary)
        
        # If both grid and dictionary are valid, solve the puzzle
        if self.grid is not None and self.dictionary is not None:
            self._solve()
    
    def setGrid(self, grid):
        """
        Set and validate the grid.
        
        Args:
            grid: 2D array of strings representing the letter grid
        """
        if not self._validate_grid(grid):
            self.grid = None
            return
        
        # Normalize the grid: convert all to uppercase
        self.grid = []
        for row in grid:
            normalized_row = []
            for cell in row:
                normalized_row.append(cell.upper())
            self.grid.append(normalized_row)
    
    def setDictionary(self, dictionary):
        """
        Set and validate the dictionary.
        
        Args:
            dictionary: List of valid words
        """
        if not self._validate_dictionary(dictionary):
            self.dictionary = None
            return
        
        # Normalize dictionary: convert all to uppercase and store in a set for O(1) lookup
        self.dictionary = set()
        for word in dictionary:
            if isinstance(word, str):
                self.dictionary.add(word.upper())
    
    def getSolution(self):
        """
        Get the solution to the Boggle puzzle.
        
        Returns:
            List of found words, or empty list if no words found or if there was an error
        """
        if self.grid is None or self.dictionary is None:
            return []
        
        return sorted(list(self.solution_set))
    
    def _validate_grid(self, grid):
        """
        Validate that the grid is a proper 2D array.
        
        Args:
            grid: The grid to validate
            
        Returns:
            True if valid, False otherwise
        """
        if not grid or not isinstance(grid, list):
            return False
        
        if len(grid) == 0:
            return False
        
        # Check that all rows are lists and have the same length
        row_length = len(grid[0])
        for row in grid:
            if not isinstance(row, list) or len(row) != row_length:
                return False
            # Check that all cells are strings
            for cell in row:
                if not isinstance(cell, str):
                    return False
        
        return True
    
    def _validate_dictionary(self, dictionary):
        """
        Validate that the dictionary is a proper list of strings.
        
        Args:
            dictionary: The dictionary to validate
            
        Returns:
            True if valid, False otherwise
        """
        if not isinstance(dictionary, list):
            return False
        
        return True
    
    def _solve(self):
        """
        Solve the Boggle puzzle by searching for all dictionary words in the grid.
        """
        if not self.grid or not self.dictionary:
            return
        
        rows = len(self.grid)
        cols = len(self.grid[0]) if rows > 0 else 0
        
        # Build a set of all possible prefixes from the dictionary for pruning
        self.prefixes = set()
        for word in self.dictionary:
            for i in range(1, len(word) + 1):
                self.prefixes.add(word[:i])
        
        # Try starting from each position in the grid
        for i in range(rows):
            for j in range(cols):
                visited = [[False] * cols for _ in range(rows)]
                self._dfs(i, j, "", visited)
    
    def _dfs(self, row, col, current_word, visited):
        """
        Depth-first search to find words starting from a given position.
        
        Args:
            row: Current row position
            col: Current column position
            current_word: The word built so far
            visited: 2D boolean array tracking visited cells
        """
        rows = len(self.grid)
        cols = len(self.grid[0])
        
        # Check bounds
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        
        # Check if already visited
        if visited[row][col]:
            return
        
        # Add current cell to the word
        cell_value = self.grid[row][col]
        new_word = current_word + cell_value
        
        # PRUNING: If this word is not a prefix of any dictionary word, stop exploring
        if new_word not in self.prefixes:
            return
        
        # Mark as visited
        visited[row][col] = True
        
        # Check if this word is in the dictionary and meets minimum length
        word_length = self._get_word_length(new_word)
        if word_length >= 3 and new_word in self.dictionary:
            self.solution_set.add(new_word)
        
        # Explore all 8 adjacent cells (including diagonals)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Top-left, top, top-right
            (0, -1),           (0, 1),    # Left, right
            (1, -1),  (1, 0),  (1, 1)     # Bottom-left, bottom, bottom-right
        ]
        
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            self._dfs(new_row, new_col, new_word, visited)
        
        # Backtrack: unmark as visited
        visited[row][col] = False
    
    def _get_word_length(self, word):
        """
        Calculate the actual length of a word, accounting for special tiles.
        
        Special tiles that count as 2 letters:
        - "QU" (representing the Qu tile)
        - "ST" (representing the St tile)
        - "IE" (representing the Ie tile)
        
        Args:
            word: The word to measure
            
        Returns:
            The actual length of the word
        """
        length = 0
        i = 0
        while i < len(word):
            # Check for two-letter tiles
            if i + 1 < len(word):
                two_char = word[i:i+2]
                if two_char in ["QU", "ST", "IE"]:
                    length += 2
                    i += 2
                    continue
            # Single letter
            length += 1
            i += 1
        
        return length


def main():
    """
    Main function to demonstrate the Boggle solver.
    """
    grid = [["A", "B", "C", "D"],
            ["E", "F", "G", "H"], 
            ["IE", "J", "K", "L"], 
            ["A", "B", "C", "D"]]

    dictionary = ["ABEF", "AFJIEEB", "DGKD", "DGKA"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
