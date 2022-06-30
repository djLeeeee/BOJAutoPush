from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
arr = [0] * n
sn = int(n ** 0.5)
sqrt = [0] * (n // sn + 1)
for _ in range(m):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        _, x, y = query
        x -= 1
        sqrt[x // sn] += y
        arr[x] += y
    else:
        _, s, e = query
        s -= 1
        e -= 1
        ss, rs = s // sn, s % sn
        se, re = e // sn, e % sn
        ans = 0
        for si in range(ss, se):
            ans += sqrt[si]
        for ri in range(rs):
            ans -= arr[ss * sn + ri]
        for ri in range(re + 1):
            ans += arr[se * sn + ri]
        print(ans)
