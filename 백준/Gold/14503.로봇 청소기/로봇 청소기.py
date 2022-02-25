from sys import stdin as s

m, n = map(int, s.readline().split())
x, y, d = map(int, s.readline().split())
board = []
for _ in range(m):
    board.append(list(map(int, s.readline().split())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0


def clean(x, y, d):
    global ans
    if board[x][y] == 0:
        board[x][y] = -1
        ans += 1
    for _ in range(4):
        nd = d - 1
        if nd < 0:
            nd = 3
        nx = x + dx[nd]
        ny = y + dy[nd]
        if board[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if board[nx][ny] == 1:
        print(ans)
        exit(0)
    clean(nx, ny, d)


clean(x, y, d)

