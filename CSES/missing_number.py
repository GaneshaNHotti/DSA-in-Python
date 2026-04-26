n = int(input())
nums = list(map(int, input().split()))
expected_sum = n * (n + 1) // 2
missing = expected_sum - sum(nums)

print(missing)
