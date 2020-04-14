# TO-DO: Complete the selection_sort() function below 
list = [1, 14, 5, 6, 17, 9, 15, 44, 6, 32]
def selection_sort( arr ):  # If `elements` is a collection, remember it will be passed by reference, not value
    # How many loops will be needed to complete this algorithm?
    # How do we know when we are ready to swap values? 
    # And how do we keep track of which values should be swapped?
    # loop through n-1 elements
    # For every index in the collection from 0 to length-2:
    # Compare the element at the current index, i, with everything on its right to identify the position of the smallest element
    # Swap the element at i with the smallest element
    # i++  
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(smallest_index + 1, len(arr)):
            if arr[cur_index] > arr[j]:
                cur_index = j     
                
        # TO-DO: swap
        # Swap smallest index with current index and repeat
        if cur_index != smallest_index:
            arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

# What, if anything needs to be returned?
    return arr
print(selection_sort(list))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) -1):
            if arr[j] > arr [j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr [j]
    return arr
print(bubble_sort(list))

# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr