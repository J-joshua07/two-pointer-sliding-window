#eg


s = MinStack()

s.push(5)
print(s.get_min())   # 5

s.push(3)
print(s.get_min())   # 3

s.push(7)
print(s.get_min())   # 3

s.push(2)
print(s.get_min())   # 2

s.pop()
print(s.get_min())   # 3