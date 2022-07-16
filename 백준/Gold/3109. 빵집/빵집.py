from sys import stdin

input = stdin.readline


def dfs(x, y):
    if y == m - 1:
        return 1
    for d in range(3):
        nx = x + dx[d]
        if 0 <= nx < n and arr[nx][y + 1] == '.' and not visited[nx][y + 1]:
            visited[nx][y + 1] = True
            if dfs(nx, y + 1):
                return 1
    return 0


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = 0
dx = [-1, 0, 1]
for i in range(n):
    if arr[i][0] == '.':
        ans += dfs(i, 0)
print(ans)
