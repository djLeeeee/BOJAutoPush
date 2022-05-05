from sys import stdin

input = stdin.readline

_ = input()
nums = list(map(int, input().split()))
gn = 0
dp = [0] * (10 ** 6 + 1)
n = 1
pointer = 0
while pointer + n <= 10 ** 6:
    for dn in range(n):
        dp[pointer + dn] = n - 1
    pointer += n
    n += 1
for num in nums:
    gn ^= dp[num]
print('koosaga' if gn else 'cubelover')
