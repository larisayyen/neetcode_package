from typing import List

def findMin_s1(nums: List[int]) -> int:

    '''use binary search to find minimum'''

    l,r = 0,len(nums) - 1

    while l<r:

        mid = (l+r)//2

        if nums[mid] > nums[r]: # which side is in order
            l = mid + 1 #将范围缩小到无序的那一半，因为答案就在那一半。之所以要+1，是因为mid肯定不是最小的那个，至少nums[right]比nums[mid]更小
        else:
            r = mid #这里直接取mid，因为此时mid的左边（包含）是不完全有序的那一半，mid有可能直接是最小值，所以要取mid

    return nums[l]


def findMin_s2(nums: List[int]) -> int:
    L, R = 0, len(nums) - 1
    while L < R:
        if R - L == 1:   #LR相邻时，最小值只存在于LR之间
            break
        mid = int(L+(R-L)/2)
        if nums[mid] > nums[L] and nums[mid] > nums[R]:   #中间值大于两端，则说明最小值在右侧
            L = mid
        elif nums[mid] < nums[L] and nums[mid] < nums[R]: #中间值小于两端，则说明最小值在左侧
            R = mid
        elif nums[L] < nums[mid] < nums[R]:  #中间值介于两者之间，则说明此时已按顺序排列，最小值就是L
            break
    return min(nums[L], nums[R])

# 1.中间值大于等于两端，则说明最小值在右侧,返回left = mid+1
# 2.中间值小于等于两端，则说明最小值在左侧，也有可能是最小值,所以这里返回right = mid
# 3.中间值介于两者之间，则说明此时已按顺序排列 返回right = mid-1

def findMin_s3(nums: List[int]) -> int:    
    low, high = 0, len(nums) - 1
    while low < high:
        pivot = low + (high - low) // 2
        if nums[pivot] < nums[high]:
            high = pivot 
        else:
            low = pivot + 1
    return nums[low]


"source:https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/solution/xun-zhao-xuan-zhuan-pai-xu-shu-zu-zhong-5irwp/"
