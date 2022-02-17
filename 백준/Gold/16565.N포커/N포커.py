dp = [[1] * 53 for _ in range(53)]
for i in range(1, 53):
    for j in range(1, i + 1):
        dp[j][i - j + 1] = (dp[j - 1][i - j + 1] + dp[j][i - j]) % 10007
n = int(input())
ans = 0
for k in range(1, n // 4 + 1):
    if k % 2:
        ans += dp[13 - k][k] * dp[52 - n][n - 4 * k]
    else:
        ans -= dp[13 - k][k] * dp[52 - n][n - 4 * k]
    ans %= 10007
print(ans)