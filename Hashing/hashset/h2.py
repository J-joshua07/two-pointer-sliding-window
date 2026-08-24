#find duplicates


arr = [4, 2, 7, 2, 9, 5]

seen = set()

for num in arr:

    if num in seen:
        print("Duplicate:", num)
        break

    seen.add(num)