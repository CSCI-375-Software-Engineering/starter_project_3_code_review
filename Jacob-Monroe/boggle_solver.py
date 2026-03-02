"""
Jacob Monroe
SSID: 003108194
"""

class BoggleSolver:
    def __init__(self, dictionary):
        self.words = set(dictionary)
        self.trie = {}
        for word in self.words:
            if len(word) < 3:
                continue
            node = self.trie
            for char in word.lower():
                if char not in node:
                    node[char] = {}
                node = node[char]
            node["#"] = True

    def getSolution(self, grid):
        if not grid:
            return []
        
        rows = len(grid)
        cols = len(grid[0])
        found_words = set()
        
        for r in range(rows):
            for c in range(cols):
                self._dfs(grid, r, c, rows, cols, self.trie, "", set(), found_words)
        
        return sorted(list(found_words))

    def _dfs(self, grid, r, c, rows, cols, node, path, visited, found_words):
        char = grid[r][c].lower()
        current_node = node
        
        for s in char:
            if s not in current_node:
                return
            current_node = current_node[s]
        
        new_path = path + char
        visited.add((r, c))

        if "#" in current_node:
            found_words.add(new_path)

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    self._dfs(grid, nr, nc, rows, cols, current_node, new_path, visited, found_words)

        visited.remove((r, c))