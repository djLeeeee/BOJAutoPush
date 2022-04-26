from sys import stdin
from collections import defaultdict
from heapq import *


def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


input = stdin.readline

n, f = map(int, input().split())
point = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]
point_cnt = defaultdict(list)
graph = [[] for _ in range(n + 1)]
for i in range(n + 1):
    x, y = point[i]
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            nx = x + dx
            ny = y + dy
            for j in point_cnt[(nx, ny)]:
                graph[i].append(j)
                graph[j].append(i)
    point_cnt[(x, y)].append(i)
INF = float('inf')
dist = [INF] * (n + 1)
dist[0] = 0
heap = [(0, 0)]
ans = -1
while heap:
    d, now = heappop(heap)
    if dist[now] < d:
        continue
    if point[now][1] == f:
        ans = d
        break
    for adj in graph[now]:
        ex = distance(point[now], point[adj])
        if dist[adj] > d + ex:
            dist[adj] = d + ex
            heappush(heap, (dist[adj], adj))
print(round(ans))
