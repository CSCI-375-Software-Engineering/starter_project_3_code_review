'''
Name: Langyia Philemon
SID: 004002416
'''

class Boggle:
  # constructor: set up the grid, dictionary and helper sets
    def __init__(self, grid, dictionary):
        self.grid = grid #this is teh NxN boggle board
        self.dictionary = dictionary #list of valid words
        self.solution = [] #hold all the words we find
        if dictionary: #convert dictionary to uppercase to make it case insensitive
          self.word_set = set(word.upper()for word in dictionary)
        else:
          self.word_set = set() #incase there is an empty dictionary
        self.prefix_set = set() #makes a prefix set so that the dfs ends early
        for word in self.word_set:
          for i in range(1, len(word)+1):
            self.prefix_set.add(word[:i]) #adds every prefix of each word
    def setDictionary(self, dictionary): #setter for dictionary
      self.dictionary = dictionary
      if dictionary:
          self.word_set = set(word.upper()for word in dictionary)
      else:
        self.word_set = set()
      self.prefix_set = set()
      for word in self.word_set:
        for i in range(1, len(word)+1):
          self.prefix_set.add(word[:i])
    def getSolution(self): #function to find all words
        self.solution = []
        if not self.grid or not self.dictionary: #check for invalid input
            return []
        rows = len(self.grid) #number of rows
        columns = len(self.grid[0]) #number of columns
        visited = [[False for j in range(columns)] for i in range(rows)] #create visited array to check the tiles used in the current word
        found = set() # store words that we find and we used a set to prevent duplicates
        for r in range(rows): #start dfs from every tile
            for c in range(columns):
                self._dfs(r, c, "", visited, found)
        self.solution = sorted(found) #sort to arrange the words found
        return self.solution
    def _dfs(self, r, c, current_word, visited, found): #helper function
        rows = len(self.grid)
        columns = len(self.grid[0])
        if r < 0 or r >= rows or c < 0 or c >= columns: #base case if out of bounds
            return
        if visited[r][c]: #base case if we already used thsi tile in the current path
            return
        letter = self.grid[r][c].upper() #the tile
        new_word = current_word + letter #add the tile to the current word
        if new_word not in self.prefix_set: #stop if the new_word wonyt match the prefixes
          return
        if len(new_word) >= 3 and new_word in self.word_set: #if the word is valid, add it to the set
            found.add(new_word) 
        visited[r][c] = True #tile is used
        for drow in [-1, 0, 1]: # explore all the adjacent tiles including the diagonals
            for dcolumn in [-1, 0, 1]:
                if drow != 0 or dcolumn != 0: #skip the current tile
                    self._dfs(r+ drow, c+ dcolumn, new_word, visited, found)
        visited[r][c] = False #unmark tile when going back
    
def main(): #main function
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    mygame = Boggle(grid, dictionary) #boggle object
    print(mygame.getSolution()) #print the words that we found

if __name__ == "__main__":
    main()
    
