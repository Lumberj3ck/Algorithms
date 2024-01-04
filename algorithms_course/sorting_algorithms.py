
def bubble_sort(unordered_array: list) -> list:
    for i in range(len(unordered_array)):
        for j in range(len(unordered_array) - i - 1):
            if unordered_array[j] > unordered_array[j + 1]:
                unordered_array[j], unordered_array[j + 1] = unordered_array[j + 1], unordered_array[j]

    return unordered_array
