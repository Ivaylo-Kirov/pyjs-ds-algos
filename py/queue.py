from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def add(self, data):
        self.items.appendleft(data)

    def pop(self):
        self.items.pop()

q = Queue()

q.add(3)
q.add(2)

q.pop()
q.pop()

