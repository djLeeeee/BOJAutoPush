from sys import stdin

input = stdin.readline

n = int(input())
INF = float('inf')
umm = [0] + list(map(int, input().split()))
dp = [[INF] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 0
dp[1][0] = 0
dp[0][1] = 0
for j in range(n):
    if j:
        dp[j][j + 1] = dp[j][0]
        dp[j + 1][j] = dp[0][j]
        for k in range(1, j):
            dp[j][j + 1] = min(dp[j][j + 1], dp[j][k] + abs(umm[j + 1] - umm[k]))
            dp[j + 1][j] = min(dp[j + 1][j], dp[k][j] + abs(umm[j + 1] - umm[k]))
    for i in range(j + 2, n + 1):
        dp[i][j] = dp[i - 1][j] + abs(umm[i] - umm[i - 1])
        dp[j][i] = dp[j][i - 1] + abs(umm[i] - umm[i - 1])
ans = min(dp[-1])
for idx in range(n):
    ans = min(ans, dp[idx][-1])
print(ans)
