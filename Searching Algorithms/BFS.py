
# Breadth First Search

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


class BinarySearchTree:
	def __init__(self):
		self.root = None


		def bfs(self):
			currentNode = self.root
			li = []
			queue = []
			queue.append(currentNode)

			while (len(queue) > 0):
				currentNode = queue[0]
				del queue[0]
				li.append(currentNode.value)

				if (currentNode.left):
					queue.append(currentNode.left)
				if (currentNode.right):
					queue.append(currentNode.right)

			return li


		def recursivebfs(self, queue, li):
			if (len(queue) == 0):
				return li

			currentNode = queue[0]
			del queue[0]
			li.append(currentNode.value)

			if (currentNode.left):
					queue.append(currentNode.left)
			if (currentNode.right):
					queue.append(currentNode.right)


			return recursivebfs(self, queue, li)



 