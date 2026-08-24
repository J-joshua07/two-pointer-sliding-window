#Find how many times each number appears.

arr = [2, 1, 2, 3, 1, 2]

freq = {}

for num in arr:

    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)