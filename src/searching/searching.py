# STRETCH: implement Linear Search				
def linear_search(arr, target):
  for i in range(0, len(arr) - 1):
    if arr[i] == target:
      return i
   return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
  if len(arr) == 0:
    return -1 # array empty 
  low = 0
  high = len(arr)-1
  # loop while low remains smaller than high
  while low <= high:
    mp = (low + high) // 2
    # if the el matches return the index
    if arr[mp] == target:
      return mp
    # if the mp is too low, adjust high
    elif arr[mp] > target:
      high = mp
    # if the mp is too high, adjust low
    else:
      low = mp
  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
