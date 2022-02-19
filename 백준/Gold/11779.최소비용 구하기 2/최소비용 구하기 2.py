from sys import stdin as s
from math import inf
import heapq

n = int(s.readline())
m = int(s.readline())
roads = [list(map(int, s.readline().split())) for _ in range(m)]
init, fin = map(int, s.readline().split())
d = [inf] * (n + 1)
d[init] = 0
route = [[] for _ in range(n + 1)]
route[init].append(init)
connection = [[] * (n + 1) for _ in range(n + 1)]
for x, y, z in roads:
    connection[x].append((z, y))
heap = []
heapq.heappush(heap, (0, init))
while heap:
    distance, now = heapq.heappop(heap)
    if d[now] < distance:
        continue
    for cost, i in connection[now]:
        if d[i] > distance + cost:
            d[i] = distance + cost
            heapq.heappush(heap, (d[i], i))
            route[i] = route[now] + [i]
print(d[fin])
print(len(route[fin]))
print(*route[fin])
