from sys import stdin

input = stdin.readline


def sol(x, y, d1, d2):
    region = [[0] * (n + 2) for _ in range(n + 2)]
    start = y
    end = y
    yy = 0
    xx = x
    tot = [0] * 5
    while start <= end:
        region[xx][start:end + 1] = [5] * (end - start + 1)
        tot[4] += sum(board[xx][start:end + 1])
        if yy < d1:
            start -= 1
        else:
            start += 1
        if yy < d2:
            end += 1
        else:
            end -= 1
        yy += 1
        xx += 1
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if not region[r][c]:
                if 1 <= r < x + d1 and 1 <= c <= y:
                    tot[0] += board[r][c]
                elif 1 <= r <= x + d2 and y < c <= n:
                    tot[1] += board[r][c]
                elif x + d1 <= r <= n and 1 <= c < y - d1 + d2:
                    tot[2] += board[r][c]
                elif x + d2 < r <= n and y - d1 + d2 <= c <= n:
                    tot[3] += board[r][c]
    return max(tot) - min(tot)


n = int(input())
board = [[0] * (n + 2) for _ in range(n + 2)]
for i in range(1, n + 1):
    board[i][1:-1] = list(map(int, input().split()))
ans = 10000
for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):
                try:
                    ans = min(ans, sol(x, y, d1, d2))
                except IndexError:
                    continue
print(ans)
