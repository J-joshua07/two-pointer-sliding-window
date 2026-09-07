#getting top n minimum

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        value = self.stack.pop()

        if value == self.min_stack[-1]:
            self.min_stack.pop()

        return value

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]


s = MinStack()

s.push(10)
s.push(3)
s.push(7)
s.push(1)

print("Top:", s.top())
print("Minimum:", s.get_min())