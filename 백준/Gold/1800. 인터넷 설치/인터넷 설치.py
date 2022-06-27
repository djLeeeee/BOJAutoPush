from sys import stdin
from collections import defaultdict
from heapq import heappop, heappush

input = stdin.readline


def dijkstra(limit):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[1] = 0
    heap = [(0, 1)]
    while heap:
        cost, idx = heappop(heap)
        if idx == n:
            return True
        if dist[idx] < cost:
            continue
        for adj, ex in graph[idx]:
            if ex > limit:
                if cost + 1 < dist[adj] and cost + 1 <= k:
                    dist[adj] = cost + 1
                    heappush(heap, (dist[adj], adj))
            else:
                if cost < dist[adj]:
                    dist[adj] = cost
                    heappush(heap, (dist[adj], adj))
    return False


n, p, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(p):
    x, y, d = map(int, input().split())
    graph[x].append((y, d))
    graph[y].append((x, d))
ans = -1
left = 0
right = 10 ** 6
while left <= right:
    mid = (left + right) // 2
    if dijkstra(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)
