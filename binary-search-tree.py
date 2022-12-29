# Binary search tree
# O(log(n)) for average case
# O(n) for worst case

class Node():
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None


def insert(toBeInsertedNode,currentNode):
    if(toBeInsertedNode.data>currentNode.data):
        if(currentNode.right is None):
            currentNode.right = toBeInsertedNode
            return
        else:
            insert(toBeInsertedNode,currentNode.right)

    if(toBeInsertedNode.data<currentNode.data):
        if(currentNode.left is None):
            currentNode.left = toBeInsertedNode
            return
        else:
            insert(toBeInsertedNode,currentNode.left)


def bst(array):
    root = Node(array[0])
    for i in range(1,len(array)):
        toBeInsertedNode = Node(array[i])
        insert(toBeInsertedNode,root)
    
    return root

def printTreeSorted(node):
    if node is None:
        return
    printTreeSorted(node.left)
    print(node.data, end = " ")
    printTreeSorted(node.right)

pre = [10, 5, 1, 7, 40, 50]
ss = bst(pre)

printTreeSorted(ss)
