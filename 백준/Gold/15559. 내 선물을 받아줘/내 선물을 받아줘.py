from sys import stdin

input = stdin.readline


def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    a, b = find(a), find(b)
    parent[a] = b


n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
parent = list(range(n * m))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
d = {'S': 0, 'N': 1, 'E': 2, 'W': 3}
ans = n * m
for x in range(n):
    for y in range(m):
        nx = x + dx[d[board[x][y]]]
        ny = y + dy[d[board[x][y]]]
        if 0 <= nx < n and 0 <= ny < m:
            s, e = x * m + y, nx * m + ny
            if find(s) != find(e):
                ans -= 1
                union(s, e)
print(ans)
