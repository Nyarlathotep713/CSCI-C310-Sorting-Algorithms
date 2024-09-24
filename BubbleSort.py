def bubbleSort(arr):
    #creates a copy of the testcase array in order to prevent any other algorithms from being affected by the changes made
    arrCopy = []
    arrCopy += arr
    #outer loop to iterate through the list the necessary n times
    for n in range(len(arrCopy) - 1, 0, -1):

        #this inner loop compares adjacent elements to each other
        for i in range(n):
            #if the current element is greater than the next, they will swap
            if arrCopy[i] > arrCopy[i + 1]:
                #swaps elements
                arrCopy[i], arrCopy[i + 1] = arrCopy[i + 1], arrCopy[i]
    return arrCopy


