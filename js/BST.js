
class BSTNode {
    constructor(data, left=null, right=null) {
        this.data = data;
        this.left = left;
        this.right = right;
    }
}

class BST {
    constructor() {
        this.head = null;
    }
    insert(data) {
        this.head = this.insertUtil(this.head, data);
        
    }
    insertUtil(curr, data) {
        if (curr == null) {
            curr = new BSTNode(data);
            return curr;
        }
        if (data < curr.data) {
            curr.left = this.insertUtil(curr.left, data);
        } else {
            curr.right = this.insertUtil(curr.right, data);
        }
        return curr;
    }
    search(data) {
        // recurse or loop
    }

}

bst = new BST();

bst.insert(4);
bst.insert(2);
bst.insert(6);
bst.insert(5);
bst.insert(3);