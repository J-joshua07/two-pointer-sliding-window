#find duplicate

arr = [4, 2, 7, 2, 9, 4]

seen = set()

for num in arr:

    if num in seen:
        print("Duplicate:", num)
        break

    seen.add(num)