from sys import stdin as s
import heapq

n, m = map(int, s.readline().split())
connection = [[] for _ in range(n + 1)]
get_in = [0] * (n + 1)
parents = [ ]
result = [ ]
for _ in range(m):
    a = list(map(int, s.readline().split()))
    for i in range(1, a[0]):
        x, y = a[i], a[i + 1]
        connection[x].append(y)
        get_in[y] += 1        
for i in range(1, n + 1):
    if get_in[i] == 0:
        heapq.heappush(parents, i)

while parents:
    a = heapq.heappop(parents)
    result.append(a)
    for j in connection[a]:
        get_in[j] -= 1
        if get_in[j] == 0:
            heapq.heappush(parents, j)
if len(result) == n:
    print(*result, sep = '\n')
else:
    print(0)