
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]


def productExceptSelf(nums):

    res = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    print(res)

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res
