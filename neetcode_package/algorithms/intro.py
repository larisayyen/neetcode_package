
# linear search O(n):
    ## starts from the beginning
    ## compare current to target
    ## move sequentially
    ## reach end of the list

    ## problem -> input and output -> correct
    ## finite number of time -> efficiency
        ### running time -> time complexity
        ### memory -> space complexity

# binary search O(log(n)):
    ## target left or right -> subset
    ## sort values -> start from middle -> more efficient

# O(n) -> measures the worst performance
    ## runtime -> log/ linear/ quasilinear/ quatric/ cubic/ polynomial/ exponential

# linear search
def linear_search(list,target):
    '''
    return the index of the target in list
    else return None
    '''
    # for i in range(len(list)):
    #     if list[i] == target:
    #         return i
    # return None

    for i,n in enumerate(list):
        if n == target:
            return i
    return None

def verify(index):
    if index is not None:
        print('Target found at index: ',index)
    else:
        print('Target not found in list')

nums = [1,2,3,4,5,6]

result = linear_search(nums,6)
verify(result)

# binary search
def binary_search(list,target):

    # define position
    first = 0
    last = len(list) - 1

    # loop
    while first <= last:
        # calculate mid point
        mid = (first + last) // 2

        if list[mid] == target:
            return mid
        elif list[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return None

result = binary_search(nums,3)
verify(result)

# recursive binary search
def recursive_binary_search(list,target):

    if len(list) == 0:
        return False
    else:
        mid = (len(list)) // 2

        if list[mid] == target:
            return True
        else:
            if list[mid] < target:
                # sublist
                return recursive_binary_search(list[mid+1:],target)
            else:
                return recursive_binary_search(list[:mid],target)

result = recursive_binary_search(nums,3)
verify(result)
