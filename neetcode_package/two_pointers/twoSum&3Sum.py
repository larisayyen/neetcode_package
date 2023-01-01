
def twoSum(numbers,target):
    '''
    numbers is a sorted list
    target is a number
    '''
    l,r = 0,len(numbers) - 1

    while l < r:
        lr = numbers[l] + numbers[r]

        if lr == target:
            return [l+1 , r+1]
        elif lr < target:
            l += 1
        else:
            r -= 1

    raise ValueError("No solution found.")

numbers = [2,7,11,15]
target = 9

print(twoSum(numbers,target))

def threeSum(numbers):
    '''
    return 3 nums that sum up as 0
    '''
    res = []
    numbers.sort()

    for i , v in enumerate(numbers):
        if i > 0  and v == numbers[i -1]: # check duplicates
            continue

        l,r = i +1,len(numbers) - 1
        while l < r:
            sum_ = v + numbers[l] + numbers[r]
            if sum_ > 0:
                r -= 1
            elif sum_ < 0:
                l += 1
            else:
                res.append([v,numbers[l],numbers[r]])
                l += 1
                while numbers[l] == numbers[l -1] and l< r:
                    l += 1
    return res
