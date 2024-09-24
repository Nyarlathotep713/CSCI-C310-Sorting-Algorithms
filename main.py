import BubbleSort
import InsertionSort
import MergeSort
import QuickSort
import RadixSort
import random
import time

#establishes all test cases we will be using for our individual tests
testCase1 = random.choices(range(2147483647), k=1000)
testCase2 = random.choices(range(2147483647), k=10000)
testCase3 = random.choices(range(2147483647), k=100000)
testCase4 = random.choices(range(2147483647), k=1000000)
testCase5 = random.choices(range(2147483647), k=10000000)

#The following will start and stop individual timers in order to time each individual sorting algorithm on how long it takes their respective methods to sort the given randomized test case
start_time = time.time()
# Run your algorithm
MergeSort.mergeSort(testCase5)
# Stop the timer
end_time = time.time()
# Calculate the elapsed time
elapsed_time = end_time - start_time
print("merge sort: " + str(elapsed_time))

start_time = time.time()
# Run your algorithm
QuickSort.quickSort(testCase5)
# Stop the timer
end_time = time.time()
# Calculate the elapsed time
elapsed_time = end_time - start_time
print("quick sort: " + str(elapsed_time))

start_time = time.time()
# Run your algorithm
RadixSort.radixSort(testCase5)
# Stop the timer
end_time = time.time()
# Calculate the elapsed time
elapsed_time = end_time - start_time
print("radix sort: " + str(elapsed_time))

# Start the timer
start_time = time.time()
# Run your algorithm
InsertionSort.insertionSort(testCase5)
# Stop the timer
end_time = time.time()
# Calculate the elapsed time
elapsed_time = end_time - start_time
print("insertion sort: " + str(elapsed_time))

start_time = time.time()
# Run your algorithm
BubbleSort.bubbleSort(testCase5)
# Stop the timer
end_time = time.time()
# Calculate the elapsed time
elapsed_time = end_time - start_time
print("bubble sort: " + str(elapsed_time))


