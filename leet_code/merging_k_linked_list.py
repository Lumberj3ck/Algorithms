import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linked_list(list):
    curr = list
    while curr:
        print(curr.val)
        curr = curr.next


def create_linked_list(n):
    nodes = [ListNode(val=i) for i in sorted([random.randint(1, 10) for _ in range(n)])]
    root = nodes.pop(0)
    current = root
    while nodes:
        current.next = nodes.pop(0)
        current = current.next
    return root


def reverseList(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp


def mergeKLists(lists: list[Optional[ListNode]]):
    curr = dummy = ListNode()

    while len(lists) > 1:
        head_values = [
            link_list.val if link_list else lists.remove(link_list)
            for link_list in lists
        ]
        if not head_values:
            break
        minimum_index = head_values.index(min(head_values))
        minimum_node = lists[minimum_index]
        curr.next = minimum_node
        curr = curr.next

        if minimum_node.next:
            lists[minimum_index] = minimum_node.next
        else:
            lists.pop(minimum_index)

    if lists:
        curr.next = lists.pop()

    return dummy.next


# lists = [create_linked_list(3) for _ in range(random.randint(1, 5))]
# for list in lists:
#     print_linked_list(list)
#     print("-------------")
lists1 = [None, None]
merged_list = mergeKLists(lists1)
print_linked_list(merged_list)
