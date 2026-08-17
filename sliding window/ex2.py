#the maximum sum of 3 consecutive numbers

arr = [2, 4, 1, 7, 5, 3]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum

for right in range(k, len(arr)):

    window_sum = window_sum - arr[right - k] + arr[right]

    max_sum = max(max_sum, window_sum)

print(max_sum)