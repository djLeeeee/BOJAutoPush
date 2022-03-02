# 2533 사회망 서비스
from sys import stdin as s
from collections import deque

input = s.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
deg = [len(graph[i]) for i in range(n + 1)]
leaves = deque()
for j in range(1, n + 1):
    if deg[j] == 1:
        leaves.append(j)
dp = [[0, 0] for _ in range(n + 1)]
while leaves:
    now = leaves.popleft()
    dp[now][1] = 1
    for adj in graph[now]:
        deg[adj] -= 1
        if deg[adj] == 1:
            leaves.append(adj)
        dp[now][0] += dp[adj][1]
        dp[now][1] += min(dp[adj])
print(min(dp[now]))
