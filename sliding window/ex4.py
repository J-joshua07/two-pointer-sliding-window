# Count Even Numbers in Every Window

arr = [2, 4, 1, 6, 3, 8]
k = 3

even_count = 0

for i in range(k):
    if arr[i] % 2 == 0:
        even_count += 1

print(even_count)

for right in range(k, len(arr)):

    left = right - k

    if arr[left] % 2 == 0:
        even_count -= 1

    if arr[right] % 2 == 0:
        even_count += 1

    print(even_count)