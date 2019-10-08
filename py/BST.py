
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def addNode(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._addNode(self.root, data)
        
    def _addNode(self, startNode, data):
        if data < startNode.data:
            if startNode.left is None:
                startNode.left = Node(data)
            else:
                self._addNode(startNode.left, data)
        else:
            if startNode.right is None:
                startNode.right = Node(data)
            else:
                self._addNode(startNode.right, data)
    
    def findMin(self):
        startNode = self.root
        while startNode.left is not None:
            startNode = startNode.left
        return startNode.data

bst = BST()
bst.addNode(5)
bst.addNode(2)
bst.addNode(8)
bst.addNode(4)
bst.addNode(3)

print(bst.findMin())

bst.addNode(1)

print(bst.findMin())


