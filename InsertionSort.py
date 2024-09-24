#insertion sort
def insertionSort(arr):
    #creates a copy of the testcase array in order to prevent any other algorithms from being affected by the changes made
    arrCopy = []
    arrCopy += arr
    n = len(arrCopy)
    #return the arr if it only has 0 or 1 element since it is already sorted
    if n <= 1:
        return arrCopy

    #iterates through the array starting at the second element
    for i in range(1, n):
        #store current element in the variable key that will be inserted into the right positions
        key = arrCopy[i]
        j = i-1
        #this while loop will mvoe elements greater than one key position ahead
        while j >= 0 and key < arrCopy[j]:
            #here we shift all elements to the right to account for the insertion
            arrCopy[j+1] = arrCopy[j]
            j -= 1
        #inserts the key
        arrCopy[j+1] = key
    return arrCopy


