#Quick sort, divide and conquer
def quickSort(arr):
    #creates a copy of the testcase array in order to prevent any other algorithms from being affected by the changes made
    arrCopy = []
    arrCopy += arr
    #if the length of the array is either 0 or 1, it will return the array as it is already sorted
    if len(arrCopy) <= 1:
        return arrCopy

    else:
        #sets the pivot point as the first value in the array
        pivot = arrCopy[0]

        #determines if the value within the nested for loop is on the left or right side of the pivot value and assigns accordingly
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        #returns the sorted array
        return quickSort(left) + [pivot] + quickSort(right)


