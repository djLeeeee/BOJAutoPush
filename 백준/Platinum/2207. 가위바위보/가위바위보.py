from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 5)


def dfs(idx):
    if visited[idx]:
        return
    visited[idx] = True
    for adj in graph[idx]:
        if not visited[adj]:
            dfs(adj)
    stack.append(idx)


def dfs_inv(idx):
    if scc[idx]:
        return
    scc[idx] = component
    for adj in graph_inv[idx]:
        if not scc[adj]:
            dfs_inv(adj)


def check(arr):
    l = len(arr) // 2
    for j in range(1, l +1):
        if arr[j] == arr[-j]:
            return 'OTL'
    return '^_^'


n, m = map(int, input().split())
graph = [[] for _ in range(2 * m + 1)]
graph_inv = [[] for _ in range(2 * m + 1)]
for _ in range(n):
    x, y = map(int, input().split())
    graph[-x].append(y)
    graph[-y].append(x)
    graph_inv[x].append(-y)
    graph_inv[y].append(-x)
stack = []
visited = [False] * (2 * m + 1)
for i in range(1, m + 1):
    if not visited[i]:
        dfs(i)
    if not visited[-i]:
        dfs(-i)
scc = [0] * (2 * m + 1)
component = 0
while stack:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
print(check(scc))
