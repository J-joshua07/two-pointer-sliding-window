#Remove a Specific Number

arr = [3, 2, 3, 4, 3, 5]

slow = 0

for fast in range(len(arr)):

    if arr[fast] != 3:
        arr[slow] = arr[fast]
        slow += 1

print(arr[:slow])