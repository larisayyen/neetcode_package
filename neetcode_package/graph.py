
import collections
def numIslands(grid):

    if not grid:
        return 0

    rows,cols = len(grid),len(grid[0])
    visit = set()
    islands = 0

    # iterative search
    def bfs(r,c):

        q = collections.deque()
        visit.add(r,c)
        q.append((r,c))

        while q:
            row,col = q.popleft()
            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            # visit the neighbours
            for dr,dc in directions:
                r,c = row+dr,col+dc

                if (r in range(rows) and
                    c in range(cols) and
                    grid[r][c] == '1'and
                    (r,c) not in visit):

                    q.append((r,c))
                    visit.add((r,c))

    # iterate through each row and column
    for r in range(rows):
        for c in range(cols):

            # mark the position when there is a '1'
            if grid[r][c] == '1' and (r,c) not in visit:
                bfs(r,c)
                islands += 1

    return islands

def maxAreaOfIsland(grid):
    '''
    find the island with the maximum area
    '''

    row,col = len(grid),len(grid[0])
    visit = set()

    # recursive search
    def dfs(r,c):

        if ( r<0 or r == row or
             c<0 or c == col or
             grid[r][c] == 0 or (r,c) in visit):
            return 0

        visit.add((r,c))

        # return area of all four direction
        return (1+dfs(r+1,c)+
                  dfs(r-1,c)+
                  dfs(r,c+1)+
                  dfs(r,c-1))

    area = 0
    for r in range(row):
        for c in range(col):
            area = max(area,dfs(r,c))

    return area
