

class DynamicArray:
    def __init__(self):
        self.length = 0
        self.data = {}


    def get(self,index):      # Get the element from a particular index
        return self.data[index]

    def push(self, item):     # Add the item to the end of the array
        self.data[self.length] = item
        self.length += 1
        return self.length


    def pop(self):            # Remove last item from the array
        lastItem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return lastItem


    def delete(self, index):   # Delete the element at a particular index
        item = self.data[index]
        self.shiftItems(index)  


    def shiftItems(self, index):     # Creating the function to shift all the indices after deleting an element 
        for i in range(index, self.length-1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length-1]
        self.length -= 1


arr = DynamicArray()
