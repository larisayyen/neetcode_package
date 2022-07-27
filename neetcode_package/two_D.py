
def uniquePaths(m,n):
    '''
    from top-left corner to bottom-right corner
    only move in two dirs - down or right
    result = sum(d+r)
    '''

    # from bottom row -> 0+1
    row = [1] * n

    for i in range(m - 1):
        newrow = [1] * n
        for j in range(n - 2,-1,-1):
            newrow[j] = newrow[j + 1] + row[j]
        row = newrow

    return row[0]
