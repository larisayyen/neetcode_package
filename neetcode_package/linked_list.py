
# Definition for singly-linked list.
class ListNode:
    '''
    ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}} ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
    '''

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def reverseList(self,head):

        prev,curr = None,head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def mergeTwoLists(list1, list2):

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

    def hasCycle(head)->bool:

        slow,fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
