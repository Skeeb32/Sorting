# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    leftindex = 0
    rightindex = 0
    # TO-DO
    while(leftindex < len(arrA) and rightindex < len(arrB)):
        if(arrB)[rightindex] > arrA[leftindex]:
            merged_arr.append(arrA[leftindex])
            leftindex += 1
        else:
            merged_arr.append(arrB)[rightindex]
            rightindex += 1

    return merged_arr
print(merge)

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # (base case) If the array is empty or length 1, return
    if len(arr)>1:
        #spints the array into half
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[:mid]

        #recrusion
        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1
        while i < len(righthalf):
            arr[k]=lefthalf[j]
            j=j+1
            k=k+1
# Merge them back together 
# Compare the first values of each arra, add smaller of hte 2 to result 
    return arr
print(merge_sort)


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
