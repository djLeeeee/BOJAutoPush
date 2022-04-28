from sys import stdin as s


def tomato(starts, M, N):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    result = 0
    good = 0
    while starts:
        result += 1
        new = []
        for x, y in starts:
            for d in range(4):
                p = x + dx[d]
                q = y + dy[d]
                if 0 <= p < N and 0 <= q < M and g[p][q] == 0:
                    new.append((p, q))
                    g[p][q] = result
                    good += 1
        starts = new
    if good == rare:
        return result - 1
    return -1


m, n = map(int, s.readline().split())
g = []
start_points = []
rare = 0
for i in range(n):
    a = list(map(int, s.readline().split()))
    for j in range(m):
        if a[j] == 1:
            start_points.append((i, j))
        elif a[j] == 0:
            rare += 1
    g.append(a)
print(tomato(start_points, m, n))