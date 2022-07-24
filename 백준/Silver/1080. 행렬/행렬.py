n, m = map(int, input().split())
b1 = [list(map(int, input())) for _ in range(n)]
b2 = [list(map(int, input())) for _ in range(n)]
ans = 0
for i in range(n - 2):
    for j in range(m - 2):
        if b1[i][j] != b2[i][j]:
            ans += 1
            for di in range(3):
                for dj in range(3):
                    b1[i + di][j + dj] ^= 1
if b1 != b2:
    print(-1)
else:
    print(ans)
