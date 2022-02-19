from sys import stdin as s

for _ in range(int(s.readline())):
    n = int(s.readline())
    starts = [list(map(int, s.readline().split()))]
    ax, ay = map(int, s.readline().split())
    dx = [2, 2, 1, 1, -1, -1, -2, -2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]
    visited = [[False] * n for _ in range(n)]
    visited[starts[0][0]][starts[0][1]] = True
    ans = 0
    while not visited[ax][ay]:
        ans += 1
        new_starts = []
        for x, y in starts:
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    new_starts.append([nx, ny])
                    visited[nx][ny] = True
        starts = new_starts
    print(ans)
