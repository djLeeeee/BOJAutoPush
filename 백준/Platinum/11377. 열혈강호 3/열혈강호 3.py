from sys import stdin

input = stdin.readline


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    _, *a = map(int, input().split())
    graph[i] = a
match = [0] * (m + 1)
ans = 0
for i in range(1, n + 1):
    visited = [False] * (m + 1)
    ans += dfs(i)
for i in range(1, n + 1):
    if k == 0:
        break
    visited = [False] * (m + 1)
    if dfs(i):
        ans += 1
        k -= 1
print(ans)