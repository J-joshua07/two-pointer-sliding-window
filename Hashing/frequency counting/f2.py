#most frequent number


arr = [1, 3, 2, 3, 4, 3, 2]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

most_frequent = None
max_count = 0

for num in freq:
    if freq[num] > max_count:
        max_count = freq[num]
        most_frequent = num

print(most_frequent)