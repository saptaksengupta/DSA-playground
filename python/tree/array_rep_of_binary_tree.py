class BinaryTreeArray: 
    
    root = 0
    binaryArrayList = ['-'] * 10

    def setRoot(self, value):
        self.binaryArrayList[self.root] = value

    def setLeftChild(self, value, parent):
        rootIndex = self.getIndexByValue(parent)
        if self.binaryArrayList[rootIndex] != '-':
            self.binaryArrayList[2 * rootIndex + 1]  = value
    

    def setRightChild(self, value, parent):
        rootIndex = self.getIndexByValue(parent)
        if self.binaryArrayList[rootIndex] != '-':
            self.binaryArrayList[2 * rootIndex + 2] = value
    
    def printArrayList(self):
        for i in range(len(self.binaryArrayList)):
            print(self.binaryArrayList[i], end='')

    def getIndexByValue(self, value):
        return self.binaryArrayList.index(value)
    
bTreeObj = BinaryTreeArray()

bTreeObj.setRoot('A')
bTreeObj.setRightChild('C', 'A')
bTreeObj.setLeftChild('B', 'A')

bTreeObj.printArrayList()

# output
# ABC-------