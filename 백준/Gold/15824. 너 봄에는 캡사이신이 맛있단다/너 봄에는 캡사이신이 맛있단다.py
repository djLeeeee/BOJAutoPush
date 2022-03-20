from sys import stdin

input = stdin.readline


def pow2(b):
    if dp[b]:
        return dp[b]
    c = pow2(b // 2)
    if b % 2:
        dp[b] = c * c * 2 % div
        return dp[b]
    dp[b] = c * c % div
    return dp[b]


div = 10 ** 9 + 7
n = int(input())
if n == 1:
    print(0)
    exit()
ingredient = sorted(list(map(int, input().split())))
ans = 0
dp = [0] * n
dp[0] = 1
dp[1] = 2
for i in range(n):
    ans += ingredient[i] * (pow2(i) - pow2(n - 1 - i))
print(ans % div)
