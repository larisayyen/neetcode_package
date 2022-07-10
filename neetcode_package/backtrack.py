

# subset
class Solution(object):
    '''
    nums is a list
    return a list[list]
    '''
    def subsets(self, nums):

        nums.sort()
        res = [[]]
        res.append(list(nums))
        for ls in range(1, len(nums)):
            self.get_subsets(res, nums, [], ls, 0)
        return res

    def get_subsets(self, res, nums, curr_set, ls, index):
        # recursive
        if ls == 0:
            res.append(list(curr_set))
        elif index < len(nums):
            curr_set.append(nums[index])
            self.get_subsets(res, nums, curr_set, ls - 1, index + 1)
            curr_set.pop()
            self.get_subsets(res, nums, curr_set, ls, index + 1)

class Solution:
    def subsets(self, nums):
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return res

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1, subset)
        backtrack(0, [])
        return res

# word search

class Solution:
    def exist(self, board, word):
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or (r, c) in path):
                return False
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False

    # O(n * m * 4^n)
