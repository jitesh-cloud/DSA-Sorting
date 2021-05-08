# Following code is Bubble sorting technique to carry out sorting in an Array
# It checks the elements in pairs and sort it.
"""
- The algorithm starts with comparing the first pair of elements
- If the first element is smaller than the second one, then the elements are interchanged, otherwise remains intact
- This algorithm is not suitable for large data sets

Time Complexity ---
O(n^2)
Best Case ==> O(n) //already sorted
"""

def BubbleSort(arr):
    n = len(arr)

    # Traversing through all array elements
    for o in range(n-1):
    # range(n) also works but outer loop will repeat one time more than it's needed

       # Last o elements are already placed
        for p in range(0,n-o-1):
            # Traverse the array from 0 to n-o-1 //if n=5 o=1 ==> 3 times
            # Swapping of element if found greater than next one
            if arr[p] > arr[p+1]:
                arr[p], arr[p+1] = arr[p+1], arr[p]

array = list(map(int, input("Enter array elements: ").strip().split()))

BubbleSort(array)

print("Sorted Array is: ")
for i in range(len(array)):
    print(f"{array[i]}",end=" ")
print()
