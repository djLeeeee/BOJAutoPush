from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
gn = 0
for i in range(n):
    ex = 0
    for j in range(m - 1, -1, -1):
        if not ex:
            ex = board[i][j]
        else:
            if board[i][j] > ex:
                ex = board[i][j]
            else:
                ex = board[i][j] - 1
    gn ^= ex
print("koosaga" if gn else "cubelover")
