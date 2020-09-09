"""

Given 2 arrays, check which element is missing in the second array.

"""

def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for n1,n2 in zip(arr1, arr2):
        if (n1 != n2):
            return n1

    return arr1[-1]

    

print(finder([1,2,3,4,5,6,7],[3,7,2,1,4,6]))












