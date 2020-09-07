
# Fibonacci series using iterative method

def fibonacci(num):
	  n = 0
	  n1 = 1
	  li = [n, n1]
	  for i in range(0, num-1):
		    n2 = n + n1
		    li.append(n2)
		    n = n1
		    n1 = n2
	  
	  return li


print(fibonacci(20))


# Fibonacci series using Recursion

def fiboRecursion(num):
	  if (num <= 1):
	    	return num
	    	
	  ans = (fiboRecursion(num - 1) + fiboRecursion(num - 2))
	  return ans  


print(fiboRecursion(20))

