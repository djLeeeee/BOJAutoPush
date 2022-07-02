from sys import stdin

input = stdin.readline


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


n = int(input())
cost = list(map(int, input().split()))
graph = [[] for _ in range(n)]
graph_inv = [[] for _ in range(n)]
for i in range(n):
    line = input()
    for j in range(n):
        if line[j] == '1':
            graph[i].append(j)
            graph_inv[j].append(i)
visited = [False] * n
stack = []
for i in range(n):
    if not visited[i]:
        dfs(i)
scc = [0] * n
component = 0
while stack:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
ans = [10 ** 6] * (component + 1)
for i in range(n):
    if ans[scc[i]] > cost[i]:
        ans[scc[i]] = cost[i]
print(sum(ans[1:]))
