
class LinkedListNode:
    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode
    
    def getNextNode(self):
        return self.nextNode

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.size = 0
    
    def addNode(self, data):
        newNode = LinkedListNode(data, self.head)
        self.head = newNode
        self.size += 1

    def printNodes(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()
    
    def middleNode(self):
        normal = self.head
        fast = self.head
        
        while fast != None:
            if fast.nextNode != None:
                fast = fast.nextNode.nextNode
            else:
                break
            normal = normal.nextNode
        return normal.nextNode
    
    def removeNthFromEnd(self, n):
        length = 0
        counter = 0
        tempHead = self.head
        while tempHead.nextNode != None:
            length += 1
            tempHead = tempHead.nextNode
        
        # desired node is now (length - n)
        newTempHead = self.head
        while newTempHead.nextNode != None:
            if counter == length - n:
                newTempHead.data = newTempHead.nextNode.data
                newTempHead.nextNode = newTempHead.nextNode.nextNode
                self.size -= 1
                break
            else:
                counter += 1
                newTempHead = newTempHead.nextNode

ll = LinkedList()
ll.addNode("test")
ll.addNode("test2")
ll.addNode("test3")
ll.addNode("test4")
ll.addNode("test5")
#ll.removeNthFromEnd(2)
ll.middleNode()
ll.printNodes()