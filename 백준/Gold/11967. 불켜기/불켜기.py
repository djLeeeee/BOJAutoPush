from sys import stdin
from collections import defaultdict

input = stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, c, d = map(int, input().split())
    graph[(a - 1, b - 1)].append((c - 1, d - 1))
result = 1
point = [(0, 0)]
visited = [[False] * n for _ in range(n)]
light = [[False] * n for _ in range(n)]
visited[0][0] = True
light[0][0] = True
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
flag = True
while flag:
    new = []
    flag = False
    for x, y in point:
        for z, w in graph[(x, y)]:
            if not light[z][w]:
                light[z][w] = True
                result += 1
    for x, y in point:
        check = False
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                check = True
                if light[nx][ny]:
                    visited[nx][ny] = True
                    new.append((nx, ny))
                    flag = True
        if check:
            new.append((x, y))
    point = new
print(result)
