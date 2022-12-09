
import collections

# sudoku validator

## solution_1

valid_set = list(range(1,10))

def sudoku_validator(grid):

    # given a whole set of grid
    def valid_rows(grid):

        for row in grid:
            if sorted(row) != valid_set:
                return False

        return True

    def valid_columns(grid):

        # index in range(0,9)

        for i in range(0,9):
            col = []
            for j in range(0,9):
                col.append(grid[i][j])
            if sorted(col) != valid_set:
                return False

        return True

    def valid_boxes(grid):

        # split the each row and column in 3 squares
        for r in range(0,9,3):
            for c in range(0,9,3):
                square = []

                for i in range(0,3):
                    i += r

                    for j in range(0,3):
                        j += c

                        square.append(grid[i][j])
                if sorted(square) != valid_set:
                    return False

        return True

    return valid_rows(grid) and valid_columns(grid) and valid_boxes(grid)


## solution_2

def isValidSudoku(board):

    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):

            ### check if it is "."
            if board[r][c] == ".":
                continue
            ### check if it is in the dict, if yes then has repetition
            if (
                board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in squares[(r//3,c//3)]
            ):
                return False

            ### add to dict if it is not checked
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r//3,c//3)].add(board[r][c])

    return True



# sudoku solver

def valid(grid,num,pos):

    # valid_row
    for i in range(len(grid)):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # valid_col
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # valid_box
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if grid[i][j] == num and (i,j) !=pos:
                return False

    return True


def find_empty(grid):

    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == 0:
                return (r,c)
    return None

def solve(grid):

    find = find_empty(grid)
    if not find: return True
    row,col = find

    for i in range(1,10):
        if valid(grid,i,(row,col)):
            grid[row][col] = i

            # backtrack
            if solve(grid):
                return True

            grid[row][col] = 0

    return False

def sudoku_solver(grid):

    if not isinstance(grid,list):
        return 'invalid grid'

    for row in grid:
        if len(row) != 9:
            return 'invalid grid'

    if len(grid) != 9:
        return 'invalid grid'

    solve(grid)

    return grid
