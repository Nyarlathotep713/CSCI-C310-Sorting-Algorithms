#Radix Sort Program
#counting sort of array by the given digit
def countSort(arrCopy, digit):
    n = len(arrCopy)

    #this output array will be what we store the sorted array within
    output = [0] * (n)

    #initialize the array as 0
    count = [0] * (10)

    #store occurences in count[]
    for i in range(0, n):
        index = (arrCopy[i]/digit)
        count[int((index)%10)] += 1

    #change count[i] so that it contains the proper position of the digits in the output array
    for i in range(1, 10):
        count[i] += count[i-1]

    #Create and build the output (sorted) array
    i = n-1
    while i >= 0:
        index = (arrCopy[i]/digit)
        output[count[int((index)%10)] - 1] = arrCopy[i]
        count[int((index)%10)] -= 1
        i -= 1

    #Now copying the outputted arry to the original array (arr) so that the original array is now sorted
    i = 0
    for i in range(0, len(arrCopy)):
        arrCopy[i] = output[i]

def radixSort(arr):
    #creates a copy of the testcase array in order to prevent any other algorithms from being affected by the changes made
    arrCopy = []
    arrCopy += arr
    #determine the maximum number within the array
    maxNum = max(arrCopy)

    #use the countSort function for every digit
    #Instead of passign the digit number, we use exp which represents 10^i, where i is the current digit num within the array
    exp = 1
    while maxNum // exp > 0:
        countSort(arrCopy, exp)
        exp *= 10

    return arrCopy

