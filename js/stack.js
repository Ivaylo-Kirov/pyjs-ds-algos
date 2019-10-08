class Stack {
    constructor() {
        this.items = [];
    }
    add(data) {
        this.items.push(data);
    }
    pop() {
        this.items.pop();
    }
    top() {
        return this.items[this.items.length-1];
    }
}

s = new Stack();
s.add(3);
s.add(5);
s.pop();
s.add(7);
console.log(s.top());
s.add(12);