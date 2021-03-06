# Generated By lexicon-dsa CLI tool.
# Author: Saptak Sengupta(deeps.sengupta@gmail.com)
# Github: https://github.com/saptaksengupta/

# program to print the value of Lowest Common Ancestor

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    
    # Complete the demoFunction function below.
    # You should change the name accordinglly.
    def findLca(self, root: Node, n1, n2) -> Node:

        if root is None:
            return None

        if root.val == n1 or root.val == n2:
            return root

        lLca = self.findLca(root.left, n1, n2)
        rLca = self.findLca(root.right, n1, n2)


        if lLca is not None and rLca is not None:
            return root

        if lLca is not None:
            return lLca
        elif rLca is not None:
            return rLca

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    instance = Solution()
    r = instance.findLca(root, 6, 7)
    print(r.val)
