
from typing import List

def carFleet_s1(target: int, position: List[int], speed: List[int]) -> int:

    '''
    Input: target = 100, position = [0,2,4], speed = [4,2,1]
    Output: 1
    Explanation:
    The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
    Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
    
    source: https://leetcode.cn/problems/car-fleet

    '''

    # sort cars
    cars = sorted(zip(position,speed))

    # check ascending time
    time = [float(target - p) / s for p,s in cars]

    team = 0

    while len(time) > 1:
        lead = time.pop()
        
        if lead < time[-1]: # a team will be formed if the arrival time of lead is smaller than the other one
            team += 1
        else: 
            time[-1] = lead

    return team + bool(time)

def carFleet_s2(target: int, position: List[int], speed: List[int]) -> int:

    n = len(position) # get how many cars
    stack = []
    cars = zip(position,speed)
    cars = sorted(cars,reverse=True)

    time = [0]*n # get cars' arrival time
    for i in range(n):
        time[i] = (target - cars[i][0]) / cars[i][1]

    for i in range(n):
        m = time[i]
        if stack and stack[-1] >= time[i]:
            m = stack[-1]
            stack.pop()
        stack.append(m)

    return len(stack)

def carFleet_s3(target: int, position: List[int], speed: List[int]) -> int:

    '''reverse simulation'''

    n,team = len(position),1
    g =[(position[i],speed[i]) for i in range(n)]

    g.sort(reverse=True)

    cur = (target - g[0][0]) / g[0][1]

    for i in range(1,n):
        if target - g[i][0] / g[i][1] > cur:
            cur = target - g[i][0] / g[i][1]

            team += 1

    return team
