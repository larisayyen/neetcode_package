
import heapq
from collections import Counter


def topKfrequent_s1(nums,k):
    '''
    find the top k frequent elements in the nums list
    '''
    topK_dict = {}

    for i in nums:
        if i in topK_dict.keys():
            topK_dict[i] += 1
        else:
            topK_dict[i] = 1

    # sort values
    value_sort = sorted(topK_dict.values())
    # print(value_sort)

    return [topK_dict[m] for m in value_sort[-k:]]


# nums = [1,1,1,2,2,3]
# k = 2
# print(topKfrequent_s1(nums,k))

def topKfrequent_s2(nums,k):
    '''
    bucket sort
    '''
    count = {}
    freq = [[] for i in range(len(nums)+1)] # initiate a count array based on the length of the nums list


    # get the count of every element of nums
    for n in nums:
        count[n] = 1 + count.get(n,0)

    # input the element into the freq dict corresponding to its count
    for n,c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq)-1,0,-1): # match the count and k from the last
        for n in freq[i]:
            res.append(n)
            if len(n) == k: # match ends until it reaches k
                return res

def topKfrequent_s3(nums,k):
    '''
    use heapq library
    '''
    res=[]
    dict = Counter(nums)
    for val, count in dict.items():
        if len(res)<k:
            heapq.heappush(res,(count,val))
        else:
            heapq.heappush(res,(count,val))
            heapq.heappop(res)
    return [val for count, val in res]
