# Following code is a sorting of an array using Quick Sort Algorithm
"""
Quick Sort aka Partition-Exchange Sort is works on the principle of Divide and Conquer

In Quick Sort, we start with dividing a list into two halves based on pivot element, on
one side we have all smaller elements than pivot and greater on the other. It uses recursion
by calling itself again and again until sorted array is obtained.

Steps ---
1. Choose an element as a pivot from array. We can choose any element from the Array
- Pick First one as pivot
- Pick Last one as pivot
- Pick Randomly any as pivot
- Pick median one as pivot
2. Reoder array so that elements less than pivot placed before it and greater elements after it.
After final positioning we get solid position of pivot to be fixed in array. This operation is
called partition operation
3. Recusively apply step 1 & 2 to the sub-array i.e for the smaller values array and greater
values array

Time Complexity ---
Best/Average ==> O(n logn)
Worst ==> O(n^2)
"""
def partition(start, end, arr):

    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:

        while start < len(arr) and arr[start] <= pivot:
            start+=1

        while arr[end] > pivot:
            end-=1

        if(start < end):
            arr[start], arr[end] = arr[end], arr[start]


    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]

    return end

def QuickSort(start, end, arr):

    if (start < end):

        p = partition(start, end, arr)

        QuickSort(start, p-1, arr)
        QuickSort(p+1, end, arr)

array = list(map(int,input("Enter array elements :").strip().split()))
QuickSort(0, len(array)-1, array)

print(f"Sorted Array: {array}")
