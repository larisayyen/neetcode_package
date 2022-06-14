
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
