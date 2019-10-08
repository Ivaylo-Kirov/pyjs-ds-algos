class Stack:
    def __init__(self):
        self.items = []
        self.size = 0
    
    def add(self, data):
        self.items.append(data)
        self.size += 1

    def pop(self):
        self.items.pop()
        self.size -= 1
    
    def getSize(self):
        return self.size

s = Stack()

s.add(3)
s.add(2)

s.pop()
s.pop()