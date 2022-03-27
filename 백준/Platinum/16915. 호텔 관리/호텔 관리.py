from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
input = stdin.readline


def add_edge(a, b):
    graph[a].append(b)
    graph[b].append(a)
    graph[-a].append(-b)
    graph[-b].append(-a)


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
    for adj in graph[idx]:
        if not scc[adj]:
            dfs_inv(adj)


def check(arr, l):
    for j in range(1, l + 1):
        if arr[j] == arr[-j]:
            return 0
    return 1


n, m = map(int, input().split())
on_off = [0] + list(map(int, input().split()))
connection = [[] for _ in range(n + 1)]
for si in range(1, m + 1):
    k, *room_idx = map(int, input().split())
    for ri in room_idx:
        connection[ri].append(si)
graph = [[] for _ in range(2 * m + 1)]
for ri in range(1, n + 1):
    x, y = connection[ri]
    if on_off[ri]:
        add_edge(x, y)
    else:
        add_edge(x, -y)
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
print(check(scc, m))
