
def merge_sort(l):
    '''
    sort a list in ascending order
    return a new sorted list

    divide: find the mid and divide into sublists
    conquer: recursively sort the sublists
    combine: merge the sorted sublists

    takes overall O(kn log(n)) time
    '''

    if len(l) <= 1:
        return l

    # divide
    left_half,right_half = split(l)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(l):
    '''
    divide the unsorted list ar mid into sublist
    return 2 lists -- left and right
    takes overall O(k log(n)) time
    '''

    mid = len(l) // 2

    left = l[:mid]
    right = l[mid:]

    return left,right

def merge(left,right):
    '''
    merge two lists, sorting them in the process
    return a new merged list
    takes overall O(n log(n)) time
    '''

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    # left or right not of the same length
    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(l):

    n = len(l)

    if n == 0 or n == 1:
        return True

    return l[0] < l[1] and verify_sorted(l[1:])


# alist = [4,61,24,63,3,53]
# res = merge_sort(alist)
# print(res)
# print(verify_sorted(alist))
# print(verify_sorted(res))
