from sys import stdin

input = stdin.readline


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if match[adj] == 0 or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
bn = 0
wn = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == '.':
            if (i - j) % 2:
                bn += 1
                board[i][j] = bn
            else:
                wn += 1
                board[i][j] = wn
        else:
            board[i][j] = 0
graph = [[] for _ in range(bn + 1)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    for j in range(m):
        if board[i][j] and (i - j) % 2:
            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < n and 0 <= nj < m and board[ni][nj]:
                    graph[board[i][j]].append(board[ni][nj])
match = [0] * (wn + 1)
ans = bn + wn
for i in range(1, bn + 1):
    visited = [False] * (wn + 1)
    ans -= dfs(i)
print(ans)
