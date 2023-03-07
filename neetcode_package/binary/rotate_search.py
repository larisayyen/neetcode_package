
from typing import List

def search_s1(nums: List[int], target: int) -> int:

    if not nums:
        return -1
    
    l,r = 0,len(nums) - 1

    while l <= r:

        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        if nums[0] <= nums[mid]:
            if nums[0] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        else:
            if nums[mid] < target <= nums[len(nums) - 1]:
                l = mid + 1
            else:
                r = mid - 1

    return -1

def search_s2(nums:List[int],target:int) ->int:
        
    l, r = 0, len(nums) - 1

    while l <= r:

        mid = (l + r) // 2
        if target == nums[mid]:
            return mid

        # left sorted portion
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        # right sorted portion
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1