
import sys
from neetcode_package.algorithms.utils.load import load_strings

names = load_strings(sys.argv[1])

search_names = ['david','sheri','darren','serena']

# linear search
def index_of_item(collection,target):

    for i in range(len(collection)):
        if target == collection[i]:
            return i
    return None

# for n in search_names:
#     index = index_of_item(names,n)
#     print(index)

# quick sort
def quick_sort(values):
    '''
    choose a pivot num
    split into less_than and greater_than
    choose pivot num for each sublist
    repeat the split

    take best O(n log(n)) or worst O(n2)
    '''

    if len(values) <= 1:
        return values

    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]

    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)

    # print("%15s %1s %-15s" % (less_than_pivot,pivot,greater_than_pivot))

    return quick_sort(less_than_pivot) + [pivot] +quick_sort(greater_than_pivot)

# sort the names
# sorted_names = quick_sort(names)
# for n in sorted_names:
#     print(n)


# binary search
def binary_search(collection,target):

    first = 0
    last = len(collection)

    while first <= last:
        mid = 1 + ((last - 1)//2)

        res = (target == collection[mid])

        if res == 0:
            return mid-1

        if res > 0:
            first = mid +1
        else:
            last = mid -1

    return -1

for n in search_names:
    index = binary_search(names,n)
    print(index)
