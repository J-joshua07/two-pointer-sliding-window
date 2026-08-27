#Duplicate Characters


text = "programming"

seen = set()

for char in text:

    if char in seen:
        print("Duplicate:", char)
        break

    seen.add(char)