#negative number


arr = [-3, 4, 3, 90]
target = 0

seen = {}

for i in range(len(arr)):

    needed = target - arr[i]

    if needed in seen:
        print([seen[needed], i])
        break

    seen[arr[i]] = i