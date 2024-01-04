class Node:
    def __init__(self, value=None, next=None):
        self.next = next
        self.value = value


class Head:
    def __init__(self, head=None):
        self.head = head

    def represent_list(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next

    def reverse(self):
        curr = self.head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev
        return self.head


a = Node(value="humm")
b = Node(value="burger")
d = Node(value="cheese")
a.next = b
b.next = d
new_head = Head(head=a)
new_head.represent_list()
print("-----------")
new_head.reverse()
new_head.represent_list()
