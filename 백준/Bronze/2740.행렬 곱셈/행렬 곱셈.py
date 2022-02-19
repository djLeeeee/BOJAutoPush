from sys import stdin as s

n, m = map(int, s.readline().split())
first = [list(map(int, s.readline().split())) for _ in range(n)]
m, k = map(int, s.readline().split())
second = [list(map(int, s.readline().split())) for _ in range(m)]
ans = [[0] * k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for x in range(m):
            ans[i][j] += first[i][x] * second[x][j]
for line in ans:
    print(*line)
