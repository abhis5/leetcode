from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # sanity check
        if not board:
            return False
        visited_cells = set()
        board_len = len(board)
        row_len = len(board[0])
        word_len = len(word)

        def valid_cell(i, j):
            return not (
                i < 0
                or i > board_len - 1
                or j < 0
                or j > row_len - 1
                or (i, j) in visited_cells
            )

        def form_word(i, j, word_idx):
            cells = [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]
            for cell in cells:
                if (
                    valid_cell(*cell)
                    and board[cell[0]][cell[1]] == word[word_idx]
                ):
                    visited_cells.add(cell)
                    if word_idx == word_len - 1:
                        return True
                    if form_word(*cell, word_idx + 1):
                        return True
                    visited_cells.remove(cell)
            return False

        for i in range(board_len):
            for j in range(row_len):
                if board[i][j] != word[0]:
                    continue
                if word_len is 1:
                    return True
                visited_cells = set()
                visited_cells.add((i, j))
                if form_word(i, j, 1):
                    return True
        return False
