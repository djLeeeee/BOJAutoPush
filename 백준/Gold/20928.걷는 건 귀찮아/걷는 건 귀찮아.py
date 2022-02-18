from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
p = list(map(int, input().split()))
x = list(map(int, input().split()))
route = [0] * 1000001
for i in range(n):
    route[p[i]] = x[i]
ans = 0
now = p[0]
while now < m and now + route[now] < m:
    can_go = []
    for i in range(now + 1, now + route[now] + 1):
        if route[i]:
            can_go.append((i + route[i], i))
    if can_go:
        a, now = max(can_go)
        ans += 1
    else:
        ans = -1
        break
print(ans)
