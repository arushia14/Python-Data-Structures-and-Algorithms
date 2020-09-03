
import math

def mergeSort(arr):
	if (len(arr) == 1):
		return arr

	length = len(arr)
	middle = math.floor(length/2)
	left = arr[:middle]
	right = arr[middle:] 

	return merge(mergeSort(left),mergeSort(right))


def merge(left, right):
	result = []
	leftIndex = 0
	rightIndex = 0

	while (leftIndex < len(left) and rightIndex < len(right)):
		if (left[leftIndex] < right[rightIndex]):
			result.append(left[leftIndex])
			leftIndex += 1
		else:
	        result.append(right[rightindex])
	        rightindex += 1
	
	return result + left[leftindex:] + right[rightindex:]

ans = mergeSort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])
print(ans)


