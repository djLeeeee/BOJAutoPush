from sys import stdin, setrecursionlimit
from collections import defaultdict

input = stdin.readline
setrecursionlimit(10 ** 6)


def dfs(idx):
    if visited[idx]:
        return
    visited[idx] = True
    for adj in graph[idx]:
        if not visited[adj]:
            dfs(adj)
    stack.append(idx)


def dfs_inv(idx):
    if checked[idx]:
        return
    checked[idx] = True
    for adj in graph_inv[idx]:
        if not checked[adj]:
            dfs_inv(adj)
    scc[idx] = component


t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    graph = defaultdict(list)
    graph_inv = defaultdict(list)
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph_inv[y].append(x)
    scc = [0] * n
    visited = [False] * n
    stack = []
    for i in range(n):
        if not visited[i]:
            dfs(i)
    checked = [False] * n
    component = 0
    while stack:
        now = stack.pop()
        if not checked[now]:
            component += 1
            dfs_inv(now)
    deg = [0] * (component + 1)
    for i in graph:
        for j in graph[i]:
            if scc[i] != scc[j]:
                deg[scc[j]] += 1
    start = []
    for k in range(1, component + 1):
        if deg[k] == 0:
            start.append(k)
    if len(start) >= 2:
        print('Confused')
    else:
        start = start[0]
        for ii in range(n):
            if scc[ii] == start:
                print(ii)
    if tc < t - 1:
        input()
        print()
