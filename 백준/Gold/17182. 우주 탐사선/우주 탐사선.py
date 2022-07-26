from sys import stdin

input = stdin.readline

n, start = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for j in range(n):
    for i in range(n):
        for k in range(n):
            if board[i][k] > board[i][j] + board[j][k]:
                board[i][k] = board[i][j] + board[j][k]
dp = [[float('inf')] * n for _ in range(1 << n)]
dp[1 << start][start] = 0
point = [(1 << start, start)]
for _ in range(n - 1):
    new = set()
    for state, last in point:
        for bit in range(n):
            if not (1 << bit) & state:
                if dp[(1 << bit) + state][bit] > dp[state][last] + board[last][bit]:
                    dp[(1 << bit) + state][bit] = dp[state][last] + board[last][bit]
                    new.add(((1 << bit) + state, bit))
    point = new
print(min(dp[-1]))
