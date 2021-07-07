def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    initial = 0
    last = len(arr) - 1
    

    while initial <= last:
        mid = (initial  + last) // 2
       
        if arr[mid] < target:
            initial = mid + 1

        elif arr[mid] > target:
            last = mid - 1
        else:
            return mid    

    return -1  # not found


    


    


    