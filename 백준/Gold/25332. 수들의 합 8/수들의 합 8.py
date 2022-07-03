from sys import stdin
from collections import defaultdict

input = stdin.readline

n = int(input())
my_sum = [0] * (n + 1)
a = list(map(int, input().split()))
b = list(map(int, input().split()))
memo = defaultdict(list)
memo[0].append(0)
for i in range(1, n + 1):
    my_sum[i] = a[i - 1] - b[i - 1] + my_sum[i - 1]
    memo[my_sum[i]].append(i)
ans = 0
for k in memo.values():
    l = len(k)
    ans += (l * l - l) // 2
print(ans)