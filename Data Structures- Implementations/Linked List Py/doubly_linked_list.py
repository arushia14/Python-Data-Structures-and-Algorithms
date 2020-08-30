
class LinkedList:
	def __init__(self, item):
		self.item = item
		self.head = {
			"value" : self.item,
			"next" : "null",
			"prev" : "null"
		}
		self.tail = self.head
		self.length = 1


	# Adding an element at the end of the list

	def append(self, item):
		newNode = {
			"value": item,
			"next" : "null",
			"prev" : "null"
		}
		newNode["prev"] = self.tail
		self.tail["next"] = newNode
		self.tail = newNode
		self.length += 1
		return self


	# Adding an element at the start of the list

	def prepend(self, item):
		newNode = {
			"value": item,
			"next" : "null",
			"prev" : "null"
		}
		newNode["next"] = self.head
		self.head["prev"] = newNode
		self.head = newNode
		self.length += 1
		return self


	# Inserting an element at an index

	def insert(self, index, item):
		if (index >= self.length):
			return self.append(item)

		newNode = {
			"value": item,
			"next" : "null",
			"prev" : "null"
		}
		first = self.lookupIndex(index-1)
		follower = first["next"]
		first["next"] = newNode
		newNode["prev"] = first
		newNode["next"] = follower
		follower["prev"] = newNode
		self.length += 1
		return self


	def lookupIndex(self, index): # Function to traverse and look for an index
		counter = 0
		currentNode = self.head
		while (counter != index):
			currentNode = currentNode["next"]
			counter += 1
		return currentNode


	# Removing an element at a selected index 

	def remove(self, index):
		first = self.lookupIndex(index-1)
		follower = self.lookupIndex(index+1)
		unwantedNode = first["next"]
		first["next"] = unwantedNode["next"]
		follower["prev"] = unwantedNode["prev"]
		self.length -= 1
		return self



li = LinkedList(5)
li.append(10)
li.append(17)
li.prepend(2)
li.insert(1, 15)
li.remove(1)
print(li.head)
