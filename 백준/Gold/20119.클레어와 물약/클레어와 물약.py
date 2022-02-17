from sys import stdin as s
from collections import deque

n, m = map(int, s.readline().split())
connection = [[] for _ in range(n + 1)]
receipt_need = [0] * m
for j in range(m):
    new_receipt = list(map(int, s.readline().split()))
    for i in new_receipt[1:-1]:
        connection[i].append((j, new_receipt[-1]))
    receipt_need[j] = new_receipt[0]
L = int(s.readline())
can_make = deque(map(int, s.readline().split()))
ans = set()
while can_make:
    now = can_make.popleft()
    if now in ans:
        continue
    ans.add(now)
    for idx, target in connection[now]:
        receipt_need[idx] -= 1
        if receipt_need[idx] == 0:
            can_make.append(target)
print(len(ans))
print(*sorted(list(ans)))
