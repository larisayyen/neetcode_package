
# dynamic programming

def climbStairs(n):
    '''
    how many distinct ways to climb to the top?
    BRUTE FORCE
    O(n)
    '''

    # already step out 1 and then step 1 or 2 --> result in 2,3
    one ,two = 1,1
    for i in range(n - 1):

        # start from bottom --> bottom up --> fabonacci
        ## how many steps to get from 5 to 4 -->1
        ## from step 5 to 3 --> 1+1 = 2
        ## from step 5 to 2 --> 1+2 = 3

        temp = one
        one = one + two
        two = temp

    return one


def minCostClimb(cost_array):
    '''
    You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
    Once you pay the cost, you can either climb one or two steps.
    '''
    #[10,15,20,0]

    cost_array.append(0)

    for i in range(len(cost_array) -3,-1,-1):
        # 15+20,or 15+0
        # 10+15,or 10+20
        cost_array[i] = min(cost_array[i] + cost_array[i+1],cost_array[i] + cost_array[i+2])

    return min(cost_array[0],cost_array[1])
