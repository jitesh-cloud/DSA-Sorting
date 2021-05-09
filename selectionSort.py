# Following code is sorting technique using Selection Sorting algorithm
"""
Selection Sort is a technique where array is sequentially sorted by placing the
smallest or the largest element from the array one after the other in multiple
iterations.

Time Complexity ---
Best ==> O(n^2)
"""

def SelectionSort(arr):
    for i in range(len(arr)-1):
        min = i

        for j in range(i+1, len(arr)):
            if (arr[j]<arr[min]):
                min = j

        arr[min], arr[i] = arr[i], arr[min]


array = list(map(int, input("Enter array elements: ").strip().split()))
SelectionSort(array)

print("Sorted Array: ",[array[i] for i in range(len(array))])
