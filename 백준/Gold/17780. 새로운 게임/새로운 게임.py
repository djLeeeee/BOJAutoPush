from sys import stdin
from heapq import *

input = stdin.readline


def turn():
    heap = []
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                heappush(heap, board[i][j][0] + [i, j])
    visited = [False] * k
    while heap:
        idx, direction, i, j = heappop(heap)
        if visited[idx]:
            continue
        ni = i + dx[direction]
        nj = j + dy[direction]
        if state[ni][nj] == 0:
            board[ni][nj] += board[i][j]
            board[i][j] = []
        elif state[ni][nj] == 1:
            board[i][j] = board[i][j][::-1]
            if not board[ni][nj] and board[i][j][0][0] > idx:
                heappush(heap, board[i][j][0] + [ni, nj])
            board[ni][nj] += board[i][j]
            board[i][j] = []
        else:
            nd = direction // 2 * 2 + (1 - direction % 2)
            ni = i + dx[nd]
            nj = j + dy[nd]
            board[i][j][0][1] = nd
            if state[ni][nj] <= 1:
                heappush(heap, [idx, nd, i, j])
            else:
                ni, nj = i, j
        if len(board[ni][nj]) >= 4:
            print(t)
            exit()


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
    turn()
print(-1)
