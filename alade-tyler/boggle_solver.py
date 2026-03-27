import re 

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        word = word.upper()  # ensure consistent case
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True


class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = set()

    def dfs(self, row, col, visited, cur, tNode):
        # Check boundaries
        if row < 0 or col < 0 or row >= len(self.grid) or col >= len(self.grid[row]):
            return
        if visited[row][col]:
            return

        next_node = tNode
        # loop over each character in the current cell
        for c in self.grid[row][col].upper():  # match dictionary case
            if c not in next_node.children:
                return
            next_node = next_node.children[c]

        visited[row][col] = True
        cur += self.grid[row][col].upper()

        if next_node.end and len(cur) >= 3:
            self.solutions.add(cur)

        # Explore all 8 directions
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
        for dr, dc in directions:
            self.dfs(row + dr, col + dc, visited, cur, next_node)

        visited[row][col] = False  # backtrack

    def getSolution(self):
        if not self.grid or not self.grid[0]:
            return []

        # Build the Trie
        trie = Trie()
        for word in self.dictionary:
            trie.insert(word)

        rows = len(self.grid)
        cols = len(self.grid[0])

        # Initialize visited matrix
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        # Start DFS from every cell
        for row in range(rows):
            for col in range(cols):
                self.dfs(row, col, visited, "", trie.root)

        # Return a sorted list for tests
        return sorted(self.solutions)


# Example usage
def main():
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]

    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt",
        "prat", "pry", "qua", "quart", "quartz", "rat",
        "tar", "tarp", "ten", "went", "wet", "arty",
        "rhr", "not", "quar"
    ]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
