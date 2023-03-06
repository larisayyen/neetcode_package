from typing import List
import math
import bisect

def minEatingSpeed_s1(piles:List[int],h:int) -> int:
    l,r = 1,max(piles)
    res = max(piles)

    while l<r:

        k = (l+r) // 2

        totalTime = 0

        for p in piles:
            totalTime += math.ceil(p/k) # ((p-1)//k) +1
        if totalTime <= h:
            res = min(res,k)
            r = k - 1
        else: 
            l = k + 1
    return res

def minEatingSpeed_s2(piles:List[int],h:int) -> int:

    l,r = 1,max(piles) + 1

    while l < r:
        
        k = l + (r - l)// 2

        total = sum([math.ceil(p/k) for p in piles])

        if total <= h:
            r = k
        else: 
            l = k + 1

    return l


def minEatingSpeed_s3(piles: List[int], h: int) -> int:
    return bisect.bisect_left(range(max(piles)), -h, 1, key=lambda k: -sum((pile + k - 1) // k for pile in piles))


'source:https://leetcode.cn/problems/koko-eating-bananas/solution/ai-chi-xiang-jiao-de-ke-ke-by-leetcode-s-z4rt/'
'binary search tutorial:https://www.runoob.com/python3/python-binary-search.html'