# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # loop through the elements in the unsorted part of the list
        for j in range(smallest_index, len(arr))
        # iterate until the index of the smallest element is found
        if arr[smallest_index] > arr[j]:
            smallest_index = j
        # swap the first element in the unsorted list with the smallest 
        # element in the remainder of the list
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    # return the sorted list
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1):
            # decide whether the number pair should be swapped
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # return the sorted list
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr