from sys import stdin

input = stdin.readline


def turn(target, second=False):
    for i in range(n):
        for j in range(n):
            tl = len(board[i][j])
            for l in range(tl):
                idx, direction = board[i][j][l]
                if idx == target:
                    ni = i + dx[direction]
                    nj = j + dy[direction]
                    remain = board[i][j][:l]
                    move = board[i][j][l:]
                    if state[ni][nj] == 0:
                        board[ni][nj] += move
                        board[i][j] = remain
                        if len(board[ni][nj]) >= 4:
                            print(t)
                            exit()
                        return True
                    elif state[ni][nj] == 1:
                        board[i][j] = remain
                        board[ni][nj] += move[::-1]
                        if len(board[ni][nj]) >= 4:
                            print(t)
                            exit()
                        return True
                    else:
                        if not second:
                            nd = direction // 2 * 2 + (1 - direction % 2)
                            board[i][j][l][1] = nd
                            return False


n, k = map(int, input().split())
state = [list(map(int, input().split())) + [2] for _ in range(n)] + [[2] * (n + 1)]
board = [[[] for _ in range(n)] for _ in range(n)]
pieces = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for t in range(k):
    x, y, d = map(int, input().split())
    board[x - 1][y - 1].append([t, d - 1])
for t in range(1, 1001):
    for x in range(k):
        if not turn(x):
            turn(x, True)
print(-1)
