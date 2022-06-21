
def dailyTemperatures(temperatures: list) -> list:
    '''
    return an array answer such that answer[i]
    is the number of days you have to wait
    after the ith day to get a warmer temperature
    '''

    res = [0]*len(temperatures)
    stack = []

    for i,t in enumerate(temperatures):

        # find a greater temperature
        while stack and t > stack[-1][0]:

            # pop out the previous temperature
            Temp,Ind = stack.pop()
            # calculate the number of days
            res[Ind] = (i - Ind)

        stack.append([t,i])

    return res
