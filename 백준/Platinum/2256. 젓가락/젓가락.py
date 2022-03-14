from sys import stdin

input = stdin.readline

k, n = map(int, input().split())
stick = [int(input()) for _ in range(n)] + [0]
stick.sort()
INF = float('inf')
dp = [[INF] * (n + 1) for _ in range(k + 1)]
dp[0] = [0] * (n + 1)
for i in range(1, k + 1):
    for j in range(n - 3 * i + 1, 0, -1):
        dp[i][j] = min(
            dp[i][j + 1],
            dp[i - 1][j + 2] + (stick[j] - stick[j + 1]) ** 2
        )
print(dp[-1][1])
