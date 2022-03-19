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
    scc[idx] = component
    for adj in graph_inv[idx]:
        if not scc[adj]:
            dfs_inv(adj)
        elif scc[adj] != scc[idx]:
            deg_scc[scc[idx]] = 1


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
    component = 0
    deg_scc = defaultdict(int)
    while stack:
        now = stack.pop()
        if not scc[now]:
            component += 1
            dfs_inv(now)
    start = []
    for i in range(1, component + 1):
        if not deg_scc[i]:
            start.append(i)
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
