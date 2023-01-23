
def maxArea(height):
    '''
    given a list of heights,output the max area
    '''
    l,r = 0,len(height) - 1
    res = 0

    while l<r:
        res = max(res,min(height[l],height[r]) * (r - l))

        if height[l] < height[r]:
            l += 1
        elif height[r] <= height[l]:
            r -= 1

    return res

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))


def trapWater(height):
    '''
    given a list of heights,compute how much water it can trap after raining
    '''

    if not height:
        return 0

    l,r = 0,len(height)-1
    lMax,rMax = height[l],height[r]
    res = 0

    while l<r:
        if lMax < rMax:
            l += 1
            lMax = max(lMax,height[l])
            res += lMax - height[l]

        else:
            r -= 1
            rMax = max(rMax,height[r])
            res += rMax - height[r]

    return res
