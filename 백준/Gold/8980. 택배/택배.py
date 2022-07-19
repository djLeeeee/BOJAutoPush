from sys import stdin

input = stdin.readline

town, limit = map(int, input().split())
n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]
info.sort(key=lambda x: (x[1], x[0]))
ans = 0
luggage = [0] * town
for s, e, t in info:
    ml = max(luggage[s:e])
    ex = min(limit - ml, t)
    if ex:
        ans += ex
        for i in range(s, e):
            luggage[i] += ex
print(ans)
