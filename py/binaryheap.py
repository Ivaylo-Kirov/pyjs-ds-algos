
import math

class BinaryHeap:
    def __init__(self):
        self.items = []

    def top(self):
        return self.items[0]
    
    def swim(self, startIndex):
        if startIndex == 0:
            return
        parentIndex = self.getParentIndex(startIndex)
        if self.items[startIndex] > self.items[parentIndex]:
            self.items[parentIndex], self.items[startIndex] = self.items[startIndex], self.items[parentIndex]
            self.swim(parentIndex)
        
    def sink(self, startIndex):
        if len(self.items) < 2:
            return
        leftIndex = self.leftChildIndex(startIndex)
        rightIndex = self.rightChildIndex(startIndex)
        if leftIndex >= len(self.items) and rightIndex >= len(self.items):
            return
        if leftIndex >= len(self.items):
            swapIndex = rightIndex
        if rightIndex >= len(self.items):
            swapIndex = leftIndex
        else:
            swapIndex = self.items[leftIndex] > self.items[rightIndex] if leftIndex else rightIndex
        if self.items[startIndex] < self.items[swapIndex]:
            self.items[startIndex], self.items[swapIndex] = self.items[swapIndex], self.items[startIndex]
            self.sink(swapIndex)

    def leftChildIndex(self, index):
        return math.floor((index + 1 * 2) - 1)

    def rightChildIndex(self, index):
        return math.floor((index + 1) * 2)

    def getParentIndex(self, index):
        return math.floor((index - 1) / 2)

    def pop(self):
        self.items[0], self.items[-1] = self.items[-1], self.items[0]
        del self.items[-1]
        self.sink(0)

    def add(self, data):
        self.items.append(data)
        self.swim(len(self.items)-1)


bh = BinaryHeap()

bh.add(3)
bh.add(5)
print(bh.top())
bh.add(10)
bh.pop()
print(bh.top())