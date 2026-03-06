#Nigel Tendo
#004002779

class Boggle: #created the class for the game
    def __init__(self, grid, dictionary): #made a constructor with 3 parameters
        self._grid = grid #to store the game grid
        self._dictionary = {word.upper() for word in dictionary} #all words uppercase
        self._prefixes = set() # NEW: stores all prefixes of all dictionary words
        for word in self._dictionary:
            for i in range(1, len(word) + 1):
                self._prefixes.add(word[:i]) # e.g. "CAT" adds "C", "CA", "CAT"
        self._solution = [] #object for solution
    
    def setGrid(self, grid): #setter with 2 objects to update grid
      self._grid = grid #object for grid
      self._solution = None #object for solution equals nothing

    def setDictionary(self, dictionary): #setter to set dictionary
      self._dictionary = {word.upper() for word in dictionary} #all words uppercase
      self._prefixes = set() # NEW: rebuild prefixes when dictionary changes
      for word in self._dictionary:
          for i in range(1, len(word) + 1):
              self._prefixes.add(word[:i])
      self._solution = None

    def getSolution(self): #method to get solution
      if not self._grid: # handle empty grid
          return []
      found_words = set() #made a hashset called found words
      rows = len(self._grid)
      cols = len(self._grid[0])

      for row in range(rows): #loop through all rows and columns
        for col in range(cols):
          visited = [[False]* cols for _ in range(rows)]
          self._dfs(row, col, "", visited, found_words)

      return sorted(list(found_words))

    def _expand_tile(self, tile): #handles tile letters
      return tile.upper()

    def _dfs(self, row, col, current_word, visited, found_words):

      visited[row][col] = True

      current_letter = self._expand_tile(self._grid[row][col])
      current_word = current_word + current_letter

      # NEW: early stop - if nothing in dictionary starts with this, stop searching
      if current_word not in self._prefixes:
          visited[row][col] = False
          return

      if len(current_word) >= 3 and current_word in self._dictionary:
        found_words.add(current_word)

      rows = len(self._grid)
      cols = len(self._grid[0])

      for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
          if dr == 0 and dc == 0:
            continue

          new_row = row + dr
          new_col = col + dc

          if (new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols and not visited[new_row][new_col]):
            self._dfs(new_row, new_col, current_word, visited, found_words)

      visited[row][col] = False


def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "not"]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()


