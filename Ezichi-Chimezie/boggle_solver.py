# Boggle Solver

# Name: Ezichi Chimezie
# ID: 004004796


class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = set()
        self.trie_root = {}

    def set_grid(self, grid):
        self.grid = grid

    def set_dictionary(self, dictionary):
        self.dictionary = dictionary

    def build_trie(self):
        self.trie_root = {}

        for word in self.dictionary:
            current_node = self.trie_root

            for char in word:
                char = char.lower()
                if char not in current_node:
                    current_node[char] = {}
                current_node = current_node[char]

            current_node['_end_'] = True

    def search_from_cell(self, row, col, visited, current_word, trie_node):
        # Invalid position check
        if (row < 0 or col < 0
                or row >= len(self.grid) or col >= len(self.grid[0])):
            return

        if visited[row][col]:
            return

        # Prefix validation
        current_node = trie_node
        for char in self.grid[row][col]:
            char = char.lower()
            if char not in current_node:
                return
            current_node = current_node[char]

        visited[row][col] = True
        current_word += self.grid[row][col].lower()

        if '_end_' in current_node and len(current_word) >= 3:
            self.solutions.add(current_word)

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1),
        ]
        for d_row, d_col in directions:
            self.search_from_cell(
                row + d_row, col + d_col,
                visited, current_word, current_node
            )

        visited[row][col] = False

    def getSolution(self):
        return self.get_solution()

    def get_solution(self):
        # Validate grid
        if not isinstance(self.grid, list):
            return []
        if len(self.grid) == 0:
            return []
        for row in self.grid:
            if len(row) != len(self.grid):
                return []

        # Validate dictionary
        if not isinstance(self.dictionary, list):
            return []
        if len(self.dictionary) == 0:
            return []

        # Clear previous solutions
        self.solutions.clear()

        # Build trie
        self.build_trie()

        # Create visited matrix
        size = len(self.grid)
        visited = [[False] * size for _ in range(size)]

        # Loop over each cell
        for row in range(size):
            for col in range(size):
                self.search_from_cell(row, col, visited, "", self.trie_root)

        return sorted(self.solutions)


def main():
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"],
    ]
    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry",
        "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet",
        "arty", "rhr", "not", "quar",
    ]

    my_game = Boggle(grid, dictionary)
    print(my_game.get_solution())


if __name__ == "__main__":
    main()
