

class Hashtable:
	def __init__(self, size):
		self.size = size
		self.map = [None] * self.size


	def _hash(self, key):     # Simple hashing function for the keys
		hash = 0
		for char in str(key):
			hash += ord(char)
		return hash % self.size


	def add(self, key, value):    # Adding a new key-value pair in the hashmap
		key_hash = self._hash(key)
		key_value = [key, value]

		if self.map[key_hash] is None:
			self.map[key_hash] = list([key_value])
			return True

		else:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					pair[1] = value
					return True
			self.map[key_hash].append(key_value)
			return True


	def get(self, key):         # Getting a value based on key
		key_hash = self._hash(key)
		if self.map[key_hash] is not None:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					return pair[1]
		return None



	def delete(self, key):        # Deleting a pair from the hashmap
		key_hash = self._hash(key)
		if self.map[key_hash] is None:
			return False
		for i in range(0, len(self.map[key_hash])):
			if self.map[key_hash][i][0] == key:
				self.map[key_hash].pop(i)
				return "True"


	def keys(self):               # Getting all the keys from the hashmap
		keysList = []
		for item in range(0, len(self.map)):
			if self.map[item] is not None:
				keysList.append(self.map[item][0][0])
		return keysList



	def showAll(self):             # Printing all the pairs in the hashmap
		for item in self.map:
			if item is not None:
				print(item)
		return ''


hmap = Hashtable(6)
hmap.add("Peter", '18')
hmap.add("Tony", '40')
hmap.add("Natasha", '35')
hmap.add("Steve", '37')
hmap.delete("Peter")
print(hmap.get("Natasha"))
print(hmap.keys())
print(hmap.showAll())















