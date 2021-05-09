# Following code is sorting of array using Insertion sort
"""
- Consider that there are 5 elements in an array which are to be sorted.
- First, we consider the 0th index as sorted part and the rest is unsorted.
- Then we compare the next element of the array, if the first element is smaller
than second element then we swap the elements, otherwise we place the element after
the first element.
- Thus each time we insert element the sorted array becomes larger and unsorted
becomes smaller, and the new element is to be compare with all the previous elements
of the sorted array and adjust the element just next to its smaller element.
- We repeat this process till all the elements in array become part of the sorted
array.

Time Complexity ---
Best ==> O(n)
Average/Worst ==> O(n^2)
"""

def InsertionSort(arr):

    #Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        value = arr[i]

        #Move elements of arr[0..i-1], that are greater than key, to one pos. ahead
        hole = i
        while hole>0 and arr[hole-1]>value:
            arr[hole] = arr[hole-1]
            hole -= 1
        arr[hole] = value


array = list(map(int, input("Enter array elements: ").strip().split()))
InsertionSort(array)

print("Sorted array is: ",[array[i] for i in range(len(array))])
