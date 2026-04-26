t = int(input())

def answer(x, y):
    n = max(x, y)
    if n % 2 == 0:
        if x == n:
            return n*n - (y - 1)
        else:
            return (n-1)*(n-1) + x
    else:
        if y == n:
            return n*n - (x - 1)
        else:
            return (n-1)*(n-1) + y

def solve(num):
    for _ in range(num):
        x, y = map(int, input().split())
        print(answer(x, y))

solve(t)
