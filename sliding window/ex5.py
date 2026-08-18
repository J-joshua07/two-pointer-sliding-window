#find the value 31

arr = [2, 5, 8, 12, 17, 25, 31, 40, 50]
target = 31

left = 0
right = len(arr) - 1

while left <= right:

    mid = (left + right) // 2

    if arr[mid] == target:
        print("Found at index", mid)
        break

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1