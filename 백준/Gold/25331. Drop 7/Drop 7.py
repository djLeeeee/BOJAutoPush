now = [list(map(int, input().split())) + [0] for _ in range(7)]
ans = float('inf')
ball = int(input())
for j in range(7):
    board = [line[:] for line in now]
    board[0][j] = ball
    flag = True
    while flag:
        flag = False
        for x in range(6, 0, -1):
            for y in range(7):
                if not board[x][y]:
                    for nx in range(x - 1, -1, -1):
                        if board[nx][y]:
                            board[x][y] = board[nx][y]
                            board[nx][y] = 0
                            break
        # 세로 컴포넌트
        cc = [[0] * 7 for _ in range(7)]
        # 가로 컴포넌트
        rc = [[0] * 7 for _ in range(7)]
        for x in range(7):
            for y in range(7):
                if board[x][y]:
                    if not cc[x][y]:
                        for nx in range(x, 7):
                            cc[nx][y] = 7 - x
                    if not rc[x][y]:
                        ny = y
                        while board[x][ny]:
                            ny += 1
                            rc[x][y] += 1
                        for yy in range(y + 1, ny):
                            rc[x][yy] = rc[x][y]
        for x in range(7):
            for y in range(7):
                if board[x][y]:
                    if board[x][y] == rc[x][y] or board[x][y] == cc[x][y]:
                        board[x][y] = 0
                        flag = True
    remain = 0
    for ii in range(7):
        for jj in range(7):
            if board[ii][jj]:
                remain += 1
    if remain < ans:
        ans = remain
print(ans)
