# Boggle Solver
import re

class Boggle:
  def __init__(self, grid, dictionary):
    self.grid = grid
    self.dictionary = dictionary
    self.solutions = set()


  def dict_hash(self):
    # Builds hash map of word prefixes

    prefix_hash = {}
  
    for word in self.dictionary:
      prefix = ""
      for i, letter in enumerate(word):
        prefix += letter

        # If the prefix has not been seen before, its defult value is 0
        if prefix not in prefix_hash:
          prefix_hash[prefix] = 0
      
        # If the prefix is a full word, its value is 1
        if i == len(word) - 1:
          prefix_hash[prefix] = 1
  
    return prefix_hash

  def getSolution(self):
    # Check input paarameters
    if not self.grid or not self.dictionary:
      return []
  
    # Check grid is NxN
    n = len(self.grid)
    for row in self.grid:
      if len(row) != n:
        return []

    # Make data one case
    self.grid = [[cell.lower() for cell in row] for row in self.grid]
    self.dictionary = [word.lower() for word in self.dictionary]

    # Check dictionary
    if not all(isinstance(word, str) for word in self.dictionary):
      return []
  
    # Data structures
    self.fast_dict = self.dict_hash()     # Hash map of prefixes
    self.solutions = set()                # Solution set

    visited = [[False for _ in range(n)] for _ in range(n)]

    # Iterate over NxN grid and search from each cell
    for y in range(n):
      for x in range(n):
        self.find_all_words(y, x, "", visited)

    return [word.upper() for word in self.solutions]

  def find_all_words(self, y, x, word, visited):
    n = len(self.grid)

    # Check base case
    if y < 0 or y >= n or x < 0 or x >= n:
      return

    if visited[y][x]:
      return
  
    # Form word
    letter = self.grid[y][x]
    new_word = word + letter

    # If prefix dosen't exist, stop search
    if new_word not in self.fast_dict:
      return
  
    # Mark cell visited
    visited[y][x] = True

    # If full word, save to solutions
    if self.fast_dict[new_word] == 1 and len(new_word) >= 3:
      self.solutions.add(new_word)

    # Continue searching
    for dy in [-1, 0, 1]:
      for dx in [-1, 0, 1]:
        if dy != 0 or dx != 0:
          self.find_all_words(y + dy, x + dx, new_word, visited)
  
    # Unmark cell visited
    visited[y][x] = False



def main():
    grid = [["T", "W", "Y", "R"], 
            ["E", "N", "P", "H"],
            ["G", "Z", "Qu", "R"],
            ["O", "N", "T", "A"]]

    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    mygame = Boggle(grid, dictionary) 
    print(mygame.getSolution())

if __name__ == "__main__":
    main()
