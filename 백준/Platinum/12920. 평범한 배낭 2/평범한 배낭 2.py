from sys import stdin as s

m, n = map(int, s.readline().split())

goods = [ ]
dp = [0] * (n + 1)
for _ in range(m):
    v, c, k = map(int, s.readline().split())
    btmsk = 1
    while k > 0:
        a = min(btmsk, k)
        for j in range(n, a * v - 1, -1):
            dp[j] = max(dp[j], dp[j - a * v] + a * c)
        k -= btmsk
        btmsk *= 2
print(dp[-1])