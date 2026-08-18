#not exist

arr = [2, 5, 8, 12, 17, 25, 31, 40]
target = 20

left = 0
right = len(arr) - 1

found = False

while left <= right:

    mid = (left + right) // 2

    if arr[mid] == target:
        found = True
        break

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

if found:
    print("Found")
else:
    print("Not found")