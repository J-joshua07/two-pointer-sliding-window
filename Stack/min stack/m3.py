#pop the minimum


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

    def get_min(self):
        return self.min_stack[-1]


s = MinStack()

s.push(10)
s.push(5)
s.push(8)
s.push(2)

print("Minimum:", s.get_min())

s.pop()

print("Minimum:", s.get_min())

s.pop()

print("Minimum:", s.get_min())