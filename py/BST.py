
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
    
    def _countNodes(self, node):
        if node is None:
            return 0
        return (1 + self._countNodes(node.left) + self._countNodes(node.right))
    
    def countNodes(self):
        return self._countNodes(self.root)

    def findMin(self):
        startNode = self.root
        while startNode.left is not None:
            startNode = startNode.left
        return startNode.data
    
    def checkValid(self):
        minV = -200000
        maxV = 200000
        return self._checkValid(self.root, minV, maxV)

    def _checkValid(self, currentNode, minV, maxV):
        if currentNode == None:
            return True
        return currentNode.data >= minV and currentNode.data <= maxV and self._checkValid(currentNode.left, minV, currentNode.data) and self._checkValid(currentNode.right, currentNode.data, maxV)



bst = BST()
bst.addNode(5)
bst.addNode(2)
bst.addNode(8)
bst.addNode(4)
bst.addNode(3)

result = bst.countNodes()

print(bst.findMin())

bst.addNode(1)

print(bst.findMin())

result = bst.checkValid()
print('hi')


