from sys import stdin
from collections import defaultdict

input = stdin.readline

n = int(input())
cnt = defaultdict(int)
ans = ''
m = 0
for _ in range(n):
    target = input().strip()
    cnt[target] += 1
    if cnt[target] > m:
        ans = target
        m = cnt[target]
    elif cnt[target] == m and target < ans:
        ans = target
print(ans)
