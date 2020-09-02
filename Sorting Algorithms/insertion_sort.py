
def insertion(arr):
	for i in range(1, len(arr)):
		value = arr[i]
		temp = i

		while (temp > 0 and arr[temp-1] > value):
			arr[temp] = arr[temp-1]
			temp = temp-1

		arr[temp] = value

	return arr


print(insertion([4,6,8,2,5,4]))