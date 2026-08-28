#Count Subarrays With Target Sum


arr = [1, 1, 1]
target = 2

freq = {0: 1}
prefix = 0
count = 0

for num in arr:

    prefix += num

    needed = prefix - target

    if needed in freq:
        count += freq[needed]

    freq[prefix] = freq.get(prefix, 0) + 1

print(count)

