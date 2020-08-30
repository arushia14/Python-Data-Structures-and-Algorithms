

class LinkedList:
	def __init__(self, item):
		self.item = item
		self.head = {
			"value" : self.item,
			"next" : "null"
		}
		self.tail = self.head
		self.length = 1


	# Adding an element at the end of the list

	def append(self, item):
		newNode = {
			"value": item,
			"next" : "null"
		}
		self.tail["next"] = newNode
		self.tail = newNode
		self.length += 1
		return self


	# Adding an element at the start of the list	

	def prepend(self, item):
		newNode = {
			"value": item,
			"next" : "null"
		}
		newNode["next"] = self.head
		self.head = newNode
		self.length += 1
		return self


	# Inserting an element at an index

	def insert(self, index, item):
		if (index >= self.length):
			return self.append(item)

		newNode = {
			"value": item,
			"next" : "null"
		}
		first = self.lookupIndex(index-1)
		holdPointer = first["next"]
		first["next"] = newNode
		newNode["next"] = holdPointer
		self.length += 1
		return self


	def lookupIndex(self, index):  # Function to traverse and look for an index
		counter = 0
		currentNode = self.head
		while (counter != index):
			currentNode = currentNode["next"]
			counter += 1
		return currentNode


	# Removing an element at a selected index 

	def remove(self, index):
		first = self.lookupIndex(index-1)
		unwantedNode = first["next"]
		first["next"] = unwantedNode["next"]
		self.length -= 1
		return self


	# Reversing a Linked List

	def reverse(self):

		if (self.length == 1):
			return self

		else:
			first = self.head
			tail = self.head
			second = first["next"]
			while second:
				temp = second["next"]
				second["next"] = first
				first = second
				second = temp

			self.head["next"] = "null"
			self.head = first
		return self


li = LinkedList(5)
li.append(10)
li.append(3)
li.append(7)
li.prepend(2)
li.remove(1)
li.insert(1, 15)
print(li)
