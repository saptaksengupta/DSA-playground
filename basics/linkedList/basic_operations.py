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

    def printNumberOfNodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        
        print('Number of nodes in this list is: ', count)
    
    def insertAtGivenPosition(self, data, position):

        if position == 1:
            self.prependNode(data)
            return True
        
        count = 0
        temp = self.head
        while temp:
            count += 1
            if position - 1 == count:
                newNode = Node(data)
                newNode.next = temp.next
                temp.next = newNode
                return True
            temp = temp.next
        
        return False
        

if __name__ == "__main__":
    myList = SinglyLinkedList()

    myList.head = Node(5)
    myList.head.next = Node(6)
    myList.prependNode(3)
    myList.appendNode(11)
    myList.printList() 
    print()
    resp = myList.insertAtGivenPosition(8, 1)
    if resp:
        myList.printList()
    else:
        print('Enter a valid position.')
    


    

    