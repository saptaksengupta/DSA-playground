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
        inorderTraversal(root.left)
        inorderTraversal(root.right)

## Util function to Print all the nodes By Postorder Traversal.
def postorderTraversal(root): 
    if root:
        inorderTraversal(root.left)
        inorderTraversal(root.right)
        print(root.val)



r = Node(50)

insertNode(r, Node(40) )
insertNode(r, Node(60) )
insertNode(r, Node(45) )
insertNode(r, Node(55) )

inorderTraversal(r)
print('\n')
preorderTraversal(r)
print('\n')
postorderTraversal(r)

