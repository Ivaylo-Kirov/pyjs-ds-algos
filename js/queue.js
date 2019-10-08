// inefficient, but quick and dirty
// unshift is an O(n) operation

class Queue {
    constructor() {
        this.items = [];
    }
    add(data) {
        this.items.unshift(data);
    }
    pop() {
        this.items.pop();
    }
    top() {
        return this.items[this.items.length-1];
    }
}

s = new Queue();
s.add(3);
s.add(5);
s.pop();
s.add(7);
console.log(s.top());
s.add(12);