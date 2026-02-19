class Boggle:
  def __init__(self, grid, dictionary):
    self.grid = grid
    self.dictionary = dictionary
    self.solutions = []
    
  def setGrid(self, grid):
    self.grid = grid

  def setDictionary(self, dictionary):
    self.dictionary = set(dictionary)

  def getSolution(self):
    if not self.grid or not self.dictionary: #checking if parameters are empty
      print('Error: Grid and/or dictionary is empty')
      return []
        
    for elem in self.dictionary: #checks every element if all characters are alphabetic and a string
      if not elem.isalpha() or not isinstance(elem, str):
        print('Error: Dictionary contains an invalid element')
        return []
            
    for row in self.grid: #checks if the matrix is 2D
      if len(row) != len(self.grid[0]):
        print('Error: Matrix is not 2D')
        return []
            
    self.grid = [[item.lower() for item in sublist] for sublist in self.grid] #changes items in the matrix to lowercase
    fast_dictionary= {item.lower() for item in self.dictionary} #changes items in dictionary to lowercase creating fast dictionary

    rows = len(self.grid)
    columns = len(self.grid[0])
    self.solutions = set() #solution set

    for y in range(rows):
      for x in range(columns):
        visited = set() #initializing visited array
        word = '' #empty word
        self.find_all_words(y, x, word, self.grid, fast_dictionary, visited, self.solutions) #recursive method
        
    return sorted(list(self.solutions))

  def find_all_words(self, y, x, word, grid, fast_dictionary, visited, solution):
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]): #base case to check boundaries
      return
        
    if (y,x) in visited: #another base case
      return
        
    current = grid[y][x]
    word += current

    prefix = False #checks if any the word is a a prefix of any words in the dictionary
    for elem in fast_dictionary:
      if elem.startswith(word):
        prefix = True
        break
    if not prefix:
      return

    if word in fast_dictionary and len(word) >= 3: #saves word to solution if word is in dictionary
      solution.add(word)

    visited.add((y, x)) #if prefix, # mark as visited
      
    #continuing the search in 8 adjacent tiles
    for dy in [-1, 0 , 1]: #vertical adjacent tiles
      for dx in [-1, 0, 1]: #horizontal adjacent tiles
        if dy == 0 and dx == 0: #skips the current tile because it is not usable
          continue
        self.find_all_words(y + dy, x + dx, word, grid, fast_dictionary, visited, solution) #recursive

    visited.remove((y, x)) #removes the prefixes, as you continue to run through

def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()