class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self, head: Node = None, tail: Node = None):
        self.head = head
        self.tail = tail
        self.length = 0

    def enqueue(self, val):
        node = Node(val)
        self.length += 1
        if not self.tail:
            self.head = self.tail = node
            return val
        
        self.tail.next = node
        self.tail = self.tail.next
        return val


    def deque(self):
        if self.head:
            head = self.head
            self.head = self.head.next
            head.next = None
            self.length -= 1
            return head.val
        return None

    def peek(self):
        if self.head:
            return self.head.val
