from sys import stdin

input = stdin.readline


def dfs(idx):
    for adj, cost in graph[idx]:
        if visited[adj]:
            continue
        if cost <= mid:
            visited[adj] = True
            if not match[adj] or dfs(match[adj]):
                match[adj] = idx
                return 1
    return 0


r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
car = 0
parking = 0
for i in range(r):
    for j in range(c):
        if board[i][j] == 'C':
            car += 1
            board[i][j] = car
        elif board[i][j] == 'P':
            parking += 1
            board[i][j] = -parking
        elif board[i][j] == 'X':
            board[i][j] = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = [[] for _ in range(car + 1)]
max_d = 0
if car == 0:
    print(0)
    exit()
if car > parking:
    print(-1)
    exit()
for i in range(r):
    for j in range(c):
        if board[i][j] != '.' and board[i][j] > 0:
            dist = 0
            starts = [(i, j)]
            check = [[0] * c for _ in range(r)]
            check[i][j] = -1
            while starts:
                new = []
                dist += 1
                for x, y in starts:
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] and not check[nx][ny]:
                            check[nx][ny] = dist
                            new.append((nx, ny))
                            if board[nx][ny] != '.' and board[nx][ny] < 0:
                                graph[board[i][j]].append((-board[nx][ny], dist))
                                if max_d < dist:
                                    max_d = dist
                starts = new
            if not graph[board[i][j]]:
                print(-1)
                exit()
ans = -1
start = 1
end = max_d
while start <= end:
    mid = (start + end) // 2
    match = [0] * (parking + 1)
    for i in range(1, car + 1):
        visited = [False] * (parking + 1)
        if not dfs(i):
            start = mid + 1
            break
    else:
        end = mid - 1
        if ans == -1:
            ans = mid
        else:
            ans = min(ans, mid)
print(ans)
