class Boggle:
  def __init__(self, grid, dictionary):
    self.grid = grid 
    self.dictionary = dictionary
    self.solutions = set()
    self.dict_prefix_word = {}  
    self.dirs = [(-1, -1), (-1, 0), (-1, 1), 
                 (0, -1),           (0, 1), 
                 (1, -1),  (1, 0),  (1, 1)]
        
  def build_fast_dict(self):
    self.dict_prefix_word = {}
    for word in self.dictionary:
        if len(word) < 3:
            continue
        # Mark the full word
        self.dict_prefix_word[word] = 1
        # Mark all prefixes
        for i in range(1, len(word)):
            prefix = word[:i]
            # Don't overwrite a '1' (word) with a '0' (prefix)
            if prefix not in self.dict_prefix_word:
                self.dict_prefix_word[prefix] = 0

  def dir_search(self, i, j, visited, current_word):
    status = self.dict_prefix_word.get(current_word)
        
    # If not a word or a prefix, stop
    if status is None:
        return

    # If it's a word, add it
    if status == 1:
        self.solutions.add(current_word)

    # IMPORTANT: Even if status == 1, we continue searching 
    # because this word could be a prefix for a longer word.
    for di, dj in self.dirs:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(self.grid) and 0 <= nj < len(self.grid[0]):
            if (ni, nj) not in visited:
                visited.add((ni, nj))
                self.dir_search(ni, nj, visited, current_word + self.grid[ni][nj])
                visited.remove((ni, nj))

  def getSolution(self):
    self.solutions = set()
    if not self.grid or not self.dictionary:
        return self.solutions

    # Validation checks
    row_length = len(self.grid)
    for row in self.grid:
        if len(row) != row_length: return self.solutions
        for cell in row:
            if not isinstance(cell, str) or not cell.isalpha():
                return self.solutions

    # Normalization
    temp_grid = []
    for row in self.grid:
        new_row = []
        for char in row:
            c = char.lower()
            if (len(c) > 1 and c not in ["qu", "st", "ie"]) or c in ["q", "s", "i"]:
                return self.solutions
            new_row.append(c)
        temp_grid.append(new_row) # Fixed Indentation
    self.grid = temp_grid

    self.dictionary = [x.lower() for x in self.dictionary if isinstance(x, str)]
    self.build_fast_dict()

    for i in range(len(self.grid)):
        for j in range(len(self.grid[i])):
            self.dir_search(i, j, {(i, j)}, self.grid[i][j])
                
    return self.solutions

def main():
  grid = [["a","b"],["c","d"]]
  dictionary = ["a","ab","bd","bc","cd","abcd"]
    
  mygame = Boggle(grid, dictionary)
  print(f"Solutions found: {mygame.getSolution()}")

if __name__ == "__main__":
  main()