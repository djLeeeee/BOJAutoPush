from sys import stdin as s
from collections import deque

n, m = map(int, s.readline().split())
d = list(map(int, s.readline().split()))
ad = deque(d[:2 * m - 1])
M = max(ad)
result = [M]
for i in range(2 * m - 1, n):
    ad.append(d[i])
    gone = ad.popleft()
    if M < d[i]:
        M = d[i]
    elif gone == M:
        M = max(ad)
    result.append(M)
print(*result)