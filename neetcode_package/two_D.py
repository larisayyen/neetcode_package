
from this import d


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

def longestCommonSubsequence(text1, text2):
    '''
    solve sub problem
    '''
    dp = [[0 for j in range(len(text2 + 1))] for i in range(len(text1)+1)]

    for i in range(len(text1) - 1,-1,-1):
        for j in range(len(text2) -1,-1,-1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i][j+1],dp[i+1][j])

    return dp[0][0]
