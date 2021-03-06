from sys import stdin

input = stdin.readline

n = int(input())
rate = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (1 << n)
update = {i: set() for i in range(1, n + 1)}


def order(num):
    ans = 0
    while num > 0:
        if num & 1:
            ans += 1
        num >>= 1
    return ans


for j in range(1, 1 << n):
    update[order(j)].add(j)
for k in range(n):
    dp[1 << k] = rate[0][k]
for p in range(1, n):
    for now in update[p]:
        for bit in range(n):
            if (1 << bit) & now == 0:
                dp[now + (1 << bit)] = max(dp[now + (1 << bit)], dp[now] * rate[p][bit] / 100)
print(dp[-1])
