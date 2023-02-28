
from typing import List

def searchMatrix_s1(matrix: List[List[int]], target: int) -> bool:

    '''
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true
    '''

    r,c = len(matrix),len(matrix[0]) # get row and columns
    i,j = 0, (r*c) - 1 # get index

    while i <= j:
        mid = (i+j) // 2 # mid index

        mid_num = matrix[mid//c][mid % c] # mid value

        if mid_num == target:
            return True
        if mid_num < target:
            i = mid + 1
        else:
            j = mid - 1

    return False

def searchMatrix_s2(matrix: List[List[int]], target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])

    top, bot = 0, ROWS - 1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break

    if not (top <= bot):
        return False
    row = (top + bot) // 2
    l, r = 0, COLS - 1
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False