#Find two numbers whose sum is 80

arr = [10, 20, 30, 40, 50]

left = 0
right = len(arr) - 1

while left < right:

    total = arr[left] + arr[right]

    if total == 80:
        print(arr[left], arr[right])
        break

    elif total < 80:
        left += 1

    else:
        right -= 1
