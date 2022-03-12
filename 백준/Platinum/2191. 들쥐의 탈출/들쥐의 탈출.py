from sys import stdin

input = stdin.readline


def dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def dfs(x):
    for adj in graph[x]:
        if visited[adj]:
            continue
        visited[adj] = True
        if match[adj] == 0 or dfs(match[adj]):
            match[adj] = x
            return 1
    return 0


n, m, s, v = map(int, input().split())
rat = [list(map(float, input().split())) for _ in range(n)]
hole = [list(map(float, input().split())) for _ in range(m)]
graph = [[] for _ in range(n + 1)]
d = s * v
for i in range(n):
    for j in range(m):
        if dist(rat[i], hole[j]) <= d * d:
            graph[i + 1].append(j + 1)
match = [0] * (m + 1)
ans = 0
for i in range(1, n + 1):
    visited = [False] * (m + 1)
    ans += dfs(i)
print(n - ans)
