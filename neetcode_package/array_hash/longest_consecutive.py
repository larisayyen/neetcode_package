
# solution 1
def longestConsecutive_s1(nums):

    # drop duplicates
    numset = set(nums)
    longest = 0

    for i in nums:

        # check if i is the start of our sequence

        if (i - 1) not in numset:
            length = 1

            # check if i+1 is in our set
            while (i+length) in numset:
                length += 1

            # get our longest length
            longest = max(length,longest)

    return longest

# solution 2
def longestConsecutive_s2(nums):

    '''
    Given an unsorted array of integers nums
    return the length of the longest consecutive elements sequence.
    '''

    res = []

    sorted_nums = sorted(nums)

    for i in range(len(sorted_nums)):

        if i == len(sorted_nums) - 1:
            break

        if sorted_nums[i] in res:
            i += 1

        else:
            if sorted_nums[i+1] - sorted_nums[i] == 1:
                res.append(sorted_nums[i])
                res.append(sorted_nums[i+1])
    print(res)
    return len(res)




nums_1 = [100,4,200,1,3,2]
nums_2 = [0,3,7,2,5,8,4,6,0,1]
# print(longestConsecutive(nums_1))
# print(longestConsecutive(nums_2))
