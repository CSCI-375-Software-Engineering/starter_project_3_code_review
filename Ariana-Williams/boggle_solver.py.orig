def boggle_solver(board, dictionary):
    rows, cols = len(board), len(board[0])
    found_words = set()

    def dfs(r, c, visited, current_word):
        if (r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited):
            return

        visited.add((r, c))
        current_word += board[r][c]

        if current_word in dictionary:
            found_words.add(current_word)

        # explore all 8 directions
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    dfs(r + dr, c + dc, visited, current_word)

        visited.remove((r, c))

    for i in range(rows):
        for j in range(cols):
            dfs(i, j, set(), "")

    return found_words