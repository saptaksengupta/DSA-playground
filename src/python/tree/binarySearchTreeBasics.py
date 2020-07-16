class Node: 
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


## Util function to insert node at it's correct Position.
def insertNode(root, node): 
    if(root is None):
        root = node
    else: 
        if node.val > root.val:
            if root.right is None:
                root.right = node
            else:
                insertNode(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insertNode(root.left, node)

## Util function to Print all the nodes By Inorder Traversal.
def inorderTraversal(root): 
    if root:
        inorderTraversal(root.left)
        print(root.val)
        inorderTraversal(root.right)

## Util function to Print all the nodes By Preorder Traversal.
def preorderTraversal(root): 
    if root:
        print(root.val)
        preorderTraversal(root.left)
        preorderTraversal(root.right)

## Util function to Print all the nodes By Postorder Traversal.
def postorderTraversal(root): 
    if root:
        preorderTraversal(root.left)
        preorderTraversal(root.right)
        print(root.val)


def levelOrderTraversal(root): 
    h = getHeight(root)
    for x in range(1, h + 1):
        printLevel(root, x)


def printLevel(node: Node, level: int):

    if node is None:
        return None
    
    if level is 1:
        print(node.val, end=' ')
    elif level > 1:     
        printLevel(node.left, level - 1)
        printLevel(node.right, level - 1)


def getHeight(node):
    if node is None:
        return 0
    
    lHeight = getHeight(node.left)
    rHeight = getHeight(node.right)

    return max(lHeight, rHeight) + 1


root = Node(10) 
root.left = Node(11) 
root.left.left = Node(7) 
root.left.right = Node(12) 
root.right = Node(9) 
root.right.left = Node(15) 
root.right.right = Node(8) 

inorderTraversal(root)
print('\n')
preorderTraversal(root)
print('\n')
postorderTraversal(root)
print('\n')
levelOrderTraversal(root)
