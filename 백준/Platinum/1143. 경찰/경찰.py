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
        elif scc[adj] != component:
            deg[component] = 1


n = int(input())
cost = list(map(int, input().split()))
graph = [[] for _ in range(n)]
graph_inv = [[] for _ in range(n)]
for i in range(n):
    line = input()
    for j in range(n):
        if line[j] == 'Y':
            graph[i].append(j)
            graph_inv[j].append(i)
visited = [False] * n
stack = []
for i in range(n):
    if not visited[i]:
        dfs(i)
scc = [0] * n
component = 0
deg = [0] * (n + 1)
while stack:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
my_sum = 0
div = 0
used = [False] * n
for i in range(1, component + 1):
    if not deg[i]:
        div += 1
        ex = 1000
        f = 0
        for j in range(n):
            if scc[j] == i and ex > cost[j]:
                ex = cost[j]
                f = j
        used[f] = True
        my_sum += ex
extra = []
for i in range(n):
    if not used[i]:
        extra.append(cost[i])
extra.sort()
for ex in extra:
    if ex * div < my_sum:
        my_sum += ex
        div += 1
    else:
        break
print(my_sum / div)
