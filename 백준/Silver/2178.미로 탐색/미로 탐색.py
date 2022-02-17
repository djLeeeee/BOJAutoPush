from sys import stdin

r = stdin.readline

n, m = map(int, r().split())
labyrinth = [ ]
for _ in range(n):
    labyrinth.append([int(i) for i in r().strip()])
start = [[0, 0]]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
day = 1
while labyrinth[-1][-1] == 1:
    new_start = [ ]
    for i in start:
        x = i[0]
        y = i[1]
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < n and 0 <= ny < m:
                if labyrinth[nx][ny] == 1:
                    new_start.append([nx, ny])
                    labyrinth[nx][ny] = 0
    day += 1
    start = new_start
print(day)