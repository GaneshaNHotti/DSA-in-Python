n = int(input())
sum_count = 0
for i in range(n):
    x, y, z = map(int, input().split())
    if x+y+z >= 2:
        sum_count +=1

print(sum_count)

