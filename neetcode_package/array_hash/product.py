
def productExceptSelf(nums):

    res = [1] * (len(nums))

    prefix = 1

    # get the product from first
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
        print(prefix)
        print(res)

    postfix = 1

    # get the product from last
    for i in range(len(nums) -1 , -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
        print(postfix)

    return res

nums = [1,2,3,4]
print(productExceptSelf(nums))
