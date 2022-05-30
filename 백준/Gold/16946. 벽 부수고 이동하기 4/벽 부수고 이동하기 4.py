from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
ans = [["0"] * m for _ in range(n)]
size = [0] * (n * m + 2)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
idx = 1
for x in range(n):
    for y in range(m):
        if board[x][y] == 1:
            can_go_idx = set()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] == 0:
                        idx += 1
                        board[nx][ny] = idx
                        size[idx] += 1
                        point = [(nx, ny)]
                        while point:
                            xx, yy = point.pop()
                            for dd in range(4):
                                nxx = xx + dx[dd]
                                nyy = yy + dy[dd]
                                if 0 <= nxx < n and 0 <= nyy < m and board[nxx][nyy] == 0:
                                    board[nxx][nyy] = idx
                                    size[idx] += 1
                                    point.append((nxx, nyy))
                    can_go_idx.add(board[nx][ny])
            can_go = 1
            for now in can_go_idx:
                can_go += size[now]
            ans[x][y] = str(can_go % 10)
print('\n'.join([''.join(line) for line in ans]))
