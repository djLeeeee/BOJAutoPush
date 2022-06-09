from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 6)


def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    a, b = find(a), find(b)
    parent[a] = b


n = int(input())
parent = list(range(n + 1))
for _ in range(n - 2):
    x, y = map(int, input().split())
    union(x, y)
x, y = {find(i) for i in range(1, n + 1)}
print(x, y)
