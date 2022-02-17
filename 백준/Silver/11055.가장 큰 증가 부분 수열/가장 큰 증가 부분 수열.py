n = int(input())
array = list(map(int, input().split()))
dp = [0] * n
M = 0
for i in range(n):
    dp[i] = array[i]
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + array[i])
    M = max(M, dp[i])
print(M)
