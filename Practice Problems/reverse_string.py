
# Reverse a string

def reverse(str):
    arr = []
    i = len(str)-1
    while i >= 0:
        arr.append(str[i])
        i -= 1
        
    return ''.join(arr)
    
    
    
print(reverse("Let's reverse this string"))

