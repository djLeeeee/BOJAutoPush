from sys import stdin

input = stdin.readline


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


n = int(input())
board = [list(input().strip()) for _ in range(n)]
row = [[0] * n for _ in range(n)]
col = [[0] * n for _ in range(n)]
rn, cn = 0, 0
for i in range(n):
    for j in range(n):
        if board[i][j] == '.':
            if not row[i][j]:
                rn += 1
                ii, jj = i, j
                while ii < n and jj < n and board[ii][jj] == '.':
                    row[ii][jj] = rn
                    jj += 1
            if not col[i][j]:
                cn += 1
                ii, jj = i, j
                while ii < n and jj < n and board[ii][jj] == '.':
                    col[ii][jj] = cn
                    ii += 1
graph = [[] for _ in range(rn + 1)]
for i in range(n):
    for j in range(n):
        if board[i][j] == '.':
            graph[row[i][j]].append(col[i][j])
match = [0] * (cn + 1)
ans = 0
for i in range(1, rn + 1):
    visited = [False] * (cn + 1)
    ans += dfs(i)
print(ans)
