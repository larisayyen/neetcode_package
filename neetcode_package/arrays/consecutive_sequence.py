
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0

    for n in nums:
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest
