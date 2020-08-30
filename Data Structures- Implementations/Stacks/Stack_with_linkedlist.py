
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class Stack:
	def __init__(self):
		self.top = None
		self.bottom = None
		self.length = 0


	def peek(self):     # Returns the top element
		print(self.top)


	def push(self, item):      # Adding element at the top
		newNode = Node(item)
		if (self.length == 0):
			self.top = newNode
			self.bottom = newNode
		else:
			initialTop = self.top
			self.top = newNode
			self.top.next = initialTop

		self.length += 1
		return self

 
	def pop(self):        # Removing the top element
		if (self.top is None):
			return None
		if (self.top == self.bottom):
			self.bottom = None

		initialTop = self.top
		self.top = self.top.next
		self.length -= 1
		return self




s = Stack()
s.push("Google")
s.push("YouTube")
s.push("Discord")
s.push("GitHub")
s.pop()
print(s.length)
s.peek()



