class MinStack(object):

    def __init__(self):
        self.regular_stack = []
        self.min_stack = []

    def push(self, val):
        self.regular_stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self):
        val = self.regular_stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.regular_stack[-1]

    def getMin(self):
        return self.min_stack[-1]
