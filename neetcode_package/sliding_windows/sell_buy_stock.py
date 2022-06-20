
def maxProfit(prices):

    # define a result,start from 0
    res = 0

    # define left index,start from 0
    l = 0

    # iterate index from 1
    for r in range(1,len(prices)):
        if prices[r] < prices[l]:
            l = r
        res = max(res,prices[r]-prices[l])
    return res
