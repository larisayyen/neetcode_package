
# sudoku validator

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
