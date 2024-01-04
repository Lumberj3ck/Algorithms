def linear_search(array, query):
    for index in range(len(array)):
        if array[index] == query:
            return index

    return -1


def binary_search_new(array: list, query) -> int:
    """
    wrote this as a training exercise
    """
    start_index, end_index = 0, len(array)

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2

        if array[mid_index] == query:
            return mid_index
        elif array[mid_index] < query:
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1

    return -1
            

def binary_search(array: list, query: int, low: int, high: int) -> int:
    if low > high:
        return -1
    mid_index = (low + high) // 2

    if array[mid_index] == query:
        return mid_index
    elif array[mid_index] < query:
        return binary_search(array, query, mid_index + 1, high)
    else:
        return binary_search(array, query, low, mid_index - 1)


ordered_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# print(binary_search_new(ordered_numbers, 5))
