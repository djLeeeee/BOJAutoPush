n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * (1 << n)
dp[0] = 1
check = [(0, 0)]
for _ in range(n):
    new = set()
    for t, c in check:
        for bit in range(n):
            if not (1 << bit) & c and t + arr[bit] >= m:
                now = c + (1 << bit)
                new.add((t + arr[bit] - m, now))
                dp[now] += dp[c]
    check = new
print(dp[-1])