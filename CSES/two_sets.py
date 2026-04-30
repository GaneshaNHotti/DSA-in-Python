n = int(input())
total = n * (n + 1) // 2

# Check feasibility
if total % 2 != 0:
    print("NO")
    exit()

print("YES")

set1 = []
set2 = []

# Case 1: n % 4 == 0
if n % 4 == 0:
    i = 1
    while i <= n:
        # block: (i, i+1, i+2, i+3)
        set1.extend([i, i + 3])
        set2.extend([i + 1, i + 2])
        i += 4

# Case 2: n % 4 == 3
else:
    # handle first 3
    set1.extend([1, 2])
    set2.append(3)

    i = 4
    while i <= n:
        set1.extend([i, i + 3])
        set2.extend([i + 1, i + 2])
        i += 4

# Output
print(len(set1))
print(*set1)
print(len(set2))
print(*set2)