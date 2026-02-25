"""
ALANA MARCIAL
004001996
"""
from typing import List


class Boggle:
    def __init__(self, grid: List[List[str]], dictionary: List[str]):
        self.grid = []
        self.dictionary = []
        self.rows = 0
        self.cols = 0
        
        self.set_grid(grid)
        self.set_dictionary(dictionary)
        self.solution = []

    def _normalize_grid(self, grid: List[List[str]]):
        if not grid or not grid[0]:
            return [], 0, 0
        
        normalized = [[cell.lower() for cell in row] for row in grid]
        rows = len(normalized)
        cols = len(normalized[0])
        
        if not all(len(row) == cols for row in normalized):
            raise ValueError("Grid must be rectangular.")
            
        return normalized, rows, cols

    def set_grid(self, grid: List[List[str]]):
        self.grid, self.rows, self.cols = self._normalize_grid(grid)
        self.solution = []

    def set_dictionary(self, dictionary: List[str]):
        self.dictionary = [word.lower() for word in dictionary]
        self.solution = []

    def get_solution(self) -> List[str]:
        if not self.grid or not self.dictionary:
            return []

        found = set()
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        for word in self.dictionary:
            if len(word) < 3:
                continue
            
            if self._exist(word, visited):
                found.add(word)

        self.solution = sorted(list(found))
        return self.solution

    def _exist(self, word: str, visited: List[List[bool]]) -> bool:
        for r in range(self.rows):
            for c in range(self.cols):
                if self._dfs(r, c, word, 0, visited):
                    return True
        return False

    def _dfs(self, r: int, c: int, word: str, index: int, visited: List[List[bool]]) -> bool:
        if index == len(word):
            return True

        if not (0 <= r < self.rows and 0 <= c < self.cols) or visited[r][c]:
            return False

        tile = self.grid[r][c]
        tile_len = len(tile)

        if not word[index:].startswith(tile):
            return False

        visited[r][c] = True
        
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                
                if self._dfs(r + dr, c + dc, word, index + tile_len, visited):
                    visited[r][c] = False
                    return True

        visited[r][c] = False
        return False


def main():
    grid = [
        ["T", "W", "Y", "R"], 
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]
    
    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt", "prat", 
        "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", 
        "ten", "went", "wet", "arty", "rhr", "not", "quar"
    ]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.get_solution())


if __name__ == "__main__":
    main()