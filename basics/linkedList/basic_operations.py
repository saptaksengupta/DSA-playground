class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head

        while (temp):
            print(temp.data, end=' ')
            temp = temp.next
    
    def prependNode(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def appendNode(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = newNode


if __name__ == "__main__":
    myList = SinglyLinkedList()

    myList.head = Node(5)
    myList.head.next = Node(6)
    myList.prependNode(3)
    myList.appendNode(11)
    myList.printList()
        
    


    

    