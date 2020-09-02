

def selectionsort(arr):
    i = 0
    while (i < len(arr)):
        min = arr[i]
        temp = i
        for j in range(i+1,len(arr)):
          if arr[j] < min:
            temp = j
            min = arr[j]
        arr[i] , arr[temp] = arr[temp] , arr[i]
        i += 1
    
    return arr

print(selectionsort([8,6,5,0,4,3,2]))
