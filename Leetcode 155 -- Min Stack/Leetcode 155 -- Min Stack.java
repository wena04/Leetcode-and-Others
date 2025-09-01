// Leetcode 155: Min Stack
// https://leetcode.com/problems/min-stack/

// OOD or OOP right here. everything is O(1)

import java.util.Stack;

// Define the interface for a stack
interface StackInterface {
    void push(int x);
    void pop();
    int top();
    int getMin();
}

// MinStack implementing the StackInterface
public class MinStack implements StackInterface {
    private Stack<Integer> stack;      // Main stack for storing elements
    private Stack<Integer> minStack;   // Auxiliary stack for tracking minimum values

    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }

    @Override
    public void push(int x) {
        stack.push(x);
        // Push onto minStack if it's the smallest seen so far
        if (minStack.isEmpty() || x <= minStack.peek()) {
            minStack.push(x);
        }
    }

    @Override
    public void pop() {
        if (stack.isEmpty()) return;

        int popped = stack.pop();
        // If the popped value is the current minimum, pop from minStack as well
        if (popped == minStack.peek()) {
            minStack.pop();
        }
    }

    @Override
    public int top() {
        return stack.isEmpty() ? -1 : stack.peek();
    }

    @Override
    public int getMin() {
        return minStack.isEmpty() ? Integer.MAX_VALUE : minStack.peek();
    }
}
