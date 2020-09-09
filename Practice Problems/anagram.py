

# Check whether 2 strings are anagrams


def anagram(s1,s2):
    
    s1.lower()
    s2.lower()
    
    li1 = []
    li2 = []
    
    for i in s1:
        li1.append(i)
        if i == ' ':
            li1.remove(i)
    
    for i in s2:
        li2.append(i)
        if i == ' ':
            li2.remove(i)
        
    li1.sort()
    li2.sort()
    
    if(li1 == li2):
        return True
    else:
        return False

