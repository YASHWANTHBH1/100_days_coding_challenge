# LeetCode Problem Number: 232
# Problem Link: https://leetcode.com/problems/implement-queue-using-stacks/
#
# Time Complexity:
# - push: O(1)
# - pop: Amortized O(1), Worst Case O(n)
# - peek: Amortized O(1), Worst Case O(n)
# - empty: O(1)
#
# Space Complexity: O(n)

class MyQueue(object):

    def __init__(self):
        """Initialize two stacks: s1 (main stack), s2 (for reversing order)."""
        self.s1 = []  # Stack 1 for push operations
        self.s2 = []  # Stack 2 for pop/peek operations

    def push(self, x):
        """Push an element to the back of the queue (O(1))."""
        self.s1.append(x)

    def pop(self):
        """Removes and returns the front element of the queue."""
        if not self.s2:  # If s2 is empty, transfer all elements from s1
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()  # Pop from s2 (front of the queue)

    def peek(self):
        """Returns the front element of the queue without removing it."""
        if not self.s2:  # If s2 is empty, transfer all elements from s1
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]  # Peek the top element of s2 (front of the queue)

    def empty(self):
        """Returns True if the queue is empty, False otherwise."""
        return not self.s1 and not self.s2  # Check if both stacks are empty

# Test Cases
queue = MyQueue()
queue.push(1)
queue.push(2)
print("Peek:", queue.peek())  # Expected: 1
print("Pop:", queue.pop())    # Expected: 1
print("Empty:", queue.empty())  # Expected: False
print("Pop:", queue.pop())    # Expected: 2
print("Empty:", queue.empty())  # Expected: True
