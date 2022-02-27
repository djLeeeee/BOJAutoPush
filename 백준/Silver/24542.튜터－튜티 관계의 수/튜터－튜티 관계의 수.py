from sys import stdin as s
from sys import setrecursionlimit as st

st(10 ** 6)

input = s.readline

div = 1000000007
n, m = map(int, input().split())
p = list(range(n + 1))


def find(t):
    if t == p[t]:
        return t
    p[t] = find(p[t])
    return p[t]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


for _ in range(m):
    x, y = map(int, input().split())
    union(x, y)


tr = {}
for i in range(1, n + 1):
    j = find(i)
    tr[j] = tr.get(j, 0) + 1
ans = 1
for num in tr.values():
    ans *= num
    ans %= div
print(ans)
