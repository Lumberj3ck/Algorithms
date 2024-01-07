import random


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


resp = factorial(5)


# 1, 1, 2, 3, 5
cache = {}


def fibonaci(n):
    print("fib", n)
    if n in (1, 2):
        return 1
    else:
        return fibonaci(n - 1) + fibonaci(n - 2)


def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n - 1, auxiliary, destination, source)


def frac(a, n):
    if n == 1:
        return a**0.5
    else:
        return (a * frac(a, n - 1)) ** 0.5


def sum(*args):
    if len(args) == 0:
        return 0
    args = list(args)
    arg = args.pop()
    return arg + sum(*args)


print(sum(1, 2, 3, 4, 5, 6))
# Merge sort implementation


# fa  3  27  38 43
# sa  9  10  82
# algorithm to merge to sorted arrays into one sorted array
def merge(first_array: list, second_array: list) -> list:
    merged_array = []
    if first_array[0] > second_array[0]:
        first_array, second_array = second_array, first_array
    for index, elem in enumerate(first_array):
        next_insertion = index + 1
        current_index = index
        cycle = False

        while (
            next_insertion < len(first_array)
            and current_index < len(second_array)
            and first_array[current_index] > second_array[current_index]
        ):
            merged_array.append(second_array[current_index])
            current_index += 1
            cycle = True
        if (
            not cycle
            and next_insertion < len(second_array)
            and next_insertion < len(first_array)
            and first_array[next_insertion] > second_array[index]
        ):
            if second_array[index] > first_array[index]:
                merged_array.extend([first_array[index], second_array[index]])
            else:
                merged_array.extend([second_array[index], first_array[index]])
            continue
        merged_array.append(first_array[index])

    if len(merged_array) < len(second_array + first_array):
        diff = len(second_array) - (len(second_array + first_array) - len(merged_array))
        merged_array += second_array[diff:]
        print(diff)
    return merged_array


# first = sorted([random.randint(1, 100) for i in range(5)])
# second = sorted([random.randint(1, 100) for i in range(5)])
# # resp = merge([3, 27, 38, 43], [9, 10, 82])
# print(first, "-----------", second)
# first = [-10, 5, 76, 90, 99]
# second = [-4, 43, 61, 65, 74]
# resp = merge(first, second)
# print(resp, resp.__len__())
