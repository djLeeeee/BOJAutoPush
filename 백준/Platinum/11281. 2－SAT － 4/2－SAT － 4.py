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
    if scc[-idx] == component:
        print(0)
        exit()
    elif idx > 0 and scc[-idx] > 0:
        ans[idx] = 1
    for adj in graph[-idx]:
        if not scc[-adj]:
            dfs_inv(-adj)


n, m = map(int, input().split())
graph = [[] for _ in range(2 * n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[-x].append(y)
    graph[-y].append(x)
stack = []
visited = [False] * (2 * n + 1)
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
    if not visited[-i]:
        dfs(-i)
scc = [0] * (2 * n + 1)
component = 0
ans = [0] * (n + 1)
while stack:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
print(1)
print(*ans[1:])
