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
    if scc[idx]:
        return
    scc[idx] = component
    size[component] += 1
    for adj in graph_inv[idx]:
        if not scc[adj]:
            dfs_inv(adj)
        elif scc[adj] != component:
            graph_scc[scc[adj]].add(component)


def dfs_scc(idx):
    if not graph_scc[idx]:
        return size[idx]
    result = size[idx]
    ex = 0
    for adj in graph_scc[idx]:
        ex_now = dfs_scc(adj)
        if ex_now > ex:
            ex = ex_now
    return result + ex


n = int(input())
graph = [[] for _ in range(n + 1)]
graph_inv = [[] for _ in range(n + 1)]
arr = list(map(int, input().split()))
for i in range(n):
    if i + arr[i] < n:
        graph[i + 1].append(i + arr[i] + 1)
        graph_inv[i + arr[i] + 1].append(i + 1)
    if i - arr[i] >= 0:
        graph[i + 1].append(i - arr[i] + 1)
        graph_inv[i - arr[i] + 1].append(i + 1)
start = int(input())
visited = [False] * (n + 1)
stack = []
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
scc = [0] * (n + 1)
size = {}
component = 0
graph_scc = defaultdict(set)
while stack:
    now = stack.pop()
    if not scc[now]:
        component += 1
        size[component] = 0
        dfs_inv(now)
print(dfs_scc(scc[start]))
