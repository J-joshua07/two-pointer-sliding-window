#have common elements


arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 3, 8]

seen = set(arr1)

for num in arr2:

    if num in seen:
        print("Common:", num)