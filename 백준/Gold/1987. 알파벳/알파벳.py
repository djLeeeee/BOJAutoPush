from sys import stdin as s


r, c = map(int, s.readline().split())
board = []
for _ in range(r):
    board.append(s.readline().rstrip())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
start = {(0, 0, board[0][0])}
ans = 1
while start:
    x, y, route = start.pop()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in route:
            start.add((nx, ny, route + board[nx][ny]))
            ans = max(len(route) + 1, ans)
print(ans)
