"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
NOTE:

All the operations have to be constant time operations.
getMin() should return -1 if the stack is empty.
pop() should return nothing if the stack is empty.
top() should return -1 if the stack is empty.
"""


class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.st.append(x)
        if len(self.min_st) == 0 or x <= self.min_st[-1]:
            self.min_st.append(x)

    # @return nothing
    def pop(self):
        el = None
        if len(self.st) > 0:
            el = self.st.pop()
            min_val = self.min_st[-1]
            if min_val == el:
                self.min_st.pop()
        return el

    # @return an integer
    def top(self):
        return self.st[-1] if len(self.st) > 0 else -1

    # @return an integer
    def getMin(self):
        return self.min_st[-1] if len(self.st) > 0 else -1
