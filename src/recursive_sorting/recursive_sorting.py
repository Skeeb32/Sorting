# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    # put back together here
    # Sorting happens here

    a = 0
    b = 0 

    for k in range(0, elements):
        # What do we do in here?
        # Compare a and b
        # if a is out of range, push b and iterate
        if a >= len(arrA): # we're done with a, push B
            merged_arr[k] = arrB[b]
            b += 1
        # if b is out of range, push a and iterate
        elif b >= len(arrB): # we're done with a, push B
            merged_arr[k] = arrA[a]
            a += 1
        # if a is bigger, put it in an array and iterate both
        elif arrA[a] < arrB[b]: # we're done with a, push B
            merged_arr[k] = arrA[a]
            a += 1
        # if b is smaller put it in an array and iterate both
        else:
            merged_arr[k] = arrB[b]
            b +=1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # Split here
    # base condition
    # if array size >= 1
    if len(arr) > 1:
    # find the middle of arr
    # sort stuff in left and put it in put stuff to the left in left
        left = merge_sort(arr[0: len(arr) // 2])
    # sort to the right in the right in the right
        right = merge_sort(arr[len(arr) // 2:])

    # Merge left and right
        arr = merge(left, right)

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