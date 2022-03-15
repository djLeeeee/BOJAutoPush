p = list(map(int, input().split()))
total = sum(p)
ans = total
for i in range(1, 4):
    ans = min(ans, abs(total - 2 * (p[0] + p[i])))
print(ans)
