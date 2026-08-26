#two sum


arr = [2, 7, 11, 15]
target = 9

seen = {}

for i in range(len(arr)):

    needed = target - arr[i]

    if needed in seen:
        print([seen[needed], i])
        break

    seen[arr[i]] = i