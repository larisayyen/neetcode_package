
from socket import RCVALL_MAX


def water(height):

    a,b = 0,len(height)-1
    w = 0

    while a<b:
        w = max(w,min(height[a],height[b])*(b-1))

        if height[a] < height[b]:
            a += 1
        elif height[a] >= height[b]:
            b -= 1

    return w

def advanced_water(height):

    if not height:
        return 0

    a,b = 0,len(height)-1
    w = 0

    l_max,r_max = height[a],height[b]

    while a < b:
        if l_max < r_max:
            a += 1
            l_max = max(l_max,height[a])
            w += l_max - height[a]
        else:
            b -= 1
            r_max = max(r_max,height[b])
            w += r_max - height[b]
    return w
