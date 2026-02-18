class Boggle:
    def __init__(self, grid=None, dictionary=None):
        '''
        Initializes the Boggle game with a board and a list of words.
        '''
        self.grid = grid if grid else []
        self.dictionary = dictionary if dictionary else []
        self.solution = []
        self.n = 0

    def setGrid(self, grid):
        '''
        Updates the game board with a new 2D array.
        '''
        self.grid = grid

    def setDictionary(self, dictionary):
        '''
        Updates the list of valid words for the game.
        '''
        self.dictionary = dictionary

    def getSolution(self):
        '''
        Main logic: Validates input, cleans data, and starts the word search.
        '''
        if not self.dictionary or not self.grid:
            return []
        
        self.n = len(self.grid)
        if self.n <= 0: 
            return []
        for row in self.grid:
            if len(row) != self.n:
                return []

        fast_dictionary = set()
        prefix_set = set()

        for word in self.dictionary:
            clean_word = str(word).upper().strip()
            if len(clean_word) >= 3:
                fast_dictionary.add(clean_word)
                # Build prefixes: Q, QU, QUA, QUAR...
                for i in range(1, len(clean_word) + 1):
                    prefix_set.add(clean_word[:i])
        
        upper_grid = [[str(cell).upper().strip() for cell in row] for row in self.grid]
        solution_set = set()

        for y in range(self.n):
            for x in range(self.n):
                self._find_all_words(y, x, "", upper_grid, prefix_set, fast_dictionary, set(), solution_set)

        self.solution = sorted(list(solution_set))
        return self.solution

    def _find_all_words(self, y, x, current_word, grid, prefix_set, fast_dict, visited, solution_set):
        if (y < 0 or y >= self.n or x < 0 or x >= self.n or (y, x) in visited):
            return

        tile = grid[y][x]
        
        # Robust "QU" handling: 
        # If tile is "Q", treat it as "QU". If it's already "QU", use "QU".
        if tile == "Q":
            added_word = "QU"
        else:
            added_word = tile

        new_word = current_word + added_word

        # Pruning Logic
        if new_word not in prefix_set:
            return

        visited.add((y, x))
        
        if new_word in fast_dict:
            solution_set.add(new_word)

        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue
                self._find_all_words(y + dy, x + dx, new_word, grid, prefix_set, fast_dict, visited, solution_set)

        visited.remove((y, x))

def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
  
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()