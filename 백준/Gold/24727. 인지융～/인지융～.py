n = int(input())
c, e = map(int, input().split())
board = [[0] * n for _ in range(n)]
for xy in range(2 * n):
    for x in range(xy + 1):
        y = xy - x
        if c:
            if 0 <= x < n and 0 <= y < n:
                board[x][y] = 1
                c -= 1
        else:
            break
    if not c:
        break
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]
for i in range(n):
    for j in range(n):
        if not e:
            break
        if not board[i][j]:
            flag = True
            for d in range(2):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 1:
                    flag = False
            if flag:
                e -= 1
                board[i][j] = 2
                point = [(i, j)]
                while e and point:
                    x, y = point.pop()
                    for d in range(4):
                        nx = x + di[d]
                        ny = y + dj[d]
                        if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                            flag = True
                            for dd in range(2):
                                nnx = nx + di[dd]
                                nny = ny + dj[dd]
                                if 0 <= nnx < n and 0 <= nny < n and board[nnx][nny] == 1:
                                    flag = False
                            if flag and e:
                                board[nx][ny] = 2
                                e -= 1
                                point.append((nx, ny))
    if not e:
        break
if not e:
    print(1)
    for line in board:
        print(*line, sep='')
else:
    print(-1)
