#Return the Actual Numbers


arr = [2, 7, 11, 15]
target = 9

seen = set()

for num in arr:

    needed = target - num

    if needed in seen:
        print(needed, num)
        break

    seen.add(num)