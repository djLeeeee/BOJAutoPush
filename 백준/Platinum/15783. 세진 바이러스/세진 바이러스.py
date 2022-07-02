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
        if scc[adj]:
            if scc[adj] != component:
                deg[scc[idx]] += 1
        else:
            dfs_inv(adj)


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
graph_inv = [[] for _ in range(n)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph_inv[e].append(s)
visited = [False] * n
stack = []
for i in range(n):
    if not visited[i]:
        dfs(i)
component = 0
scc = [0] * n
deg = [0] * (n + 1)
while stack:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
ans = 0
for i in range(1, component + 1):
    if not deg[i]:
        ans += 1
print(ans)
