
class LinkedListNode {
    constructor(data, nextNode = null) {
        this.data = data;
        this.nextNode = nextNode;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
    }

    addNode(data) {
        let newNode = new LinkedListNode(data);
        if (this.head == null) {
            this.head = newNode;
        } else {
            newNode.nextNode = this.head;
            this.head = newNode;
        }
    }

    addNodeToEnd(data) {
        let current = this.head;
        if (current == null) {
            this.head = new LinkedListNode(data);
        } else {
            while (current.nextNode) {
                current = current.nextNode;
            }
            current.nextNode = new LinkedListNode(data);
        }
    }

}

ll = new LinkedList();
ll.addNode(3);
ll.addNode(15);
ll.addNodeToEnd(23);