# 1865 웜홀
from sys import stdin as s

input = s.readline


def fw():
    for jj in range(1, n + 1):
        for ii in range(1, n + 1):
            for kk in range(1, n + 1):
                connection[ii][kk] = min(connection[ii][kk], connection[ii][jj] + connection[jj][kk])
            if connection[ii][ii] < 0:
                return 'YES'
    return 'NO'


INF = int(1e9)
for _ in range(int(input())):
    n, m, w = map(int, input().split())
    connection = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        connection[i][i] = 0
    for _ in range(m):
        x, y, c = map(int, input().split())
        connection[x][y] = min(connection[x][y], c)
        connection[y][x] = connection[x][y]
    for _ in range(w):
        wx, wy, wc = map(int, input().split())
        connection[wx][wy] = min(connection[wx][wy], -wc)
    print(fw())
