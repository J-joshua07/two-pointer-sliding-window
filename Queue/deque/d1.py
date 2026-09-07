from collections import deque

d = deque()

# Add from right
d.append(20)
d.append(30)

# Add from left
d.appendleft(10)

print(d)

# Remove from left
print("Removed:", d.popleft())

# Remove from right
print("Removed:", d.pop())

print(d)