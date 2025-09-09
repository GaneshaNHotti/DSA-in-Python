n = int(input())
store_value = []

def weird_algorithm(x):
    if x % 2 == 0:
        store_value.append(x)
        return x // 2
    else:
        store_value.append(x)
        return 3 * x + 1

while n != 1:
    n = weird_algorithm(n)
store_value.append(n)
print(*store_value)
