def is_good(n):
    return len(set(str(n))) <= 2

t = int(input())

for _ in range(t):
    x = int(input())

    for y in range(2, 10):
        if is_good(x * y):
            print(y)
            break