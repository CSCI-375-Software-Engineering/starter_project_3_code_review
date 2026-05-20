def boggle_solver(board, dictionary):
    """
    Finds all valid words in a Boggle board using depth-first search.

    Args:
        board (list): 2D list representing the Boggle board.
        dictionary (set): Set of valid dictionary words.

    Returns:
        set: A set containing all valid words found on the board.
    """

    rows = len(board)
    cols = len(board[0])

    # Store all discovered valid words
    found_words = set()

    def dfs(row, col, visited_cells, current_word):
        """
        Recursively explores neighboring cells to build words.

        Args:
            row (int): Current row position.
            col (int): Current column position.
            visited_cells (set): Cells already visited in current path.
            current_word (str): Current word being formed.
        """

        # Check if position is outside board boundaries
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return

        # Prevent revisiting the same cell
        if (row, col) in visited_cells:
            return

        # Mark current cell as visited
        visited_cells.add((row, col))

        # Add current letter to the word
        current_word += board[row][col]

        # Check if current word exists in dictionary
        if current_word in dictionary:
            found_words.add(current_word)

        # Explore all 8 neighboring directions
        for row_offset in [-1, 0, 1]:
            for col_offset in [-1, 0, 1]:

                # Skip current cell
                if row_offset == 0 and col_offset == 0:
                    continue

                dfs(
                    row + row_offset,
                    col + col_offset,
                    visited_cells,
                    current_word
                )

        # Backtrack by removing current cell
        visited_cells.remove((row, col))

    # Start DFS from every cell on the board
    for row in range(rows):
        for col in range(cols):
            dfs(row, col, set(), "")

    return found_words
