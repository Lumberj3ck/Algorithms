import random
from dataclasses import dataclass
from collections import namedtuple


def bubble_sort(unordered_list: list) -> list:
    for i in range(len(unordered_list)):
        for j in range(i, 0, -1):
            if unordered_list[j - 1] > unordered_list[j]:
                unordered_list[j - 1], unordered_list[j] = (
                    unordered_list[j],
                    unordered_list[j - 1],
                )
    return unordered_list


Index = namedtuple(
    "Index",
    [
        "index",
    ],
)
result_index = Index(index=213).index

# @dataclass
# class Index:
#     """binary_search result"""
#     item_index: int
# key 5
#  0 1 2 3 4
#  1 2 3 4 5
#  middle 2 it is not the key


def binary_search(ordered_list: list, key: int) -> Index:
    last_searching_index = len(ordered_list) - 1
    first_searching_index = 0

    while first_searching_index <= last_searching_index:
        middle = (last_searching_index + first_searching_index) // 2
        print(first_searching_index, last_searching_index, middle)
        if ordered_list[middle] == key:
            return Index(index=middle)
        elif ordered_list[middle] < key:
            first_searching_index = middle + 1
        else:
            last_searching_index = middle - 1

    if first_searching_index > last_searching_index:
        return Index(index=-1)

    return Index(index=-1)

ordered_list = sorted([random.randint(1, 500) for _ in range(10)])
key = ordered_list[2]
print(ordered_list, "====", key)
output = binary_search(ordered_list, key)
print(output, 2)
# print(ordered_list, sorted(unordered_list) == ordered_list)
