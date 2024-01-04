class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self, head: Node = None, tail: Node = None):
        self.head = head
        self.tail = tail

    def deque(self):
        if self.head:
            head = self.head
            self.head = self.head.next
            head.next = None
            return head.val
        return None

    def peek(self):
        if self.head:
            return self.head.val
