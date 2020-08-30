

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class BinarySearchTree:
	def __init__(self):
		self.root = None


# Function to insert a new node in the tree

	def insert(self, value):
		newNode = Node(value)
		if (self.root == None):
			self.root = newNode
		else:
			currentNode = self.root

			while True:
				if (value < currentNode.value):
					if (currentNode.left is None):
						currentNode.left = newNode
						return self
					currentNode = currentNode.left
				else:
					if (currentNode.right is None):
						currentNode.right = newNode
						return self
					currentNode = currentNode.right


# Function to search for a node in the tree

	def search(self, value):
		if (self.root is None):
			return False
		else:
			currentNode = self.root

			while (currentNode):
				if (value < currentNode.value):
					currentNode = currentNode.left
				elif (value > currentNode.value):
					currentNode = currentNode.right
				elif (currentNode.value == value):
					return currentNode




tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(3)
tree.insert(15)
tree.insert(20)
print(tree.search(15))
print(tree)














