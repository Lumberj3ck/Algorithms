from queue import Node

class StackNode:
    def __init__(self, val=0, prev=None):
        self.val = val
        self.prev = prev 


class Stack:
    def __init__(self, head) -> None:
        self.head: StackNode | None = head
        self.length = 0
    
    def push(self, val):
        node = StackNode(val)
        self.length += 1
        if not self.head:
            self.head = node
            return
        node.prev = self.head
        self.head = node 
    

    def pop(self):
        self.length = max(0, self.length - 1)
        if self.length == 0:
            node = self.head
            self.head = None
            if node:
                return node.val
            return

        node = self.head
        self.head = self.head.prev
        # free 
        # node.prev = None
        return node.val


    def peek(self):
        if self.head:
