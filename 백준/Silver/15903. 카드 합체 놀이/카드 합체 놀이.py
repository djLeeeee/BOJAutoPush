from heapq import *
from sys import stdin
input = stdin.readline
m, n = map(int, input().split())
heap = list(map(int, input().split()))
heapify(heap)
for _ in range(n):
    a = heappop(heap)
    b = heappop(heap)
    heappush(heap, a + b)
    heappush(heap, a + b)
print(sum(heap))