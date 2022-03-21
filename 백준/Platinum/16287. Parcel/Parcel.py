from collections import defaultdict
from sys import stdin

input = stdin.readline


def sol(array, l, t):
    dp = defaultdict(bool)
    for i in range(l - 1):
        for j in range(i + 1, l):
            if dp[t - array[i] - array[j]]:
                return 'YES'
        for k in range(i):
            dp[nums[i] + nums[k]] = True
    return 'NO'


target, m = map(int, input().split())
nums = list(map(int, input().split()))
print(sol(nums, m, target))
