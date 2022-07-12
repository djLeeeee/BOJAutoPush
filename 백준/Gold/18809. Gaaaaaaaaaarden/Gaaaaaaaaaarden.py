from sys import stdin

input = stdin.readline


def sol(idx):
    global ans
    if idx == k:
        if remain[1] or remain[2]:
            return
        result = bfs()
        if ans < result:
            ans = result
        return
    for t in range(3):
        if remain[t]:
            remain[t] -= 1
            state[idx] = t
            sol(idx + 1)
            state[idx] = 0
            remain[t] += 1


def bfs():
    gr = [[], [], []]
    visited = [[0] * m for _ in range(n)]
    for idx in range(k):
        x, y = farm[idx]
        if state[idx]:
            gr[state[idx]].append((x, y))
            visited[x][y] = 1
    day = 2
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    result = 0
    while gr[1] and gr[2]:
        day += 1
        new = [set() for _ in range(3)]
        for rx, ry in gr[1]:
            for d in range(4):
                nx = rx + dx[d]
                ny = ry + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and board[nx][ny]:
                        visited[nx][ny] = day
                        new[1].add((nx, ny))
        for gx, gy in gr[2]:
            for d in range(4):
                nx = gx + dx[d]
                ny = gy + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny]:
                        if visited[nx][ny] == day:
                            new[1].remove((nx, ny))
                            result += 1
                            visited[nx][ny] = -1
                        elif not visited[nx][ny]:
                            new[2].add((nx, ny))
                            visited[nx][ny] = 1
        gr = [list(gn) for gn in new]
    return result


n, m, g, r = map(int, input().split())
farm = []
board = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 2:
            farm.append((i, j))
    board.append(line)
k = len(farm)
ans = 0
remain = [10, g, r]
state = [0] * k
sol(0)
print(ans)
