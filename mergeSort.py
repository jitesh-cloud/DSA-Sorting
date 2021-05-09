# Following code is sorting techinque using Merge sort algorithms
"""
Merge Sort is Divide & Conquer based algorithm, like its Cousin Quick Sort. The
main idea of merge sort is to divide large data-sets into smaller sets of data,
and then solve them. Merge Sort is a recursive algorithm, it divides the given
array into smaller halves and the calls itself repeatedly to solve them.

Time Complexity ---
Best/Average/Worst ==> O(n logn)  //remains same for all test cases

Space Complexity ---
O(n)
"""
# Merge Sorting algorithm
def MergeSort(arr):
    # Condition - lets say len(arr)=5, consider arr = [8,12,3,6,5]
    # If len(arr)>1 //True ==> 5>1
    if len(arr)>1:

        # Assign new variable Mid which is middle term
        # Middle term can be achieved by absolute dividing len(arr) in two parts
        # Absolute division in python ==> len(arr)//2 ==> returns int always
        # 5//2 ==> 2 ==> Array will be divided into 2 elements and 3 elements
        mid = len(arr)//2

        # L will contain first part of Array ==> 2 Elements
        # L = [8,12]
        L = arr[:mid]
        # R will contain second part of Array ==> 3 Elements
        # R = [3,6,5]
        R = arr[mid:]

        # L array will go in the recursion and again same steps
        MergeSort(L)
        # Same R will also go in recursion
        MergeSort(R)

        # For checking and sorting steps further we will have to assign some more variables
        # i, j and k assigned to 0
        i=j=k=0

        # while loop for comparing L & R elements
        # while len(L&R)>i&j respectively this loop will run
        while i < len(L) and j < len(R):

            # L[0] and R[0] are compared for first tym... and goes on
            # L[0]=8 and R[0]=3 ==> arr[0]=3 and more iterations upto len(l..or..R) != 0
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        # Here remaining places will be filled by iterating the two separately
        # L array while len(L) greater than i and i&k are increasing gradually by 1
        while i<len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        # R array while len(R) greater than j and j&k are increasing gradually by 1
        while j<len(R):
            arr[k] = R[j]
            j+=1
            k+=1


# User can dynamically put in all the array elements by choice
array = list(map(int,input("Enter array Elements: ").strip().split()))

# MergeSort function call by giving array as argument to it!
MergeSort(array)

# Printing all the array elements in the sorted form //Sorting Completed!!!
print("Sorted Array: ",[array[i] for i in range(len(array))])
