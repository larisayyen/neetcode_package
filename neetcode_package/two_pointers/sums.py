
from operator import indexOf


def twoSums_simple(nums,target):

    # use enumerate to iterate through a list
    index_d = {}

    for i,n in enumerate(nums):
        d = target - n
        if d in index_d:
            return [index_d[d],i]
        index_d[n] = i

def twoSums_advance(nums,target):

    # create index to iterate through a list from both sides
    a,b = 0,len(nums)-1

    while a<b:
        sum = nums[a] + nums[b]

        if sum > target:
            b -=1
        elif sum < target:
            a += 1
        else:
            return [a+1,b+1]

def threeSums(nums):

    res = []
    nums.sort()

    for i,n in enumerate(nums):

        if i > 0 and n == nums[i-1]:
            continue

        a,b = i+1, len(nums)-1
        while a<b:
            sum = n + nums[a] + nums[b]
            if sum > 0:
                b -= 1
            elif sum < 0:
                a += 1
            else:
                res.append([n,nums[a],nums[b]])
                a += 1
                while nums[a] == nums[a-1] and a < b:
                    a += 1

    return res
