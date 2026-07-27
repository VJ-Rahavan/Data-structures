class Queue {
  constructor() {
    this.items = {};
    this.front = 0;
    this.rear = 0;
  }

  enqueue(item) {
    this.items[this.rear] = item;
    this.rear++;
  }

  dequeue() {
    if (this.isEmpty()) return null;

    const item = this.items[this.front];
    delete this.items[this.front];
    this.front++;
    return item;
  }

  peek() {
    return this.isEmpty() ? null : this.items[this.front];
  }

  isEmpty() {
    return this.front === this.rear;
  }

  size() {
    return this.rear - this.front;
  }
}

// Example
const q = new Queue();

q.enqueue(1);
q.enqueue(2);
q.enqueue(3);

console.log(q.dequeue()); // 1
console.log(q.peek());    // 2
console.log(q.size());    // 2
console.log(q.isEmpty()); // false