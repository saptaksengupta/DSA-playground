from heapq import heappush, heappop
import sys
class MinHeap:

    def __init__(self):
        self.heap = []

    def parent(self, i):
        # print('parent of', i, 'is: ', int((i - 1) / 2))
        return int((i - 1) / 2)
    
    def insertKey(self, k):
        heappush(self.heap, k)

    def extractMin(self):
        return heappop(self.heap)

    def decreaseKey(self, key, newVal):
        self.heap[key] = newVal
        while key != 0 and (self.heap[self.parent(key)] > self.heap[key]):
            self.heap[self.parent(key)], self.heap[key] = self.heap[key], self.heap[self.parent(key)]
    
    def deleteKey(self, key):
        # First decrease the value to make it a last element
        # Then Extract minimum element
        self.decreaseKey(key, float("-inf"))
        self.extractMin()

    def getMin(self):
        return self.heap[0]

    def printHeap(self):
        print(self.heap)

heapObj = MinHeap() 
heapObj.insertKey(7) 
heapObj.insertKey(4)
heapObj.insertKey(6) 
heapObj.insertKey(10) 


heapObj.printHeap()
heapObj.decreaseKey(2, 1) 
print(heapObj.getMin())
heapObj.printHeap()
heapObj.deleteKey(0)
heapObj.printHeap()
# print(heapObj.extractMin())
# print(heapObj.getMin())