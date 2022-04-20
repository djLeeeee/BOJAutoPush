from sys import stdin as s
N, M = map(int, s.readline().split())
dp = [0] * (M + 1)
for _ in range(N):
	m, v = map(int, s.readline().split())
	for j in range(M, m - 1, -1):
		dp[j] = max(dp[j], dp[j - m] + v)
print(dp[-1])