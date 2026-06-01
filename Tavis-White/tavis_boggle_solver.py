"""Tavis White-004001953"""


def _normalize_tile_key(tile):
    """Normalize tile label for special-tile checks (case-insensitive)."""
    if not tile:
        return tile
    t = tile.upper()
    if t == "QU":
        return "Qu"
    if t == "ST":
        return "St"
    if t == "IE":
        return "Ie"
    return tile


class Boggle:
    """
    A Boggle game solver that finds all valid words in a grid.

    Rules:
    - Words must use adjacent tiles (including diagonals)
    - Each tile may not be used more than once per word
    - Words must be at least 3 letters long
    - Special tiles: "Qu", "St", "Ie" count as 2 letters each
    """

    _SPECIAL = frozenset({"Qu", "St", "Ie"})

    def __init__(self, grid=None, dictionary=None):
        """
        Initialize a Boggle game instance.

        Args:
            grid: 2D array of strings representing the game grid
            dictionary: List of valid words to search for
        """
        self.grid = grid if grid is not None else []
        self.dictionary = dictionary if dictionary is not None else []
        # Words collected during DFS (deduped in getSolution).
        self._found_words = []
        self.rows = len(self.grid) if self.grid else 0
        self.cols = len(self.grid[0]) if self.grid and self.grid[0] else 0

    def setGrid(self, grid):
        """Set the game grid."""
        self.grid = grid
        self.rows = len(self.grid) if self.grid else 0
        self.cols = len(self.grid[0]) if self.grid and self.grid[0] else 0

    def setDictionary(self, dictionary):
        """Set the dictionary of valid words to search for."""
        self.dictionary = dictionary

    def getSolution(self):
        """
        Find all valid words in the grid and return them as a list.

        Returns:
            List of found words
        """
        if not self.grid or not self.dictionary:
            return []

        self._found_words = []

        word_set = {word.upper() for word in self.dictionary}
        trie_root = self._build_prefix_trie(self.dictionary)
        self._max_path_chars = max(len(w.upper()) for w in self.dictionary)

        for i in range(self.rows):
            for j in range(self.cols):
                visited = set()
                self._dfs(i, j, "", visited, word_set, trie_root)

        return sorted(set(self._found_words))

    @staticmethod
    def _build_prefix_trie(dictionary):
        """Trie for uppercase prefixes; True marks end of a dictionary word."""
        root = {}
        for w in dictionary:
            node = root
            for ch in w.upper():
                node = node.setdefault(ch, {})
            node[True] = True
        return root

    @staticmethod
    def _trie_has_prefix(root, s):
        node = root
        for ch in s:
            if ch not in node:
                return False
            node = node[ch]
        return True

    def solution(self):
        """Same as getSolution()."""
        return self.getSolution()

    def _get_tile_length(self, tile):
        """Letter count contributed by a tile (special bigrams = 2)."""
        if _normalize_tile_key(tile) in self._SPECIAL:
            return 2
        return 1

    def _get_tile_letters(self, tile):
        """Letters represented by a tile (e.g. Qu -> QU)."""
        return tile.upper()

    def _is_valid_position(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def _get_neighbors(self, row, col):
        neighbors = []
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if self._is_valid_position(new_row, new_col):
                neighbors.append((new_row, new_col))

        return neighbors

    def _path_letter_count(self, path):
        """Count letters along path (QU/ST/IE pairs count as two letters)."""
        i = 0
        count = 0
        while i < len(path):
            two = path[i:i + 2]
            if two in ("QU", "ST", "IE"):
                count += 2
                i += 2
            else:
                count += 1
                i += 1
        return count

    def _dfs(self, row, col, current_path, visited, word_set, trie_root):
        position = (row, col)
        visited.add(position)

        tile = self.grid[row][col]
        tile_letters = self._get_tile_letters(tile)
        new_path = current_path + tile_letters
        new_path_upper = new_path.upper()

        too_long = len(new_path_upper) > self._max_path_chars
        if too_long or not self._trie_has_prefix(trie_root, new_path_upper):
            visited.remove(position)
            return

        letters = self._path_letter_count(new_path_upper)
        if new_path_upper in word_set and letters >= 3:
            self._found_words.append(new_path_upper)

        for neighbor_row, neighbor_col in self._get_neighbors(row, col):
            neighbor_pos = (neighbor_row, neighbor_col)
            if neighbor_pos not in visited:
                self._dfs(
                    neighbor_row,
                    neighbor_col,
                    new_path,
                    visited,
                    word_set,
                    trie_root,
                )

        visited.remove(position)


def main():
    grid = [
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["IE", "J", "K", "L"],
        ["A", "B", "C", "D"],
    ]

    dictionary = ["ABEF", "AFJIEEB", "DGKD", "DGKA"]

    mygame = Boggle(grid, dictionary)
    print(mygame.solution())


if __name__ == "__main__":
    main()
