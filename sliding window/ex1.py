arr = [3, 5, 2, 8, 1, 6]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum

for right in range(k, len(arr)):
    window_sum = window_sum - arr[right - k] + arr[right]

    max_sum = max(max_sum, window_sum)

print(max_sum)