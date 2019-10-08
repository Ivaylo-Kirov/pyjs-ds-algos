# next time don't use list for a queue
# has BFS and DFS
class Vertex:
    def __init__(self, data):
        self.data = data
        self.conns = []
    
class Graph:
    def __init__(self):
        self.vertices = []
        self.DFSvisited = []
    
    def addVertex(self, data):
        self.vertices.append(Vertex(data))
    
    def printVertices(self):
        for vertex in self.vertices:
            print(vertex.data)
    
    def addEdge(self, src, dest):
        srcV = [v for v in self.vertices if v.data == src]
        destV = [v for v in self.vertices if v.data == dest]
        srcV[0].conns.append(destV)

    def BFS(self):
        # list for now
        visited = []
        q = []
        q.append(self.vertices[0])
        visited.append(self.vertices[0].data)

        while len(q) > 0:
            current = q.pop(0)
            for child in current.conns:
                if child[0].data not in visited:
                    print(child[0].data)
                    visited.append(child[0].data)
                    q.append(child[0])
    
    def DFS(self):
        self.DFSvisited.append(self.vertices[0].data)
        for conn in self.vertices[0].conns:
            if conn[0].data not in self.DFSvisited:
                self.DFSvisited.append(conn[0].data)
                self._DFS(conn[0])
        self.DFSvisited.clear()

    def _DFS(self, curr):
        print(curr.data)
        for conn in curr.conns:
            self._DFS(conn[0])

g = Graph()

g.addVertex("Toronto")
g.addVertex("Markham")
g.addVertex("Niagara")
g.addVertex("Costa Rica")
g.addVertex("North Bay")
g.addVertex("Montreal")
g.addVertex("PEI")

g.addEdge("Toronto", "Markham")
g.addEdge("Toronto", "Niagara")
g.addEdge("Markham", "North Bay")
g.addEdge("Niagara", "Costa Rica")
g.addEdge("Toronto", "Montreal")
g.addEdge("Montreal", "PEI")

print('==BFS==')
g.BFS()

print('==DFS==')
g.DFS()