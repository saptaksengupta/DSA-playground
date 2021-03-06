# Generated By lexicon-dsa CLI tool.
# Author: Saptak Sengupta(deeps.sengupta@gmail.com)
# Github: https://github.com/saptaksengupta/

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inOrderTravarsal(node: Node):

    if node.left is not None:
        inOrderTravarsal(node.left)

    print(node.val, end=' ')

    if node.right is not None:
        inOrderTravarsal(node.right)


count = 0
def getNtInorder(node, n):
    global count

    if node is None:
        return

    if count < n: 
        getNtInorder(node.left, n)
        count += 1

        if count == n:
            print(n, 'th node is: ', node.val)
        
        getNtInorder(node.right, n)

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)  
    root.right = Node(30)  
    root.left.left = Node(40)  
    root.left.right = Node(50)

    
    
    inOrderTravarsal(root)
    print('\n')
    n = 5
    getNtInorder(root, n)
    
