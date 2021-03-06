from sys import stdin

input = stdin.readline


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if match[adj] == 0 or dfs(match[adj]):
            match[adj] = idx
            check[idx] = True
            return 1
    return 0


def coloring(idx):
    used_a[idx] = False
    for adj in graph[idx]:
        if match[adj] != idx:
            used_b[adj] = True
            if used_a[match[adj]]:
                coloring(match[adj])


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
rn = 0
cn = 0
row = [[0] * m for _ in range(n)]
row_inv = {}
col = [[0] * m for _ in range(n)]
col_inv = {}
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and not row[i][j]:
            rn += 1
            jj = j
            while jj < m and board[i][jj] != 2:
                if board[i][jj] == 0:
                    row[i][jj] = rn
                    row_inv[rn] = i + 1
                jj += 1
for j in range(m):
    for i in range(n):
        if board[i][j] == 0 and not col[i][j]:
            cn += 1
            ii = i
            while ii < n and board[ii][j] != 2:
                if board[ii][j] == 0:
                    col[ii][j] = cn
                    col_inv[cn] = j + 1
                ii += 1
graph = [[] for _ in range(rn + 1)]
for i in range(n):
    for j in range(m):
        if not board[i][j]:
            graph[row[i][j]].append(col[i][j])
match = [0] * (cn + 1)
check = [False] * (rn + 1)
ans = 0
for i in range(1, rn + 1):
    visited = [False] * (cn + 1)
    ans += dfs(i)
print(ans)
for i in range(1, cn + 1):
    if match[i]:
        print(row_inv[match[i]], col_inv[i])
