
# Binary Search in Python


def binary(arr, item):
	start = 0
	end = len(arr) - 1

	while (start <= end):
		mid = start + (end - start) // 2
		mid_val = arr[mid]

		if mid_val == item:
			return mid

		elif item < mid_val:
			end = mid - 1

		else:
			start = mid + 1

	return None


print(binary([3,5,7,2,5,4,8,9,4], 2))
