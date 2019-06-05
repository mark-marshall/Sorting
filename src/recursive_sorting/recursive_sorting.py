# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # create new array of combined arrA and arrB size
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # loop over elements
    for i in range(0, elements):
        if len(arrA) == 0:
            # add from the front of arrB
            merged_arr[i] = arrB[0]
            del arrB[0]
        elif len(arrB) ==  0:
            # add from the front of arrA
            merged_arr[i] = arrA[0]
            del arrA[0]
        elif arrA[0] < arrB[0]:
            # add from the front of arrA
            merged_arr[i] = arrA[0]
            del arrA[0]
        else:
            # add from the front of arrB
            merged_arr[i] = arrB[0]
            del arrB[0]
    return merged_arr

def merge_sort( arr ):
    # recursively split the array into pairs
    if len(arr) > 1:
        left = merge_sort(arr[0 : len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2 :])
        # merge and sort the array
        arr = merge(left, right)
    # return the sorted array
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
