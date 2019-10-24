from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def add(self, data):
        self.items.appendleft(data)

    def pop(self):
        try:
            self.items.pop()
        except IndexError:
            raise RuntimeError('pop from empty Queue')

    def __len__(self):
        return len(self.items)




q = Queue()
q.add(3)
assert(len(q) == 1)
q.add(2)
q.pop()
q.pop()

