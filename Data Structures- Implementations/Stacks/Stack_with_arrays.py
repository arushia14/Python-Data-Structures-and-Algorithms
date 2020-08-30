
class Stack:
	def __init__(self):
		self.array = []


	def peek(self):      # Returns the top element
		if (len(self.array) == 0):
			return None

		return(self.array[-1])


	def push(self, item):       # Adds an element at the top
		self.array.append(item)
		return self


	def size(self):      # Returns the size or length of the stack
		return len(self.array)


	def pop(self):        # Removes the top element
		self.array.pop()
		return self



s = Stack()
s.push("Pizza")
s.push("Cheesecake")
s.push("Brownies")
s.push("Mac n Cheese")
s.pop()
print(s.peek())
print(s.size())



