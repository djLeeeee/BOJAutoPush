n = int(input())
array = list(map(int, input().split()))
dp = [0] * 1001
for i in range(n):
    dp[array[i]] = max(dp[:array[i]]) + array[i]
print(max(dp))