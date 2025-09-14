n, k = input().split()
n, k = int(n), int(k)

count = 0

arr = [int(x) for x in input().split()]

for i in range(n):
    if arr[i] >= arr[k-1] and arr[i] > 0:
        count +=1

print(count)