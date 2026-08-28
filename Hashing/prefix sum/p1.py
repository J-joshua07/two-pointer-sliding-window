#subarray sum


arr = [1, 2, 3, 4, 5]
target = 9

seen = {0: -1}
prefix = 0

for i in range(len(arr)):

    prefix += arr[i]

    needed = prefix - target

    if needed in seen:
        print(seen[needed] + 1, i)
        break

    seen[prefix] = i