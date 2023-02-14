# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot
import time
from colors import *

# Function to find the partition position
def partition(array, low, high):

	# choose the rightmost element as pivot
	pivot = array[high]

	# pointer for greater element
	i = low - 1

	# traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1

# function to perform quicksort


def quickSort(data, low, high, drawData, timeTick):
    if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
        pi = partition(data, low, high)

        # Recursive call on the left of pivot
        quickSort(data, low, pi - 1, drawData, timeTick)

        # Recursive call on the right of pivot
        quickSort(data, pi + 1, high, drawData, timeTick)
        
        drawData(data, [PURPLE if x >= low and x < pi else LIGHT_GREEN if x == pi else RED if x > pi and x <= high else BLUE for x in range(len(data))])
        time.sleep(timeTick)
    
    drawData(data, [BLUE for _ in range(len(data))])
        