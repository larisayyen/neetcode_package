
# check time
## time python ...

import random
import sys
from neetcode_package.algorithms.utils.load import load_numbers

numbers = load_numbers(sys.argv[1])
# print(numbers)

# bogo_sort
# verify sorted or not
def is_sorted(values):
    for index in range(len(values)-1):
        if values[index] > values[index+1]:
            return False
    return True

# sort func
def bogo_sort(values):
    attempt = 0
    while not is_sorted(values):
        print(attempt)
        random.shuffle(values)
        attempt += 1
    return values

# print(bogo_sort(numbers))

# selection_sort
def selection_sort(values):
    '''
    take O(n2) time
    '''
    sorted_list = []
    # print("%-25s %-25s" % (values,sorted_list))

    for i in range(len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
        # print("%-25s %-25s" % (values,sorted_list))

    return sorted_list

# picks out the min
def index_of_min(values):
    min_index = 0
    for i in range(1,len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index

# print(selection_sort(numbers))

# recursion
def sum(numbers):

    if not numbers:
        return 0

    # print("calling sum(%s)" % numbers[1:])
    remains = sum(numbers[1:])
    # print("call to sum(%s) return %d + %d" % (numbers,numbers[0],remains) )
    return numbers[0] + remains

# print(sum([1,2,3,4,5]))

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

# print(quick_sort(numbers))

# merge_sort
def merge_sort(values):
    '''
    take O(n log(n))
    '''
    if len(values) <= 1:
        return values

    mid = len(values) // 2

    left_values = merge_sort(values[:mid])
    right_values = merge_sort(values[mid:])

    print("%15s %-15s" % (left_values,right_values))

    sorted_values = []

    left_index = 0
    right_index = 0

    while left_index < len(left_values) and right_index < len(right_values):

        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1

    sorted_values += left_values[left_index:]
    sorted_values += right_values[right_index:]
    return sorted_values

# print(merge_sort(numbers))
