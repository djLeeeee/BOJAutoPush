from sys import stdin as s
N, M = map(int, s.readline().split())
dp = [0] * (M + 1)
for _ in range(N):
	m, v = map(int, s.readline().split())
	new_dp = [0] * (M + 1)
	new_dp[:m] = dp[:m]
	for j in range(m, M + 1):
		new_dp[j] = max(dp[j], dp[j - m] + v)
	dp = new_dp
print(dp[-1])