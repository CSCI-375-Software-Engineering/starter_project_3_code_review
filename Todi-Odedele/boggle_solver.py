class Boggle:
    """
    Todi Odedele
    004012569
    """
    
    def __init__(self, grid=None, dictionary=None):
        """
        Constructor for Boggle game.
        :param grid: 2D list of strings representing the Boggle board
        :param dictionary: List of valid words
        """
        self.grid = []
        self.dictionary = []
        self.solutions = []
        if grid:
            self.setGrid(grid)
        if dictionary:
            self.setDictionary(dictionary)
        if grid and dictionary:
            self._solve()
    
    def setGrid(self, grid):
        """
        set the Boggle board grid.
        2D list of strings
        """
        if self._validate_grid(grid):
            self.grid = grid
            if self.dictionary:
                self._solve()
    
    def setDictionary(self, dictionary):
        """
        Set the dictionary of valid words.
        List of strings
        """
        if self._validate_dictionary(dictionary):
            self.dictionary = dictionary
            if self.grid:
                self._solve()
    
    def getSolution(self):
        
        return self.solutions
    
    def _validate_grid(self, grid):
        """
        2D list to validate
        """
        if not isinstance(grid, list):
            return False
        for row in grid:
            if not isinstance(row, list):
                return False
            for cell in row:
                if not isinstance(cell, str):
                    return False
        return True
    
    def _validate_dictionary(self, dictionary):
        """
        List to validate
        """
        if not isinstance(dictionary, list):
            return False
        for word in dictionary:
            if not isinstance(word, str):
                return False
        return True
    
    def _solve(self):
        
        self.solutions = []
        if not self.grid or not self.dictionary:
            return
        
        
        word_set = set(word.lower() for word in self.dictionary)
        
        
        prefix_set = set()
        for word in word_set:
            for i in range(1, len(word) + 1):
                prefix_set.add(word[:i])
        
        
        rows = len(self.grid)
        cols = len(self.grid[0])
        
        for i in range(rows):
            for j in range(cols):
                visited = [[False] * cols for _ in range(rows)]
                self._dfs(i, j, "", visited, word_set, prefix_set, rows, cols)
        
        
        self.solutions.sort()
    
    def _dfs(self, row, col, current_path, visited, word_set, prefix_set, rows, cols):
        """
        Depth-first search to explore all possible word paths.
        """
        
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        
        # Visited check
        if visited[row][col]:
            return
        
        
        tile = self.grid[row][col]
        new_path = current_path + tile
        new_path_lower = new_path.lower()
        
        
        if new_path_lower not in prefix_set:
            return
        
        
        visited[row][col] = True
        
        
        if (len(new_path) >= 3 and  # Simple length check first
            new_path_lower in word_set and 
            new_path not in self.solutions):
            self.solutions.append(new_path)
        
        
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            self._dfs(new_row, new_col, new_path, visited, word_set, prefix_set, rows, cols)
        
        
        visited[row][col] = False
    
    def _count_letters(self, word):
        """
        Count the number of letters in a word, accounting for special tiles.
        special tiles like "Qu", "St", "le" count as 2 letters each.
        """
        count = 0
        i = 0
        while i < len(word):
            if i + 1 < len(word):
                # Check for special letter combinations
                pair = word[i:i+2]
                if pair.lower() in ["qu", "st", "le"]:
                    count += 2
                    i += 2
                    continue
            count += 1
            i += 1
        return count


def main():
   
    # Using the board from the assignment
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "St", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]
    
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", 
                  "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", 
                  "ten", "went", "wet", "arty", "rhr", "not", "quar", "ston", "stqura"]
    
    
    mygame = Boggle(grid, dictionary)
    
    # Get and print solution
    print("Found words:", mygame.getSolution())
    print("\nExpected valid words from assignment: art, ego, gent, get, net, new, newt, prat, pry, qua, quart, rat, tar, tarp, ten, went, wet, ston, stqura")
    print("\nExpected invalid words from assignment: arty, egg, not")


if __name__ == "__main__":
    main()

