n, m = map(int, input().split())
ans = [-1]
s = (m * m - m) // 2
while s <= n and m <= 100:
    s += m
    if not (n - s) % m:
        ex = (n - s) // m
        ans = list(range(ex + 1, ex + m + 1))
        break
    m += 1
print(*ans)
