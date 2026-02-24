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
        for word in self.dictionary:
            # Rule: Words must be at least 3 letters long
            if len(word) < 3:
                continue
            self.dict_prefix_word[word] = 1
            for i in range(1, len(word)):
                prefix = word[:i]
                if prefix not in self.dict_prefix_word:
                    self.dict_prefix_word[prefix] = 0

    def dir_search(self, i, j, visited, current_word): 
        # Check dictionary status
        status = self.dict_prefix_word.get(current_word)
        
        if status == 1:
            self.solutions.add(current_word)
            
        # Stop searching if this path isn't a valid prefix
        if status is None and not any(k.startswith(current_word) for k in self.dict_prefix_word):
             # We use a slightly more robust check because "qu" might jump 
             # over a prefix state in the dictionary keys.
             if status is None: return

        for di, dj in self.dirs:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < len(self.grid) and 0 <= nj < len(self.grid[0]):
                if (ni, nj) not in visited:
                    visited.add((ni, nj))
                    new_letter = self.grid[ni][nj]
                    
                    # Recurse with the updated string
                    self.dir_search(ni, nj, visited, current_word + new_letter)
                    
                    # Backtrack
                    visited.remove((ni, nj))

    def getSolution(self):
        if not self.grid or not self.dictionary:
            return self.solutions

        # Square Grid Check
        row_length = len(self.grid)
        for row in self.grid:
            if len(row) != row_length:
                return self.solutions

        # Alphabetic Dictionary Check
        for word in self.dictionary:
            if not word.isalpha():
                return self.solutions

        # Normalization and multi-char tile validation
        self.dictionary = [x.lower() for x in self.dictionary]
        temp_grid = []
        for row in self.grid:
            new_row = []
            for char in row:
                c = char.lower()
                if len(c) > 1 and c not in ["qu", "st", "ie"]:
                    return self.solutions
                # Rules: No raw Q, S, or I
                if c in ["q", "s", "i"]:
                    return self.solutions
                new_row.append(c)
            temp_grid.append(new_row)
        self.grid = temp_grid

        self.build_fast_dict()

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.dir_search(i, j, {(i, j)}, self.grid[i][j])
                
        return self.solutions

def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()