import sys
class MinHeap:

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.size = 0
        self.heap = [0] * self.maxSize
        self.heap[0] = -1 * sys.maxsize
        self.FRONT = 1
    
    def parent(self, pos):
        return pos // 2
    
    def leftChild(self, pos):   
        # as 'one' is the leading index
        return (2 * pos)
    
    def rightChild(self, pos):
        # as 'one' is the leading index
        return (2 * pos) + 1
    
    def swap(self, firstPos, secPos):
        self.heap[firstPos], self.heap[secPos] = self.heap[secPos], self.heap[firstPos]
    
    # return true if passed position is a Leaf Node
    def isLeaf(self, pos):
        if pos > (self.size // 2) and pos < self.size:
            return True
        return False

    
    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.heap[pos] > self.heap[self.leftChild(pos)] or 
                self.heap[pos] > self.heap[self.rightChild(pos)]):

                # swap the current parent node with it's 
                # younger child

                if self.heap[self.leftChild(pos)] < self.heap[self.rightChild(pos)]:
                    # swap the current position with the 
                    # left child
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    # swap the current position with the
                    # right child
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))


    def insert(self, element):

        if self.size >= self.maxSize:
            return None # Overloaded
        
        self.size += 1
        self.heap[self.size] = element

        current = self.size

        while self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
        

    def minHeap(self):
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)

    def remove(self):
        popped = self.heap[self.FRONT]
        self.heap[self.FRONT] = self.heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)

        # Storing the popped element 
        # into the last of the heap
        self.heap[self.size + 1] = popped
        return popped

    def print(self):
        
        for i in range(1, self.size // 2 + 1):
            print(
                "PARENT : " + str(self.heap[i]) + 
                " Left Child: " + str(self.heap[i * 2]) + 
                " Right Child: " + str(self.heap[(i * 2) + 1])
            ) 


if __name__ == "__main__":
    print('The Min Heap is: ')
    minHeap = MinHeap(15) 
    minHeap.insert(5) 
    minHeap.insert(3) 
    minHeap.insert(17) 
    minHeap.insert(10) 
    minHeap.insert(84) 
    minHeap.insert(19) 
    minHeap.insert(6) 
    minHeap.insert(22) 
    minHeap.insert(9) 
    minHeap.minHeap() 

    minHeap.print()

    minHeap.remove()
    print()
    minHeap.print()