class Node:
    def __init__(self, val: int, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self) -> None:
        self.length = 0
        self.head: Node | None = None
        self.tail: Node | None = None

    def remove(self, item: int):
        curr = self.head
        for idx in range(0, self.length):
            if curr.val == item:
                break
            curr = curr.next

        # came to the end of the list
        if not curr:
            return
        
        self.length -= 1
        if this.length == 0:
            self.head = self.tail = 0

        if 1 < idx < self.length:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            curr.prev = None
            curr.next = None

        elif idx == 0:
            curr.next.prev = None
            self.head = curr.next

        elif idx == self.length - 1:
            curr.prev.next = None
            self.tail = curr.prev
            curr.prev = None

        return curr.val


    def append(self, item):
        self.length += 1
        new_node = Node(item)
        if not self.tail:
            self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def insert_at(self, item: int, idx: int):
        if idx > self.length:
            raise Exception("this node doesn't exist")
        elif idx == self.length:
            self.append(item)
            return
        elif idx == 0:
            self.prepend(item)
            return
        self.length += 1
        new_node = Node(item)

        curr = self.head

        for _ in range(0, idx):
            curr = curr.next

        # second approach
        # curr_idx = 0
        # while curr_idx <= idx:
        #     curr_idx += 1
        #     curr = curr.next
        node = curr

        prev = node.prev
        node.prev = new_node
        prev.next = new_node

        new_node.prev = prev
        new_node.next = node

    def prepend(self, item: int):
        new_node = Node(item, None)

        self.length += 1
        if not self.head:
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node

        self.head = new_node
