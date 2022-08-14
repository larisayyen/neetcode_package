
from re import L
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
    '''
    start from nums[0],the value is the max jump steps to go
    determine whether we can reach the last value
    '''
    goal = len(nums) - 1

    for i in range(len(nums) - 1,-1,-1):
        if i + nums[i] >= goal:
            goal = i

    return True if goal == 0 else False

def jump(nums):
    '''
    assume you can always get to the last value
    '''
    l,r = 0,0
    res = 0

    while r < (len(nums) - 1):
        maxJump = 0

        for i in range(l,r+1):
            maxJump = max(maxJump,i + nums[i])

        l = r + 1
        r = maxJump
        res += 1

    return res
