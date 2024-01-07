#   Array of one element is already sorted by defenition
#  func quick_sort(arr, lo, hi)
#       pivot = lo
#       if lo == hi:
#             return
#       split_into_halves(pivot, lo, hi)
#       from lo to hi
#       if el is > pivot:
#           swap
#       remember about index_of_pivot
#       that is going to help us split the array into halves 
#       compare every num in arr to pivot 
#       swap if greater
#       quick_sort(arr, lo, index_of_pivot)
#       quick_sort(arr, index_of_pivot, hi)

#   so how the partition func works
#   loop over
#   from lo to hi 
#   swap num which is lower than pivot
#   swap with pivot index number increase idx
#   so f.ex in arr no lower numbers than pivot we just swap idx = 0 with pivot and that it 
#   

def partition(arr, lo, hi):
    # idx = lo - 1
    idx = lo 
    pivot = arr[hi]

    for i in range(lo, hi):
        print(arr)
        if arr[i] <= pivot:
            arr[i], arr[idx] = arr[idx], arr[i]
            idx += 1

    # idx += 1
    arr[hi] = arr[idx]
    arr[idx] = pivot
    return idx

def quick_sort(arr, lo, hi):
    if lo >= hi:
        return

    pivot_index = partition(arr, lo, hi)
    print(lo, hi)
    # excluding pivot from the partition
    # it already sorted
    quick_sort(arr, lo, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, hi)


arr = [4, 5, 1, 2, 7, 6, 3]
        
        
