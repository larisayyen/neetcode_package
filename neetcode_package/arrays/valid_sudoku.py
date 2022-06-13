
# solution 1
VALID_SET = list(range(1, 10))

def valid_rows(grid):
    for row in grid:
        if sorted(row) != VALID_SET:
            return False
    return True

def valid_columns(grid):
    for j in range(0, 9):
        col = []
        for i in range(0, 9):
            col.append(grid[i][j])
        if sorted(col) != VALID_SET:
            return False
    return True

def valid_boxes(grid):
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            square = []
            for i in range(0, 3):
                i += box_row
                for j in range(0, 3):
                    j += box_col
                    square.append(grid[i][j])
            if sorted(square) != VALID_SET:
                return False
    return True


def sudoku_validator(grid):
    return valid_rows(grid) and valid_columns(grid) and valid_boxes(grid)


# solution 2

import collections

def isValidSudoku(board):

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
