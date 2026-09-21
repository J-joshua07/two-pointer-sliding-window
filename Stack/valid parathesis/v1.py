# # valid parathesis


# def is_valid(s):

#     stack = []

#     pairs = {
#         ')': '(',
#         ']': '[',
#         '}': '{'
#     }

#     for char in s:

#         if char in '([{':
#             print(char)
#             stack.append(char)
#             print(stack)

#         else:
#             print(char)
#             if not stack:
#                 return False
#             print(stack[-1])
#             print(pairs[char])
#             if stack[-1] != pairs[char]:
#                 return False

#             stack.pop()

#     return len(stack) == 0


# #print(is_valid("()"))

# print(is_valid("if stack[-1]"))

s = "if stack[-1][[[[]]]{]"

c1 = s.count("[")
c2 = s.count("]")
print(c1)
print(c2)