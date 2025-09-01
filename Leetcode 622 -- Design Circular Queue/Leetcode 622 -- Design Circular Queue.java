// Leetcode 622: Design Circular Queue
// https://leetcode.com/problems/design-circular-queue/

interface CircularDataStructure {
    boolean enQueue(int value);
    boolean deQueue();
    int Front();
    int Rear();
    boolean isFull();
    boolean isEmpty();
}


class MyCircularQueue implements CircularDataStructure {
    private int[] queue;
    private int front, rear, size, capacity;

    public MyCircularQueue(int k) {
        this.capacity = k;
        this.queue = new int[k];
        this.front = 0;
        this.rear = -1;
        this.size = 0;
    }

    public boolean enQueue(int value) {
        if (isFull()) return false; // Cannot insert if queue is full
        rear = (rear + 1) % capacity; // Circular increment
        queue[rear] = value;
        size++;
        return true;
    }

    public boolean deQueue() {
        if (isEmpty()) return false; // Cannot delete if queue is empty
        front = (front + 1) % capacity; // Circular increment
        size--;
        return true;
    }

    public int Front() {
        return isEmpty() ? -1 : queue[front]; // Return front value or -1 if empty
    }

    public int Rear() {
        return isEmpty() ? -1 : queue[rear]; // Return rear value or -1 if empty
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == capacity;
    }
}


/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
