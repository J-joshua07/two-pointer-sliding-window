stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# Peek
print("Top:", stack[-1])

# Pop
removed = stack.pop()

print("Removed:", removed)
print("Stack:", stack)