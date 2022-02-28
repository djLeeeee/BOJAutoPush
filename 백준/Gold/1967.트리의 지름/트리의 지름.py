from sys import stdin as s
from sys import setrecursionlimit as st

st(10 ** 6)

input = s.readline

n = int(input())
connection = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y, c = map(int, input().split())
    connection[x].append((y, c))
    connection[y].append((x, c))
visited = [False] * (n + 1)


def dfs(start, distance):
    visited[start] = True
    end, r = start, distance
    for now, cost in connection[start]:
        if not visited[now]:
            ver, dist = dfs(now, distance + cost)
            if dist > r:
                end = ver
                r = dist
    return end, r


s, _ = dfs(1, 0)
visited = [False] * (n + 1)
_, ans = dfs(s, 0)
print(ans)
