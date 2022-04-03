from sys import stdin
from copy import deepcopy

input = stdin.readline


def dfs(idx):
    for adj in graph[idx]:
        if not visited[adj]:
            visited[adj] = True
            if match[adj] < 0 or dfs(match[adj]):
                match[adj] = idx
                check[idx] = True
                return 1
    return 0


def coloring(idx):
    used_row[idx] = False
    for adj in graph[idx]:
        if match[adj] != idx and match[adj] >= 0:
            used_col[adj] = True
            if used_row[match[adj]]:
                coloring(match[adj])


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
new_board = deepcopy(board)
for i in range(n):
    m = min(board[i])
    for j in range(n):
        board[i][j] -= m
for i in range(n):
    m = min([board[k][i] for k in range(n)])
    for j in range(n):
        board[j][i] -= m
graph = [set() for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            graph[i].add(j)
while True:
    result = 0
    match = [-1] * n
    check = [False] * n
    for i in range(n):
        visited = [False] * n
        result += dfs(i)
    if result == n:
        break
    else:
        used_row = [True] * n
        used_col = [False] * n
        for i in range(n):
            if not check[i] and used_row[i]:
                coloring(i)
        m = 100000
        zero = []
        double = []
        for i in range(n):
            for j in range(n):
                if not used_row[i] and not used_col[j]:
                    if m > board[i][j]:
                        m = board[i][j]
                    zero.append((i, j))
                elif used_row[i] and used_col[j]:
                    double.append((i, j))
        for x, y in zero:
            board[x][y] -= m
            if board[x][y] == 0:
                graph[x].add(y)
        for x, y in double:
            board[x][y] += m
            if board[x][y] == m:
                graph[x].remove(y)
ans = 0
for j in range(n):
    ans += new_board[match[j]][j]
print(ans)
