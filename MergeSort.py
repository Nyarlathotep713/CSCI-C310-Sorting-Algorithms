#Merge sort, other divide and conquer
#breaks down an array into smaller arrays, sorts them, then merges them back together
def mergeSort(arr):
    #creates a copy of the testcase array in order to prevent any other algorithms from being affected by the changes made
    arrCopy = []
    arrCopy += arr

    #if the length of the array is 0 or 1, it will return the array as it will already be sorted
    if len(arrCopy) <= 1:
        return arrCopy

    mid = len(arrCopy) // 2 #sets the middle as half of the length
    left = arrCopy[:mid] #sets the left half of the array as anything within the array before the mid point
    right = arrCopy[mid:] #sets the right half of the array as anything within the array after the mid point

    sortedLeft = mergeSort(left) #runs the merge sort to indivudally sort the left side first
    sortedRight = mergeSort(right) #runs the merge sort function to sort the right side individually

    return merge(sortedLeft, sortedRight) #returns the function merge of the already sorted right and left arrays

def merge(left, right):
    sortedArr = [] #defines the array that we will be putting all of the sorted values into
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]: #if the current value in the left array is less than the value than the right array, move the right value to the left side
            sortedArr.append(left[i])
            i += 1
        else:
            sortedArr.append(right[j]) #if the current value in the lest array is greater than the value in the right array, move the left value to the right side
            j += 1

    sortedArr.extend(left[i:]) #add the sorted left side of the array to the sorted array variable
    sortedArr.extend(right[j:]) #add the sorted right side of the array to the sorted array variable

    return sortedArr #return the fully sorted array
