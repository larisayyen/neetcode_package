
# array -> python list
new_list = [1,2,3]
res = new_list[0]

## linear search
# if 1 in new_list: print(True)

## insert vs append
nums = []
# nums.append(1)
nums.extend([2,3,4])
del nums[0]

# linked list
## node
class Node:

    def __init__(self,data,next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        return the number of nodes in the list
        takes O(n) time
        """

        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self,data):
        """
        add new node to the head of the list
        take O(n) time
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self,key):
        """
        search for the first node containing data that matches the key
        return the node or None if not found
        takes O(n) time
        """

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current =  current.next_node
        return None

    def insert(self,data,index):
        """
        Insert a new node containing data at index position
        takes O(n) time
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self,key):
        '''
        removes node containing data that matches the key
        return the node or None if key doesn't exist
        takes O(n) time
        '''
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def node_at_index(self,index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        [head:3] -> [2] -> [Tail:1]
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return  '-> '.join(nodes)
