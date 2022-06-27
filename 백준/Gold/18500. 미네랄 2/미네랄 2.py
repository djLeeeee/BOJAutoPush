from sys import stdin

input = stdin.readline


def change(x, y):
    board[x][y] = '.'
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False] * m for _ in range(n + 1)]
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx <= n and 0 <= ny < m and board[nx][ny] == 'x':
            if not visited[nx][ny]:
                visited[nx][ny] = True
                cluster = []
                point = [(nx, ny)]
                is_isolated = True
                while point:
                    mx, my = point.pop()
                    if not mx:
                        is_isolated = False
                    cluster.append([mx, my])
                    for dd in range(4):
                        nmx = mx + dx[dd]
                        nmy = my + dy[dd]
                        if 0 <= nmx <= n and 0 <= nmy < m and board[nmx][nmy] == 'x':
                            if not visited[nmx][nmy]:
                                visited[nmx][nmy] = True
                                point.append((nmx, nmy))
                if is_isolated:
                    fall(cluster)
                    return


def fall(points):
    is_isolated = True
    points.sort()
    visited = [[False] * m for _ in range(n + 1)]
    while is_isolated:
        for p in range(len(points)):
            x, y = points[p]
            if board[x - 2][y] == 'x' and not visited[x - 2][y]:
                is_isolated = False
            board[x][y] = '.'
            board[x - 1][y] = 'x'
            visited[x - 1][y] = True
            points[p][0] -= 1


n, m = map(int, input().split())
board = [['x'] * m] + [[] for _ in range(n)]
for i in range(1, n + 1):
    board[-i] = list(input().strip())
t = int(input())
orders = list(map(int, input().split()))
for i in range(t):
    h = orders[i]
    if i % 2:
        yy = m - 1
        while yy >= 0 and board[h][yy] == '.':
            yy -= 1
        if yy >= 0:
            change(h, yy)
    else:
        yy = 0
        while yy < m and board[h][yy] == '.':
            yy += 1
        if yy < m:
            change(h, yy)
for line in board[-1:-(n + 1):-1]:
    print(''.join(line))
