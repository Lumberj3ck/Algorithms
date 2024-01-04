import random


def test_case(test_array_len: int, test_amount: int):
    def actual_decorator(func):
        def inner(*args, **kwargs):
            def tester():
                unsorted_array = [
                    random.randrange(-100, 100) for i in range(test_array_len)
                ]
                response = func(unsorted_array)
                print(unsorted_array, " ----- ", response)
                assert response == sorted(unsorted_array)

            for i in range(test_amount):
                print(f"Test number {i}")
                tester()

        return inner

    return actual_decorator


@test_case(test_array_len=50, test_amount=10)
def bubble_sort(unsorted_array: list):
    for i in range(len(unsorted_array) - 1, 0, -1):
        for j in range(i):
            current = unsorted_array[j]
            next = unsorted_array[j + 1]
            if current > next:
                unsorted_array[j], unsorted_array[j + 1] = (
                    unsorted_array[j + 1],
                    unsorted_array[j],
                )
    return unsorted_array


@test_case(test_array_len=50, test_amount=10)
def insertion_sort(unsorted_array: list):
    for index in range(len(unsorted_array)):
        search_index = index
        inserting_value = unsorted_array[index]

        while search_index > 0 and unsorted_array[search_index - 1] > inserting_value:
            unsorted_array[search_index] = unsorted_array[search_index - 1]
            search_index -= 2
        unsorted_array[search_index] = inserting_value
    return unsorted_array

