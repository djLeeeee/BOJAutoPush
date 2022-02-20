from sys import stdin as s

# 53점
n = int(s.readline())
plane = [[0] * 1001 for _ in range(1001)]
result = [ 0 ] * (n + 1)
for k in range(1, n + 1):
    x, y, dx, dy = map(int, s.readline().split())
    for i in range(x, x + dx):
        for j in range(y, y + dy):
            if plane[i][j]:
                result[plane[i][j]] -= 1
            plane[i][j] = k
    result[k] = dx * dy
for area in result[1:]:
    print(area)