
from linked_list import LinkedList

def merge_sort(ll):
    '''
    sorts a linked list in ascending order
    - recursively divide the linked list into sublists containing a single node
    - repeatedly merge the sublists to produce sublists until one remains

    return a sorted linked list
    runs in O(kn log(n)) time
    '''

    if ll.size() == 1:
        return ll

    elif ll.head is None:
        return ll

    left_half ,right_half = split(ll)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)


def split(ll):
    '''
    divide the unsorted list at mid into sublists
    takes O(k log(n)) time
    '''

    if ll == None or ll.head == None:
        left_half = ll
        right_half = None

        return left_half,right_half

    else:
        size = ll.size()
        mid = size // 2

        mid_node = ll.node_at_index(mid - 1)

        # two distinct sublists divided by mid
        left_half = ll
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half,right_half

def merge(left,right):
    '''
    merges two linked lists,sorting by data in nodes
    return a new, merged list
    runs in O(n) time
    '''

    # create a new linked list that contains nodes from merging left and right
    merged = LinkedList()

    # add a fake head that is discarded later
    merged.add(0)

    # set current to the head of the linked list
    current = merged.head

    # obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # iterate over left and right until we reach the tail node of either
    while left_head or right_head:

        # if the head of left is None,we will pass the tail
        # add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # call next on right to set loop condition to false
            right_head = right_head.next_node

        # if the head node of right is None,we will pass the tail
        # add the node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # call next on left to set loop condition to false
            left_head = left_head.next_node

        else:
            # not at either tail node obtain node data
            left_data = left_head.data
            right_data = right_head.data

            # if data on left is less than right,set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # move left head to next_node
                left_head = left_head.next_node
            # if data on left is greater than right,set current to left node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        # move current to next node
        current = current.next_node

    head = merged.head.next_node
    merged.head = head

    return merged

# l = LinkedList()
# l.add(10)
# l.add(2)
# l.add(44)
# l.add(15)
# l.add(200)

# print(l)
# sorted_linked_list = merge_sort(l)
# print(sorted_linked_list)
