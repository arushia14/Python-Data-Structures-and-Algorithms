
# Bubble Sort in Python

def bubblesort(array):
    length = len(array) - 1

    for i in range(length):
        for j in range(length):
             if (array[j] > array[j+1]):
                 temp = array[j]
                 array[j] = array[j+1]
                 array[j+1] = temp
    
    return array

print(bubblesort([4,6,8,3,5,9,0,2,5,7]))