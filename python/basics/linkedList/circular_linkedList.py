class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:

    def __init__(self):
        self.head = None

    def printCircularList(self):

        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next
            if temp == self.head:
                break
            
if __name__ == "__main__":
    myList = CircularLinkedList()

    myList.head = Node(5)
    myList.head.next = Node(6)
    myList.head.next.next = Node(7)
    myList.head.next.next.next = myList.head
    myList.printCircularList() 