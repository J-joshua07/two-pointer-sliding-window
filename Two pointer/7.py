#alt hash set

arr = [8, 1, 6, 3, 5, 2]
target = 9

seen = set()

for num in arr:

    needed = target - num

    if needed in seen:
        print(needed, num)
        break

    seen.add(num)