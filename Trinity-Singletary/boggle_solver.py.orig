# Boggle Solver
import re

#depth first traversal, call dfs and use for loop to iterate through loops, use base case
#start with check to make sure the grid is a valid grid

class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = self.convert_grid_to_lowercase(grid)  # 2D list representing the board
        self.dictionary = self.convert_dictionary_to_lowercase(dictionary)  # list of words to search for
        self.solutions = []  # found words
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid else 0
        self.fast_dict = {}
        self.solution_set = set() #changed Set() to set()
        

    def convert_dictionary_to_lowercase(self, dictionary):
      return [string.lower() for string in dictionary]
    
    def convert_grid_to_lowercase(self, grid):
      return [[string.lower() for string in inner_list] for inner_list in grid]
      


#check if theres a letter, instead of i-> iu and q->qu and S->st
    def isValidGrid(self):
        #check if grid exists
        if self.grid is None or len(self.grid) == 0:
            return False
        gridSize = len(self.grid)

        #check if grid size is valid (NxN)
        for row in self.grid:
            if len(row) != gridSize:
                return False

        #check if there are no raw q's, s's, I's
        for row in self.grid:
            for letter in row:
                if letter.lower() == 'q' or letter.lower() == 's' or letter.lower() == 'i':
                    return False

        #return true or False
        return True


    def isValidDictionary(self):#check if dictionary exists and is not empty
        if self.dictionary is None or len(self.dictionary) == 0:
            return False

    #check if dictionary is an array of words and if uses letter
        for word in self.dictionary:
            if not isinstance(word, str):
                return False
            if not word.isalpha():
                return False

    #check if there are no empty words
        for word in self.dictionary:
            if len(word) == 0:
                return False

    #return true or False
        return True
        

    def build_fast_dictionary(self):
        fast_dict = {}
        for word in self.dictionary:
            prefix = ""
            for char in word:
                prefix += char
                if prefix not in fast_dict:
                    fast_dict[prefix] = 0
            fast_dict[word] = 1
        return fast_dict

    def find_all_words(self, y, x, current_word, visited):
        # ----- Base Case -----
        if y < 0 or y >= self.rows or x < 0 or x >= self.cols:
            return
        if visited[y][x]:
            return

        # ----- Form New Word -----
        new_word = current_word + self.grid[y][x]

        # ----- Prefix Pruning -----
        if new_word not in self.fast_dict:
            return

        # ----- Word Found -----
# Only add complete words with length >= 3 (Boggle rule + test requirement)
        if self.fast_dict[new_word] == 1 and len(new_word) >= 3:
            self.solution_set.add(new_word)


        # ----- DFS -----
        visited[y][x] = True

        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy != 0 or dx != 0:
                    self.find_all_words(y + dy, x + dx, new_word, visited)

        # ----- Backtrack -----
        visited[y][x] = False



    def setGrid(self, grid):
        self.grid = grid  # update grid with an existing grid

    def setDictionary(self, dictionary):
        self.dictionary = dictionary 
    
    def getSolution(self):
        # Check each word in the dictionary
        if self.isValidGrid() == False or self.isValidDictionary() == False:
          print("Grid Invalid or Dictionary Invalid")
          return self.solutions

        self.fast_dict = self.build_fast_dictionary()
        #solution_set = set() #changed Set() to set()

        for y in range(self.rows):
            for x in range(self.cols):
                visited = [[False] * self.cols for _ in range(self.rows)]
                self.find_all_words(y, x, "", visited)

        return list(self.solution_set)


    def getgrid(self):
      return self.grid 

    def getdictionary(self):
      return self.dictionary

    def exists(self, word):
        # Lowercase the word for consistent comparison
        word_lower = word.lower()
        # Try every starting position in the grid
        for row_index in range(self.rows):
            for col_index in range(self.cols):
                if self.search(row_index, col_index, word_lower, 0, set()):
                    return True
        return False

    def search(self, row_index, col_index, word_lower, word_index, visited_positions):
        # Base case: fully matched
        if word_index == len(word_lower):
            return True

        # Out of bounds or already visited
        if (row_index < 0 or row_index >= self.rows or
            col_index < 0 or col_index >= self.cols or
            (row_index, col_index) in visited_positions):
            return False

        cell_value_lower = self.grid[row_index][col_index].lower()

        # If the current cell does not match the next part of the word
        if not word_lower.startswith(cell_value_lower, word_index):
            return False

        # Mark current cell as visited
        visited_positions.add((row_index, col_index))
        next_index = word_index + len(cell_value_lower)

        # Explore all 8 directions
        for delta_row in [-1, 0, 1]:
            for delta_col in [-1, 0, 1]:
                if delta_row != 0 or delta_col != 0:
                    if self.search(row_index + delta_row, col_index + delta_col, word_lower, next_index, visited_positions.copy()):
                        return True

        # Backtrack
        visited_positions.remove((row_index, col_index))
        return False


def main():
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]

    dictionary = [
        "ego", "Quart", "Ten", "aab"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()

"""

def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()

"""