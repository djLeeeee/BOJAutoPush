from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 5)


def update(idx):
    result = 1
    for adj, _ in tree[idx]:
        result += update(adj)
    child_size[idx] = result
    return result


while True:
    n = int(input())
    if not n:
        break
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        x, y, d = map(int, input().split())
        graph[x].append((y, d))
        graph[y].append((x, d))
    tree = [[] for _ in range(n)]
    visited = [-1] * n
    point = [0]
    visited[0] = 0
    dp = [0] * n
    while point:
        now = point.pop()
        for nei, d in graph[now]:
            if visited[nei] == -1:
                visited[nei] = visited[now] + d
                dp[0] += visited[nei]
                point.append(nei)
                tree[now].append((nei, d))
    child_size = [0] * n
    update(0)
    point = [0]
    while point:
        now = point.pop()
        for nei, d in tree[now]:
            dp[nei] = dp[now] + (n - 2 * child_size[nei]) * d
            point.append(nei)
    print(min(dp))
