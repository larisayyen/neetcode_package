
from tkinter import N


def maxSubArray(nums):
    '''
    largest subtotal of nums
    '''
    res = nums[0]

    total = 0
    for i in nums:
        total += i
        res = max(res,total)

        if total < 0:
            total = 0

    return res

def canJump(nums):
    pass
