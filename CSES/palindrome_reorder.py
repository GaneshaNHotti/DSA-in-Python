s = input()

from collections import Counter
freq = Counter(s)

odd_count = 0
middle = ""

for char in freq:
    if freq[char] % 2 != 0:
        odd_count += 1
        middle = char

if odd_count > 1:
    print("NO SOLUTION")
else:
    left = []

    for char in freq:
        left.append(char * (freq[char] // 2))

    left_part = "".join(left)
    right_part = left_part[::-1]

    print(left_part + middle + right_part)