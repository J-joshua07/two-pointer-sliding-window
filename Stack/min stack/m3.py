#pop the minimum


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