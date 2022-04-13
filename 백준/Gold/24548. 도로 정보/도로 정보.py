from sys import stdin
from collections import defaultdict

input = stdin.readline

n = int(input())
road = input().strip()
trans = {'T': 0, 'F': 1, 'G': 2, 'P': 3}
state = defaultdict(int)
state[(0, 0, 0, 0)] = 1
ans = 0
cnt = [0, 0, 0, 0]
for i in range(n):
    cnt[trans[road[i]]] += 1
    cnt[trans[road[i]]] %= 3
    now = tuple(cnt)
    ans += state[now]
    state[now] += 1
print(ans)
