def merge_arrays(array1: list, array2: list) -> list:
    """
    this merge works only because two arrrays are sorted
    otherwise we would be able to insert numbers in the order
    how they located inside two arrays
    eg
    a1 = [1, 2, 3, 4]
    a2 = [5, 6, 7, 8, 9]
    we can iterate through both arrays and just remember pointer
    to the last element
    but
    a1 = [1, 2, 3, 4]
    a2 = [5, 4, 2.5, 3.5, 9]
    here if we start our merge
    we'll encounter with problem we need to insert 4 between 1 and 5
    so we need somehow perform it and loose our arrays order
    """
    pointer1 = pointer2 = 0
    merged_array = []

    # here OR instead of AND won't work because it'll cause
    # error on if condition
    while pointer1 < len(array1) and pointer2 < len(array2):
        if array1[pointer1] < array2[pointer2]:
            merged_array.append(array1[pointer1])
            pointer1 += 1
        else:
            merged_array.append(array2[pointer1])
            pointer2 += 1

    while pointer1 < len(array1):
        merged_array.append(array1[pointer1])
        pointer1 += 1

    while pointer2 < len(array2):
        merged_array.append(array2[pointer2])
        pointer2 += 1

    return merged_array


ordered1 = [12, 15, 18, 21]
ordered2 = [13, 14, 22]
result = merge_arrays(ordered1, ordered2)
print(result)
