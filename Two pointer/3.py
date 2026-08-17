#palindrome

text = "madam"

left = 0
right = len(text)-1

is_palindrome = True

while left < right:
    if text[left] != text[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

print(is_palindrome)