
class BinaryHeap {
    constructor() {
        this.items = [];
        this.size = 0;
    }

    add(data) {
        this.items.push(data);
        this.swim(this.size);
        this.size++;
    }

    swim(index) {
        // parent and swap and recurse
        const parentIndex = this.getParentIndex(index);
        if (this.items[index] > this.items[this.getParentIndex(index)]) {
            [this.items[index], this.items[this.getParentIndex(index)]] = [this.items[this.getParentIndex(index)], this.items[index]];
            this.swim(parentIndex);
        }
    }

    getParentIndex(index) {
        return Math.floor((index - 1) / 2);
    }

    getLeftChildIndex(index) {
        return Math.floor((index + 1 * 2) - 1);
    }

    getRightChildIndex(index) {
        return Math.floor((index + 1) * 2);
    }

    pop() {
        [this.items[0], this.items[this.size-1]] = [this.items[this.size-1], this.items[0]];
        this.items.pop();
        this.size--;
        this.sink(0);
    }

    sink(index) {
        // compare left and right to get swapIndex, then check for swap and recurse
        let biggerChildIndex;
        let left = this.items[this.getLeftChildIndex(index)];
        let right = this.items[this.getRightChildIndex(index)];
        if (left == undefined && right == undefined) {
            return;
        }
        if (right == undefined) {
            biggerChildIndex = this.getLeftChildIndex(index);
        } 
        else {
            biggerChildIndex = this.items[this.getLeftChildIndex(index)] > this.items[this.getRightChildIndex(index)] ? this.getLeftChildIndex(index) : this.getRightChildIndex(index);
        }    
        if (this.items[index] < this.items[biggerChildIndex]) {
            [this.items[index], this.items[biggerChildIndex]] = [this.items[biggerChildIndex], this.items[index]];
            this.sink(biggerChildIndex);
        }
    }

    top() {
        return this.items[0];
    }

}

bh = new BinaryHeap();
bh.add(3);
bh.add(5);
bh.add(2);
bh.add(7);
bh.pop();
bh.top();
bh.pop();
bh.add(1);
