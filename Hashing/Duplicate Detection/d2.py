#Find ALL Duplicates

arr = [1, 2, 3, 2, 4, 1, 5, 3]

seen = set()
duplicates = set()

for num in arr:

    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(duplicates)
