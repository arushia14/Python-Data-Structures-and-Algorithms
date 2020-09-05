
# Depth First Search


class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class BinarySearchTree:
	def __init__(self):
		self.root = None



	def inorder(self, currentNode, li):
		if (currentNode.left):
			self.inorder(node.left, li)
		li.append(currentNode.value)
		if (currentNode.right):
			inorder(currentNode.right, li)
		return li


	def postorder(self):
		if (currentNode.left):
			self.inorder(node.left, li)
		li.append(currentNode.value)
		if (currentNode.right):
			inorder(currentNode.right, li)
		li.append(currentNode.value)
		return li
		

	def preorder(self):
		li.append(currentNode.value)
		if (currentNode.left):
			self.inorder(node.left, li)
		li.append(currentNode.value)
		if (currentNode.right):
			inorder(currentNode.right, li)
		return li



	

