
class Graph:
	def __init__(self):
		self.noOfNodes = 0;
		self.adjacentList = {}


	def addVertex(self, node):
		self.adjacentList[node] = []
		self.noOfNodes += 1
		return self


	def addEdge(self, node1, node2):
		self.adjacentList[node1].append(node2)
		self.adjacentList[node2].append(node1)
		return self




g = Graph()
g.addVertex('0')
g.addVertex('4')
g.addVertex('6')
g.addVertex('8')
g.addVertex('2')
g.addEdge('4','8')
g.addEdge('2','4')
g.addEdge('0','6')
print(g)


