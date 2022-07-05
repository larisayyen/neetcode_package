
from heapq import heappush,heappop,heapify

class minHeap:

    def __init__(self,k) -> None:
        self.heap = []
        self.size = k

    # keep the bigger node
    def push(self,val):

        # pushs the elements into the minHeap if the heap size is less than k
        if len(self.heap) < self.size:
            heappush(self.heap,val)

        # push the element into the heap if it is greater than the root node
        elif val > self.heap[0]:
            heappop(self.heap)
            heappush(self.heap,val)

    # a method to return the root node
    def ans(self):
        return self.heap[0]

class KthLargest:

    def __init__(self,k,nums):

        self.nums = minHeap(k)
        self.k = k
        for i in nums:
            self.nums.push(i)

    def add(self,val):

        # add number into the stream and return the Kth largest
        self.nums.push(val)

        return self.nums.ans()

# last stone weight

def lastStoneWeight(stones):
    '''
    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
    At the end of the game, there is at most one stone left.
    '''
    stones = [-s for s in stones]
    heapify(stones)

    while len(stones) > 1:
        first = heappop(stones)
        second = heappop(stones)
        if second > first:
            heappush(stones,first - second)

    stones.append(0)
    return abs(stones[0])
