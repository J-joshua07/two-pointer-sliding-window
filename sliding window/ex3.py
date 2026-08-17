# the minimum sum of 3 consecutive numbers

arr = [5, 2, 8, 1, 3, 4]
k = 3

window_sum = sum(arr[:k])
min_sum = window_sum

for right in range(k, len(arr)):

    window_sum = window_sum - arr[right - k] + arr[right]

    min_sum = min(min_sum, window_sum)

print(min_sum)