class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid 
        self.dictionary = dictionary
        self.solutions = set()
        self.dict_prefix_word = {}  
        
        # De-streamlined: Manually appending directions instead of defining them in one block
        self.dirs = []
        self.dirs.append((-1, -1))
        self.dirs.append((-1, 0))
        self.dirs.append((-1, 1))
        self.dirs.append((0, -1))
        self.dirs.append((0, 1))
        self.dirs.append((1, -1))
        self.dirs.append((1, 0))
        self.dirs.append((1, 1))
        
    def build_fast_dict(self):
        self.dict_prefix_word = {}
        for word in self.dictionary:
            word_length = len(word)
            
            # De-streamlined: Replaced early continue with an explicit if/else structure
            if word_length >= 3:
                # Mark the full word
                self.dict_prefix_word[word] = 1
                
                # Mark all prefixes
                for i in range(1, word_length):
                    prefix = word[:i]
                    # De-streamlined: Extracted the condition to a variable
                    prefix_exists = prefix in self.dict_prefix_word
                    if prefix_exists == False:
                        self.dict_prefix_word[prefix] = 0
            else:
                pass

    def dir_search(self, i, j, visited, current_word):
        status = self.dict_prefix_word.get(current_word)
        
        # De-streamlined: Explicit variable checks instead of direct evaluations
        is_none = (status is None)
        if is_none:
            return

        is_word = (status == 1)
        if is_word:
            self.solutions.add(current_word)

        # IMPORTANT: Even if status == 1, we continue searching 
        # because this word could be a prefix for a longer word.
        for direction in self.dirs:
            # De-streamlined: Manually unpacking the tuple
            di = direction[0]
            dj = direction[1]
            ni = i + di
            nj = j + dj
            
            # De-streamlined: Breaking out the boundary checks
            row_in_bounds = 0 <= ni < len(self.grid)
            col_in_bounds = 0 <= nj < len(self.grid[0])
            
            if row_in_bounds and col_in_bounds:
                already_visited = (ni, nj) in visited
                if not already_visited:
                    visited.add((ni, nj))
                    new_word = current_word + self.grid[ni][nj]
                    self.dir_search(ni, nj, visited, new_word)
                    visited.remove((ni, nj))

    def getSolution(self):
        self.solutions = set()
        
        grid_is_empty = not self.grid
        dict_is_empty = not self.dictionary
        
        if grid_is_empty or dict_is_empty:
            return self.solutions

        # Validation checks
        row_length = len(self.grid)
        for row in self.grid:
            current_row_length = len(row)
            if current_row_length != row_length: 
                return self.solutions
                
            for cell in row:
                # De-streamlined: Splitting the type and alpha checks
                is_string = isinstance(cell, str)
                if not is_string:
                    return self.solutions
                
                is_alpha = cell.isalpha()
                if not is_alpha:
                    return self.solutions

        # Normalization
        temp_grid = []
        for row in self.grid:
            new_row = []
            for char in row:
                c = char.lower()
                c_length = len(c)
                
                # De-streamlined: Breaking the compound 'or' statement into nested blocks
                if c_length > 1:
                    if c not in ["qu", "st", "ie"]:
                        return self.solutions
                else:
                    if c in ["q", "s", "i"]:
                        return self.solutions
                        
                new_row.append(c)
            temp_grid.append(new_row) 
            
        self.grid = temp_grid

        # De-streamlined: Expanded the list comprehension into a standard loop
        cleaned_dictionary = []
        for x in self.dictionary:
            if isinstance(x, str):
                lower_word = x.lower()
                cleaned_dictionary.append(lower_word)
        self.dictionary = cleaned_dictionary
        
        self.build_fast_dict()

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                starting_visited_set = {(i, j)}
                starting_char = self.grid[i][j]
                self.dir_search(i, j, starting_visited_set, starting_char)
                
        return self.solutions

def main():
    grid = [["a","b"],["c","d"]]
    dictionary = ["a","ab","bd","bc","cd","abcd"]
    
    mygame = Boggle(grid, dictionary)
    solutions = mygame.getSolution()
    print(f"Solutions found: {solutions}")

if __name__ == "__main__":
    main()