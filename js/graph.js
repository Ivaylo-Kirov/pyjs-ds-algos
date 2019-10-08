
class Vertex {
    constructor(name) {
        this.name = name;
        this.conns = [];
    }
}

class Graph {
    constructor() {
        this.vertices = [];
        this.dfsVisited = new Set();
        this.topoSort = new Array();
    }

    addVertex(data) {
        this.vertices.push(new Vertex(data));
    }

    addEdge(src, dest) {
        let srcMatch = this.vertices.filter((vertex) => {
            return vertex.name === src 
         });
         let destMatch = this.vertices.filter((vertex) => {
            return vertex.name === dest 
         });
         srcMatch[0].conns.push(destMatch);
    }
    BFS() {
        const q = [];
        q.push(this.vertices[0]);
        while (q.length > 0) {
            console.log(q[q.length-1]);
            q[q.length-1].conns.forEach((conn) => {
                q.unshift(conn[0]);
            });
            q.pop();
        }
    }
    DFS() {
        this.dfsVisited.add(this.vertices[0].name);
        console.log(this.vertices[0].name);
        this.DFSUtil(this.vertices[0]);
    }
    DFSUtil(curr) {
        if (curr == null) {
            return;
        } else {
            curr.conns.forEach((conn) => {
                if (!this.dfsVisited.has(conn[0].name)) {
                    console.log(conn[0].name);
                    this.dfsVisited.add(conn[0].name);
                    this.DFSUtil(conn[0]);
                }
            });
        }
    }

    CheckCycle() {
        this.dfsVisited.add(this.vertices[0].name);
        console.log(this.vertices[0].name);
        this.CheckCycleUtil(this.vertices[0]);
    }
    CheckCycleUtil(curr) {
        if (curr == null) {
            return;
        } else {
            curr.color = "white";
            curr.conns.forEach((conn) => {
                curr.color = "gray";
                if (conn[0].color == "gray") {
                    console.log(`found a cycle when connecting ${curr.name} and ${conn[0].name}`);
                }
                if (!this.dfsVisited.has(conn[0].name)) {
                    console.log(conn[0].name);
                    this.dfsVisited.add(conn[0].name);
                    this.CheckCycleUtil(conn[0]);
                }
            });
            curr.color = "black";
        }
    }

    TopoSort() {
        this.dfsVisited.add(this.vertices[0].name);
        console.log(this.vertices[0].name);
        this.TopoSortUtil(this.vertices[0]);
        return this.topoSort;
    }
    TopoSortUtil(curr) {
        if (curr == null) {
            return;
        } else {
            curr.color = "white";
            curr.conns.forEach((conn) => {
                curr.color = "gray";
                if (!this.dfsVisited.has(conn[0].name)) {
                    //console.log(conn[0].name);
                    this.dfsVisited.add(conn[0].name);
                    this.TopoSortUtil(conn[0]);
                }
            });
            this.topoSort.push(curr);
            curr.color = "black";
        }
    }
}

let g = new Graph();
g.addVertex("Toronto");
g.addVertex("Markham");
g.addVertex("North Bay");
g.addVertex("Montreal");
g.addVertex("PEI");
g.addVertex("Niagara");
// g.addVertex("Lake"); // Used for cycle
g.addVertex("Costa Rica");

g.addEdge("Toronto", "Markham");
g.addEdge("Toronto", "Montreal");
g.addEdge("Toronto", "Niagara");
g.addEdge("Markham", "North Bay");
// g.addEdge("Montreal", "Lake"); // Used for cycle
g.addEdge("Montreal", "PEI");
// g.addEdge("Lake", "Toronto"); // Used for cycle
g.addEdge("Niagara", "Costa Rica");


// g.DFS();
// g.BFS(); // super basic right now and doesn't include hash of visited

// g.CheckCycle();
const result = g.TopoSort();
console.log('hi');
