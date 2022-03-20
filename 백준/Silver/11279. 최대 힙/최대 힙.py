import heapq
from sys import stdin as s

N = int(s.readline())
heap = []
for _ in range(N):
    a = int(s.readline())
    if a:
        heapq.heappush(heap,-a)
    else:
        try:
            x = heapq.heappop(heap)
            print(-x)
        except:
            print(0)