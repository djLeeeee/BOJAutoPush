from sys import setrecursionlimit, stdin

setrecursionlimit(10 ** 4)


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
    for j in range(1, n + 1):
        if arr[j] == arr[-j]:
            return 0
    return 1


input = map(int, stdin.read().split())
while True:
    try:
        n = next(input)
    except:
        break
    m = next(input)
    graph = [[] for _ in range(2 * n + 1)]
    graph_inv = [[] for _ in range(2 * n + 1)]
    for _ in range(m):
        x, y = next(input), next(input)
        graph[-x].append(y)
        graph[-y].append(x)
        graph_inv[x].append(-y)
        graph_inv[y].append(-x)
    stack = []
    visited = [False] * (2 * n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
        if not visited[-i]:
            dfs(-i)
    del graph
    scc = [0] * (2 * n + 1)
    component = 0
    while stack:
        now = stack.pop()
        if not scc[now]:
            component += 1
            dfs_inv(now)
    del graph_inv
    print(check(scc))