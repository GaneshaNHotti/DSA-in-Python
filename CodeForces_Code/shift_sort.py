def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        if "".join(sorted(s)) == s:
            print(0)
            continue
        if "01" in s and "10" in s:
            print(2)
        else:
            print(1)

solve()
# NEED TO REVISIT THE CODE