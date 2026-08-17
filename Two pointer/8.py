#alt how many times each number appears

arr = [1, 2, 2, 3, 3, 3]

frequency = {}

for num in arr:
    frequency[num] = frequency.get(num, 0) + 1

print(frequency)