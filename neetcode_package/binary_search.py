
def search(nums, target) -> int:
    '''
    nums is a list of numbers in ascending order,
    target is a number
    return the index of target in the list
    otherwise return -1
    '''
    if target not in nums:
        return -1
    else:
        for i,n in enumerate(nums):
            if n == target:
                return i

def searchMatrix(matrix, target) -> bool:
    '''
    search the integer in a matrix
    '''
    bool_list = []

    for row in matrix:
        if target in row:
            bool_list.append(1)
        else:
            bool_list.append(0)

    if 1 in bool_list:
        return True
    else:
        return False

def minEatingSpeed(piles, h) -> int:
    '''
    Return the minimum integer k
    such that she can eat all the bananas within h hours.
    '''

    start, end = 1,max(piles) # lower bound, upper bound
    k = 0  # return value

    while start < end:
        mid = (start + end) // 2

        totalTime = 0

        for p in piles:
            totalTime += ((p-1)//mid) +1 # check time

        if totalTime <= h:
            k = mid
            end = mid -1 # decrease upper bound
        else:
            start = mid +1 # increase lower bound

    return k

def pivot_search(nums,target):
    '''
    Given the array nums after the possible rotation and an integer target,
    return the index of target if it is in nums, or -1 if it is not in nums.
    '''

    if target not in nums:
        return -1
    else:
        for i,n in enumerate(nums):
            if n == target:
                return i

def findMin(nums) -> int:
    '''
    Given the sorted rotated array nums of unique elements,
    return the minimum element of this array.
    '''

    num_sorted = sorted(nums)
    return min(num_sorted)


class TimeMap:

    def __init__(self):

        self.keyStore = {} # {key : [val, timestamp]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
