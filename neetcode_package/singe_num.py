
def singleNumber(nums):
    res = 0 # XOR : n^0 = n , 0 ^0 = 0
    for n in nums:
        res = n ^ res
    return res

def num_of_1(n):
    res = 0
    while n:
        res += n%2
        n = n >>1
    return res

def count_bit(n):
    dp = [0] * (n+1)
    ans = [0]
    offset = 1

    for i in range(1,n+1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
        return dp

def reverse_bit(n):
    res = 0

    for i in range(32):
        bit = (n >> i) & 1
        res += (bit << (31 -i))

    return res

def missing_num(nums):
    res = len(nums)

    for i in range(len(nums)-1):
        res += (i - nums[i])

    return res
