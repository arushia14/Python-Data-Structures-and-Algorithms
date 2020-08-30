class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class Queue:
	def __init__(self):
		self.first = None
		self.last = None
		self.length = 0


	def peek(self):     # Returns the first element
		print(self.first)


	def enqueue(self, item):      # Adding an element to the queue
		newNode = Node(item)
		if (self.length == 0):
			self.first = newNode
			self.last = newNode
		else:
			self.last.next = newNode
			self.last = newNode

		self.length += 1
		return self

 
	def dequeue(self):        # Removing the first element
		if (self.first is None):
			return None
		if (self.first == self.last):
			self.last = None

		self.first = self.first.next
		self.length -= 1
		return self


q = Queue()
q.enqueue("Harry")
q.enqueue("Ron")
q.enqueue("Hermoine")
q.dequeue()
print(q.length)






