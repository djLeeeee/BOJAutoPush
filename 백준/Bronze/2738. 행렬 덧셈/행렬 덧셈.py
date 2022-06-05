n, m = map(int, input().split())
b1 = [list(map(int, input().split())) for _ in range(n)]
b2 = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        b2[i][j] += b1[i][j]
for line in b2:
    print(*line)