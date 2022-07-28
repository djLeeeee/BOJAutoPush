from sys import stdin

input = stdin.readline

dp = [1] * 2003
for i in range(2, 2003):
    dp[i] = dp[i - 1] * i
memo = [[0] * 2003 for _ in range(2003)]
t = int(input())
query = [tuple(map(int, input().split())) for _ in range(t)]
ans = [0] * t
for tc in range(t):
    n1, m1, n2, m2 = query[tc]
    now = dp[m1] * dp[n1 + n2 - m1 + 1] * dp[n1 + 1] * dp[n2 + 1]
    now /= dp[m1] * dp[n1 - m1] * dp[n2 + 1] * dp[n1 + n2 + 2]
    ans[tc] += now
    for k in range(1, m2 + 1):
        now *= ((m1 + k) * (n2 - k + 2)) / (k * (n1 + n2 - m1 - k + 2))
        ans[tc] += now
print(*ans, sep='\n')
