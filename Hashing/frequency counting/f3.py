#anagrams


s1 = "listen"
s2 = "silent"

freq1 = {}
freq2 = {}

for char in s1:
    freq1[char] = freq1.get(char, 0) + 1

for char in s2:
    freq2[char] = freq2.get(char, 0) + 1

if freq1 == freq2:
    print("Anagram")
else:
    print("Not anagram")