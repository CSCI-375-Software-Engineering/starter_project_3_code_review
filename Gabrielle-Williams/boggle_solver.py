
"NAME: Gabrielle Williams. SID: 004004079"
class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = []
        self.solution_set = set()
        self.rows = 0
        self.cols = 0
        
    def set_grid(self,grid):

      self.new_grid = []
      if not grid or not grid[0]:
        return False
      #gets grid dimensions
      rows = len(grid)
      cols = len(grid[0])
      for row in grid:
        if len(row) != cols or len(row) != rows:
          return False
      for row in grid:
        for cell in row:
          if not isinstance(cell, str) or not cell.isalpha():
            return False
      self.rows = rows
      self.cols = cols
      #Makes grid uppercase
      for i in grid:
        new_row = []
        for j in i:
          new_row.append(j.upper())
        self.new_grid.append(new_row)
      return True
      pass
    
  
    def set_dictionary(self,dictionary):
      self.dict_hash = {}
      if not dictionary:
        return False

      self.dict_hash= {"": 0}
      self.max_word_len = max(len(word) for word in dictionary)

      for word in dictionary:
        if not word.isalpha():
          return False
      #hashmap forming
        word_upper = word.upper()
        for i in range(1,len(word_upper)):
          
          #takes it letter by letter, prefix = 0 , word = 1
          prefix = word_upper[:i]
          if prefix not in self.dict_hash:
            self.dict_hash[prefix] = 0
        self.dict_hash[word_upper] = 1
      return True
      
    
    def boggle_dfs(self, r, c, word, visited):
      if r < 0 or r >= self.rows or c < 0 or c >= self.cols or visited[r][c]:
        return

      if visited[r][c]:
        return

      tile = self.new_grid[r][c]
      new_word = word + tile

      if len(new_word) > self.max_word_len:
        return

      if new_word not in self.dict_hash:
        return

      if self.dict_hash.get(new_word) == 1 and len(new_word) >= 3:
        self.solution_set.add(new_word)

      visited[r][c] = True
      #going through each neighbor
      for row in range(-1,2):
        for col in range(-1,2):
          if row == 0 and col == 0:
            continue
          new_row = r + row
          new_col = c +col
          self.boggle_dfs(new_row,new_col,new_word,visited)
      #unmark cells so that they can be revisited later
      visited[r][c] = False   
    pass
    
    def get_solution(self):
      #clears results
      self.solutions = []
      self.solution_set = set()
      #checks validity of grid and dictionary
      check_grid = self.set_grid(self.grid)
      if check_grid == False:
        return []
      check_dict = self.set_dictionary(self.dictionary)
      if check_dict == False:
        return []
      for r in range(self.rows):
        for c in range(self.cols):
          visited = []
          #2D grid for letters that were visited
          for i in range(self.rows):
            new_row = []
            for j in range(self.cols):
              new_row.append(False)
            visited.append(new_row)
          self.boggle_dfs(r,c,"",visited)
      #convert set to list
      for word in self.solution_set:
        self.solutions.append(word)
      return self.solutions
 
      pass
    
def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    mygame = Boggle(grid, dictionary)
    print(mygame.get_solution())
if __name__ == "__main__":
    main()
