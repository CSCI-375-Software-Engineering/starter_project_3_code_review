class Boggle:
    MIN_WORD_LENGTH = 3

    def __init__(self, grid=None, dictionary=None):
        '''
        Initializes the Boggle game with a board and a list of words.
        '''
        self.grid = []
        self.rows = 0
        self.cols = 0
        self._fast_dictionary = set()
        self._prefix_set = set()
        
        if grid:
            self.set_grid(grid)
        if dictionary:
            self.set_dictionary(dictionary)

    def set_grid(self, grid):
        '''
        Updates the game board with a new 2D array.
        '''
        if not grid or not grid[0]:
            self.grid = []
            self.rows = 0
            self.cols = 0
            return

        self.grid = [[str(cell).upper().strip() for cell in row] for row in grid]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def set_dictionary(self, dictionary):
        '''
        Updates the list of valid words for the game.
        '''
        self._fast_dictionary = set()
        self._prefix_set = set()

        for word in dictionary:
            clean_word = str(word).upper().strip()
            if len(clean_word) >= self.MIN_WORD_LENGTH:
                self._fast_dictionary.add(clean_word)
                # Build prefixes: Q, QU, QUA, QUAR...
                for i in range(1, len(clean_word) + 1):
                    self._prefix_set.add(clean_word[:i])

    def get_solution(self):
        '''
        Main logic: Validates input, cleans data, and starts the word search.
        '''
        if not self._fast_dictionary or not self.grid:
            return []

        solution_set = set()

        for y in range(self.rows):
            for x in range(self.cols):
                self._find_all_words(y, x, "", set(), solution_set)

        return sorted(list(solution_set))

    def _find_all_words(self, y, x, current_word, visited, solution_set):
        if (y < 0 or y >= self.rows or x < 0 or x >= self.cols or (y, x) in visited):
            return

        tile = self.grid[y][x]
        
        # Robust "QU" handling: 
        # If tile is "Q", treat it as "QU". If it's already "QU", use "QU".
        if tile == "Q":
            added_word = "QU"
        else:
            added_word = tile

        new_word = current_word + added_word

        # Pruning Logic
        if new_word not in self._prefix_set:
            return

        visited.add((y, x))
        
        if new_word in self._fast_dictionary:
            solution_set.add(new_word)

        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue
                self._find_all_words(y + dy, x + dx, new_word, visited, solution_set)

        visited.remove((y, x))

def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
  
    mygame = Boggle(grid, dictionary)
    print(mygame.get_solution())

if __name__ == "__main__":
    main()